import os
import uuid

from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.services.husky_service import HuskyService
from ai_commit_msg.services.pip_service import PipService
from ai_commit_msg.utils.logger import Logger


def get_bash_script():
    version = PipService.get_version()
    id = uuid.uuid4()

    PREPARE_COMMIT_MSG_BASH_SCRIPT = f"""#!/usr/bin/env bash
# This file was generated by git-ai-commit: https://github.com/the-cafe/git-ai-commit
# version: {version}
# hash: {id}

# check if git-ai-commit is installed
if ! command -v git-ai-commit &> /dev/null; then
    echo "⚠️ Warning: git-ai-commit is not installed. To install it run \n\n pip install git-ai-commit \n"
    exit 0
fi

# check if commit message is empty
if ! grep -v "^#" "$1" | grep -q -v "^$"; then
    git-ai-commit hook --run
fi
"""
    return PREPARE_COMMIT_MSG_BASH_SCRIPT


def handle_setup_hook(hook_directory_path: str):
    existing_hook_content = ""
    if os.path.exists(hook_directory_path):
        with open(hook_directory_path, "r") as file:
            existing_hook_content = file.read()

    if existing_hook_content == get_bash_script():
        Logger().log("prepare-commit-msg hook already exists")
        return

    if existing_hook_content:
        override_content = input(
            f"prepare-commit-msg hook already exists in {hook_directory_path}\n\nWould you like to overwrite it? (y/n): "
        )

        if override_content.lower() == "n":
            return
        elif override_content.lower() != "y":
            Logger().log("Invalid input. Exiting.")

    ## create the prepare-commit-msg file and write the hook code
    with open(hook_directory_path, "w") as file:
        file.write(get_bash_script())

    # make the file executable
    os.chmod(hook_directory_path, 0o755)


def handle_remove_hook():
    Logger().log("Removing prepare-commit-msg hook")

    file_path = GitService.get_git_prepare_commit_msg_hook_path()

    try:
        os.remove(file_path)
        Logger().log("prepare-commit-msg hook removed")
    except FileNotFoundError:
        Logger().log("prepare-commit-msg hook does not exist")

    return


def setup_husky_git_hook():
    Logger().log("[Setup] Husky prepare-commit-msg hook")

    if not HuskyService.repo_has_husky_framework():
        Logger().log(
            "Husky framework not found in the repository. Please install husky - https://typicode.github.io/husky/"
        )
        return

    file_path = HuskyService.get_husky_prepare_commit_msg_hook_path()
    handle_setup_hook(file_path)

    return


def setup_git_hook():
    Logger().log("[Setup] Git prepare-commit-msg hook")

    # check if husky is installed, if it is, setup husky hook
    if HuskyService.repo_has_husky_framework():
        setup_husky_git_hook()

    file_path = GitService.get_git_prepare_commit_msg_hook_path()
    handle_setup_hook(file_path)

    return


def hook_handler(args):
    if args.setup:
        setup_git_hook()
        return

    if args.setup_husky:
        setup_husky_git_hook()
        return

    if args.remove:
        handle_remove_hook()
        return

    if args.run:
        Logger().log("Running prepare-commit-msg hook")
        prepare_commit_msg_hook()
        return

    return
