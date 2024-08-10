import os
from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.logger import Logger

PREPARE_COMMIT_MSG_BASH_SCRIPT="""#!/usr/bin/env bash

# check if commit message is empty
if ! grep -v "^#" "$1" | grep -q -v "^$"; then
    git-ai-commit hook --run
fi
"""

def get_prepare_commit_msg_hook_path():
    git_repo_path = GitService.get_git_directory()
    return git_repo_path + '/hooks/prepare-commit-msg'

def handle_setup_hook():
    Logger().log("Setting up prepare-commit-msg hook")

    file_path = get_prepare_commit_msg_hook_path()

    hook_content = ""
    if os.path.exists(file_path):
      with open(file_path, 'r') as file:
          hook_content = file.read()

    if hook_content == PREPARE_COMMIT_MSG_BASH_SCRIPT:
        Logger().log("prepare-commit-msg hook already exists")
        return

    if hook_content:
      override_content = input("prepare-commit-msg hook already exists. Would you like to overwrite it? (y/n): ")

      if override_content.lower() == 'n':
        return
      elif override_content.lower() != 'y':
        Logger().log("Invalid input. Exiting.")

    ## create the prepare-commit-msg file and write the hook code
    with open(file_path, 'w') as file:
        file.write(PREPARE_COMMIT_MSG_BASH_SCRIPT)

    # make the file executable
    os.chmod(file_path, 0o755)

def handle_remove_hook():
    Logger().log("Removing prepare-commit-msg hook")

    file_path = get_prepare_commit_msg_hook_path()

    try:
        os.remove(file_path)
        Logger().log("prepare-commit-msg hook removed")
    except FileNotFoundError:
        Logger().log("prepare-commit-msg hook does not exist")

    return

def hook_handler(args):
    if args.setup:
        handle_setup_hook()
    elif args.remove:
        handle_remove_hook()
    elif args.run:
        Logger().log("Running prepare-commit-msg hook")
        prepare_commit_msg_hook()

    return