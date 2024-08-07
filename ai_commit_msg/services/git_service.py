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
