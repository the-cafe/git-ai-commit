from __future__ import annotations

import os
import sys
import subprocess

from prepare_commit_msg_hooks.openai_service import OpenAiService
# from prepare_commit_msg_hooks.utils import Utils
from datetime import datetime, timedelta, timezone

def get_file_directory():
    return os.path.dirname(os.path.realpath(__file__))

def get_current_time():
  EST = timezone(timedelta(hours=-5))  # Adjusted to UTC-5 for Eastern Standard Time
  now_utc = datetime.now(timezone.utc)  # Get the current time in UTC
  now_est = now_utc.astimezone(EST)  # Convert UTC to Eastern Standard Time

  # Format the datetime object to exclude milliseconds
  current_time = now_est.strftime('%Y-%m-%dT%H:%M:%S%z')  # ISO 8601 format without milliseconds

  return str(current_time)

def write_to_logs(message, log_path):
  new_line = "" if message.endswith('\n') else "\n"
  logged_string = "[" + get_current_time() + "] " + str(message) + new_line
  print(logged_string)

  open_mode = "a" if os.path.exists(log_path) else "w"

  with open(log_path, open_mode) as file:
    file.write(logged_string)


def execute_cli_command(cmd_string_list, cwd=None):
    try:
        result = subprocess.run(
            cmd_string_list,
            cwd=cwd,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60  # timeout in 1m/60s
        )
        return result
    except subprocess.CalledProcessError as e:
        cmd_string = " ".join(cmd_string_list)
        error_msg = f"🚨 Total failure to call: {cmd_string}\n{e.stderr}"
        raise Exception(error_msg)

def get_staged_diff():
    script_directory =  execute_cli_command(['git', 'rev-parse', '--git-dir']).stdout.rstrip()

    print('script_directory: ' + script_directory)

    # git diff --cached is used to get the staged changes to give to the AI to generate commit message
    return execute_cli_command(['git', 'diff', '--staged'], script_directory)

def generate_commit_message(openai_key: str) -> str:
    staged_diff = get_staged_diff()

    COMMIT_MSG_SYSTEM_MESSAGE = '''
You will be provided with a set of code changes in diff format.
Your task is to read each file and explain every major change in a concise way.

Be sure to include details of major changes

You don't need to add any punctuation or capitalization.

Instead of and, use a comma to save characters.
Only respond with a short sentence no longer than 50 characters that I can use for my commit message
    '''

    ai_gen_commit_msg = OpenAiService(openai_key).chat_with_openai([
        {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
        {"role": "user", "content": staged_diff.stdout},
    ])

    return ai_gen_commit_msg.strip()

def main() -> int:
    script_directory = get_file_directory()
    log_path = script_directory + "/ai_commit_msg_logs.txt"
    write_to_logs("Starting AI commit message generation in:" + script_directory , log_path)

    commit_message = generate_commit_message("sk-proj-pPkf0GH5LzbVFno8Eyc1T3BlbkFJY628EJOBgGN6wNMN494j")

    print("✨AI: " + commit_message)

    return 0

if __name__ == '__main__':
    sys.exit(main())