from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.utils import execute_cli_command
from ai_commit_msg.utils.logger import Logger


def handle_git_push():
    """
    Handle git push operation with upstream branch setting if needed.
    Returns True if push was successful, False otherwise.
    """
    logger = Logger()
    current_branch = GitService.get_current_branch()
    has_upstream = GitService.has_upstream_branch(current_branch)

    if has_upstream:
        execute_cli_command(["git", "push"], output=True)
        return True

    set_upstream = input(
        f"No upstream branch found for '{current_branch}'. This will run: 'git push --set-upstream origin {current_branch}'. Set upstream? (y/n): "
    )
    if set_upstream.lower() == "y":
        execute_cli_command(
            ["git", "push", "--set-upstream", "origin", current_branch], output=True
        )
        logger.log(f"🔄 Upstream branch set for '{current_branch}'")
        return True
    else:
        logger.log("Skipping push. You can set upstream manually")
        return False
