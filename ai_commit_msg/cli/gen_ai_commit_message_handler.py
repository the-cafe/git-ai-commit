from ai_commit_msg.core.gen_commit_msg import generate_commit_message, generate_commit_with_auto_fallback
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.services.pip_service import PipService
from ai_commit_msg.utils.utils import execute_cli_command
from ai_commit_msg.utils.error import AIModelHandlerError
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.utils.git_utils import handle_git_push


def gen_ai_commit_message_handler():
    logger = Logger()

    PipService().display_outdated_version_message()

    if len(GitService.get_staged_files()) == 0:
        print(
            "🚨 No files are staged for commit. Run `git add` to stage some of your changes"
        )
        return

    staged_diff = GitService.get_staged_diff()

    # Check if user has a custom commit template configured
    config = ConfigService()
    commit_template = config.commit_template if config.commit_template else None

    try:
        # Use auto-fallback format selection by default
        # If custom template is configured, use the original generate_commit_message
        if commit_template:
            ai_gen_commit_msg = generate_commit_message(
                staged_diff.stdout,
                commit_template=commit_template,
            )
        else:
            ai_gen_commit_msg = generate_commit_with_auto_fallback(
                staged_diff.stdout
            )
    except AIModelHandlerError as e:
        logger.log(f"Error generating commit message: {e}")
        logger.log("Please enter your commit message manually:")
        ai_gen_commit_msg = input().strip()
        if not ai_gen_commit_msg:
            logger.log("No commit message provided. Exiting.")
            return

    command_string = f"""
git commit -m "{ai_gen_commit_msg}"
git push

Would you like to commit your changes? (y/n): """

    should_push_changes = input(command_string)

    if should_push_changes == "n":
        logger.log("👋 Goodbye!")
        return
    elif should_push_changes != "y":
        logger.log("🚨 Invalid input. Exiting.")
        return

    execute_cli_command(["git", "commit", "-m", ai_gen_commit_msg], output=True)

    handle_git_push()

    return 0
