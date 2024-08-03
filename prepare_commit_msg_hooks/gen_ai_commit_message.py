import os
import sys
import subprocess
from prepare_commit_msg_hooks.openai_service import OpenAiService

script_directory = os.path.dirname(os.path.abspath(__file__))

def execute_cli_command(cmd_string_list):
    try:
        result = subprocess.run(
            cmd_string_list,
            cwd=script_directory,
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
    # git diff --cached is used to get the staged changes to give to the AI to generate commit message
    return execute_cli_command(['git', 'diff', '--cached'])

def generate_commit_message():

    print("Generating commit message...")

    staged_diff = get_staged_diff()

    COMMIT_MSG_SYSTEM_MESSAGE = '''
    You will be provided with a set of code changes in diff format.
    Your task is to read each file and explain every major change in a concise way.
    Be sure to include details of major changes
    You don't need to add any punctuation or capitalization.
    Instead of and, use a comma to save characters.
    Only respond with a short sentence no longer than 50 characters that I can use for my commit message
  '''

    ai_gen_commit_msg = OpenAiService().chat_with_openai([
        {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
        {"role": "user", "content": staged_diff.stdout},
    ])

    return ai_gen_commit_msg.strip()



def main():
    commit_message = generate_commit_message()
    if commit_message:
        # Store the commit message in .git/COMMIT_EDITMSG
        commit_msg_path = os.path.join(script_directory, '.git', 'COMMIT_EDITMSG')
        try:
            with open(commit_msg_path, 'w') as f:
                f.write(commit_message + "\n\n")
        except IOError as e:
            print(f"[ERROR] Failed to write commit message: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        print("No commit message generated", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    raise SystemExit(main())