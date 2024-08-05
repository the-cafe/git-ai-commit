from __future__ import annotations

import subprocess
import os
from prepare_commit_msg_hooks.openai_service import OpenAiService
from prepare_commit_msg_hooks.utils import execute_cli_command, get_repo_root_directory, get_git_directory
from prepare_commit_msg_hooks.logger import Logger
from typing import Sequence


def get_staged_diff():
    # git diff --cached is used to get the staged changes to give to the AI to generate commit message
    return execute_cli_command(['git', 'diff', '--staged'], get_repo_root_directory())

def generate_commit_message():
    staged_diff = get_staged_diff()

    COMMIT_MSG_SYSTEM_MESSAGE = '''
You will be provided with a set of code changes in diff format.
Your task is to read each file and explain every major change in a concise way.

Be sure to include details of major changes

You don't need to add any punctuation or capitalization.

Instead of and, use a comma to save characters.
Only respond with a short sentence no longer than 50 characters that I can use for my commit message
    '''

    print(staged_diff.stdout)

    ai_gen_commit_msg = OpenAiService().chat_with_openai([
        {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
        {"role": "user", "content": staged_diff.stdout},
    ])

    return ai_gen_commit_msg.strip()

def main(argv: Sequence[str] | None = None) -> str:
    commit_message = "✨" + generate_commit_message()

    Logger().log("✨AI: " + commit_message)

    git_directory = get_repo_root_directory()
    # open COMMIT_EDITMSG file to add the generated commit message
    commit_editmsg_file = git_directory + '/.git/COMMIT_EDITMSG'
    Logger().log("commit_editmsg_file: " + commit_editmsg_file)

    existing_content = ""

    try:
        with open(commit_editmsg_file, 'r') as file:
            existing_content = file.read()
    except FileNotFoundError:
        pass

    # Prepend the new content
    new_content = commit_message + '\n' + existing_content

    with open(commit_editmsg_file, 'w') as file:
        file.write(new_content)

    sleep

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
