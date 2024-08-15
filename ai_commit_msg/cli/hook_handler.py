import os
from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.logger import Logger

PREPARE_COMMIT_MSG_BASH_SCRIPT="""#!/usr/bin/env bash

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

def get_git_prepare_commit_msg_hook_path():
    git_repo_path = GitService.get_git_directory()
    return git_repo_path + '/hooks/prepare-commit-msg'

def get_husky_prepare_commit_msg_hook_path():
    git_repo_path = GitService.get_repo_root_directory()
    return git_repo_path + '/.husky/prepare-commit-msg'

def handle_setup_hook(hook_directory_path: str):
    Logger().log("Setting up prepare-commit-msg hook")

    existing_hook_content = ""
    if os.path.exists(hook_directory_path):
      with open(hook_directory_path, 'r') as file:
          existing_hook_content = file.read()

    if existing_hook_content == PREPARE_COMMIT_MSG_BASH_SCRIPT:
        Logger().log("prepare-commit-msg hook already exists")
        return

    if existing_hook_content:
      override_content = input("prepare-commit-msg hook already exists. Would you like to overwrite it? (y/n): ")

      if override_content.lower() == 'n':
        return
      elif override_content.lower() != 'y':
        Logger().log("Invalid input. Exiting.")

    ## create the prepare-commit-msg file and write the hook code
    with open(hook_directory_path, 'w') as file:
        file.write(PREPARE_COMMIT_MSG_BASH_SCRIPT)

    # make the file executable
    os.chmod(hook_directory_path, 0o755)


def handle_remove_hook():
    Logger().log("Removing prepare-commit-msg hook")

    file_path = get_git_prepare_commit_msg_hook_path()

    try:
        os.remove(file_path)
        Logger().log("prepare-commit-msg hook removed")
    except FileNotFoundError:
        Logger().log("prepare-commit-msg hook does not exist")

    return

def hook_handler(args):
    if args.setup:
        file_path = get_git_prepare_commit_msg_hook_path()
        handle_setup_hook(file_path)
    if args.setup_husky:
        file_path = get_husky_prepare_commit_msg_hook_path()
        handle_setup_hook(file_path)
    elif args.remove:
        handle_remove_hook()
    elif args.run:
        Logger().log("Running prepare-commit-msg hook")
        prepare_commit_msg_hook()

    return