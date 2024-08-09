from ai_commit_msg.utils.utils import execute_cli_command

class GitService:
  def __init__(self):
    return

  @staticmethod
  def get_staged_diff():
    return execute_cli_command(['git', 'diff', '--staged'], GitService.get_repo_root_directory())

  @staticmethod
  def get_repo_root_directory():
    git_directory = execute_cli_command(['git', 'rev-parse', '--show-toplevel']).stdout.rstrip()

    return git_directory

  @staticmethod
  def get_git_directory():
    script_directory = execute_cli_command(['git', 'rev-parse', '--git-dir']).stdout.rstrip()
    return script_directory

  @staticmethod
  def update_commit_message(commit_message):
    git_directory = GitService.get_repo_root_directory()

    # open COMMIT_EDITMSG file to add the generated commit message
    commit_editmsg_file = git_directory + '/.git/COMMIT_EDITMSG'

    existing_content = ""

    try:
      with open(commit_editmsg_file, 'r') as file:
        existing_content = file.read()
    except FileNotFoundError:
      pass

    new_content = commit_message + '\n' + existing_content

    with open(commit_editmsg_file, 'w') as file:
      file.write(new_content)

    return 0

  @staticmethod
  def get_staged_files():
    staged_files = execute_cli_command(['git', 'diff', '--name-only', '--cached']).stdout.splitlines()
    return staged_files