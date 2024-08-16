import os

from ai_commit_msg.services.git_service import GitConfigKeysEnum, GitService

class HuskyService:

  @staticmethod
  def repo_has_husky_framework():
    git_hook_path_config_value = GitService.get_git_config_value(GitConfigKeysEnum.hookPath.value)
    hook_path_is_husky = git_hook_path_config_value and '.husky' in git_hook_path_config_value
    husky_directory_exists = os.path.exists(GitService.get_repo_root_directory() + '/.husky/_')

    return hook_path_is_husky and husky_directory_exists

  @staticmethod
  def get_husky_prepare_commit_msg_hook_path():
    git_repo_path = GitService.get_repo_root_directory()
    return git_repo_path + '/.husky/prepare-commit-msg'