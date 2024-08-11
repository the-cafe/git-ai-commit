from ai_commit_msg.utils.utils import execute_cli_command

class GitService:
  def __init__(self):
    return

  @staticmethod
  def get_staged_diff():
    return execute_cli_command(['git', 'diff', '--staged'],
                               cwd=GitService.get_repo_root_directory(), output=False)

  @staticmethod
  def get_repo_root_directory():
    git_directory = execute_cli_command(['git', 'rev-parse', '--show-toplevel']).stdout.rstrip()

    return git_directory

  @staticmethod
  def get_git_directory():
    script_directory = execute_cli_command(['git', 'rev-parse', '--git-dir']).stdout.rstrip()
    return script_directory

  @staticmethod
  def get_commit_editmsg_file_path():
    git_directory = GitService.get_repo_root_directory()
    commit_editmsg_file = git_directory + '/.git/COMMIT_EDITMSG'
    return commit_editmsg_file

  @staticmethod
  def read_commit_editmsg_file():
    existing_content = ""

    try:
      with open(GitService.get_commit_editmsg_file_path(), 'r') as file:
        existing_content = file.read()
    except FileNotFoundError:
      pass

    return existing_content

  @staticmethod
  def update_commit_message(commit_message):
    header = "This has been created by Ming, Seif & Ali\nLink to this project: https://github.com/the-cafe/git-ai-commit\n\n"
    existing_content = GitService.read_commit_editmsg_file()

    new_content = header + commit_message + '\n' + existing_content

    with open(GitService.get_commit_editmsg_file_path(), 'w') as file:
        file.write(new_content)

    return 0

  @staticmethod
  def get_staged_files():
    staged_files = execute_cli_command(['git', 'diff', '--name-only', '--cached']).stdout.splitlines()
    return staged_files

  @staticmethod
  def get_current_branch():
    return execute_cli_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).stdout.strip()

  @staticmethod
  def has_upstream_branch(branch_name):
    try:
        execute_cli_command(['git', 'rev-parse', '--abbrev-ref', f'{branch_name}@{{u}}'])
        return True
    except Exception:
        return False

  @staticmethod
  def is_git_installed():
    try:
        execute_cli_command(['git', '--version'])
        return True
    except Exception:
        return False

  @staticmethod
  def is_git_repository():
    try:
        execute_cli_command(['git', 'rev-parse', '--is-inside-work-tree'])
        return True
    except Exception:
        return False
