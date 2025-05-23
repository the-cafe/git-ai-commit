import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.utils.utils import execute_cli_command

console = Console()


def check_git_hooks_directory():
    """Check if we can determine the correct git hooks directory"""
    try:
        # Get the hooks directory using git's built-in command
        hooks_dir = execute_cli_command(
            ["git", "rev-parse", "--git-path", "hooks"]
        ).stdout.strip()
        git_dir = execute_cli_command(["git", "rev-parse", "--git-dir"]).stdout.strip()

        return {
            "status": "ok",
            "hooks_dir": hooks_dir,
            "git_dir": git_dir,
            "is_worktree": "worktrees" in git_dir,
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}
