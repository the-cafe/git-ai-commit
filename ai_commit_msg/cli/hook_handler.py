from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.logger import Logger

BASH_SCRIPT="""#!/usr/bin/env bash

# check if commit message is empty
if ! grep -v "^#" "$1" | grep -q -v "^$"; then
    # call aicommits hook --setup
    git_ai_commit hook --run
fi
"""

def handle_hook_setup():
    print("Setting up prepare-commit-msg hook")

    git_repo_path = GitService.get_git_directory()
    file_path = git_repo_path + '/hooks/prepare-commit-msg'

    print("file_path: " + file_path)

    ## create the prepare-commit-msg file and write the hook code
    with open(file_path, 'w') as file:
        file.write(BASH_SCRIPT)


def hook_handler(args):
    if args.setup:
        handle_hook_setup()
    elif args.remove:
        print("Removing prepare-commit-msg hook")
    elif args.run:
        Logger().log("Running prepare-commit-msg hook")
        prepare_commit_msg_hook()

    return