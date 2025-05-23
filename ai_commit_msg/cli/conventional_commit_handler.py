from ai_commit_msg.core.gen_commit_msg import generate_commit_message
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.utils.utils import execute_cli_command
from ai_commit_msg.utils.error import AIModelHandlerError
from ai_commit_msg.utils.git_utils import handle_git_push


COMMIT_TYPES = {
    "feat": "New feature",
    "fix": "Bug fix",
    "docs": "Documentation changes",
    "style": "Formatting changes",
    "refactor": "Code refactoring",
    "perf": "Performance improvements",
    "test": "Adding or modifying tests",
    "chore": "Maintenance tasks",
}


def print_conventional_commit(commit_type, scope, message):
    formatted_commit = f"{commit_type}"
    if scope:
        formatted_commit += f"({scope})"
    formatted_commit += f": {message}"

    Logger().log(
        f"""Here is your conventional commit message:

  {formatted_commit}

to use this commit message run: `git commit -m "{formatted_commit}"`
"""
    )
    return formatted_commit


def select_commit_type(suggested_type=None):
    logger = Logger()

    if suggested_type and suggested_type in COMMIT_TYPES:
        logger.log(
            f"AI suggests commit type: {suggested_type} ({COMMIT_TYPES[suggested_type]})"
        )
        use_suggested = (
            input(f"Use suggested type '{suggested_type}'? (Y/n): ").strip().lower()
        )
        if use_suggested == "" or use_suggested == "y":
            return suggested_type

    logger.log("Select a commit type:")

    # Display commit types with descriptions
    for i, (type_key, description) in enumerate(COMMIT_TYPES.items(), 1):
        # Highlight the suggested type if it exists
        highlight = "→ " if suggested_type == type_key else "  "
        logger.log(f"{highlight}{i}. {type_key}: {description}")

    # Add custom option
    logger.log(f"  {len(COMMIT_TYPES) + 1}. custom: Enter a custom type")

    while True:
        try:
            choice = input("Enter the number of your choice: ")
            choice_num = int(choice)

            if 1 <= choice_num <= len(COMMIT_TYPES):
                return list(COMMIT_TYPES.keys())[choice_num - 1]
            elif choice_num == len(COMMIT_TYPES) + 1:
                custom_type = input("Enter your custom commit type: ")
                return custom_type
            else:
                logger.log("Invalid choice. Please try again.")
        except ValueError:
            logger.log("Please enter a valid number.")


def get_scope(suggested_scope=None):
    logger = Logger()

    if suggested_scope and suggested_scope.strip() and suggested_scope != "none":
        logger.log(f"AI suggests scope: '{suggested_scope}'")
        use_suggested = (
            input(f"Use suggested scope '{suggested_scope}'? (Y/n): ").strip().lower()
        )
        if use_suggested == "" or use_suggested == "y":
            return suggested_scope

    scope = input("Enter scope (optional, press Enter to skip): ")
    return scope.strip()


def conventional_commit_handler(args):
    logger = Logger()

    logger.log("Fetching your staged changes...\n")

    if len(GitService.get_staged_files()) == 0:
        logger.log(
            "🚨 No files are staged for commit. Run `git add` to stage some of your changes"
        )
        return

    staged_changes_diff = execute_cli_command(["git", "diff", "--staged"])
    diff = staged_changes_diff.stdout

    try:
        logger.log("🤖 AI is analyzing your changes to suggest a commit type...\n")
        suggested_type = generate_commit_message(diff, classify_type=True)

        if suggested_type not in COMMIT_TYPES:
            logger.log(
                f"AI suggested an invalid type: '{suggested_type}'. Falling back to manual selection."
            )
            suggested_type = None
    except AIModelHandlerError as e:
        logger.log(f"Error classifying commit type: {e}")
        suggested_type = None

    suggested_scope = None
    try:
        logger.log("🤖 AI is analyzing your changes to suggest a scope...\n")
        suggested_scope = generate_commit_message(
            diff, conventional=False, classify_type=False, classify_scope=True
        )
        logger.log(f"Debug - AI suggested scope: '{suggested_scope}'")

        if suggested_scope == "none" or not suggested_scope:
            suggested_scope = None
    except AIModelHandlerError as e:
        logger.log(f"Error suggesting scope: {e}")
        suggested_scope = None

    try:
        ai_commit_msg = generate_commit_message(diff, conventional=True)
    except AIModelHandlerError as e:
        logger.log(f"Error generating commit message: {e}")
        logger.log("Please enter your commit message manually:")
        ai_commit_msg = input().strip()
        if not ai_commit_msg:
            logger.log("No commit message provided. Exiting.")
            return

    commit_type = select_commit_type(suggested_type)

    scope = get_scope(suggested_scope)

    formatted_commit = print_conventional_commit(commit_type, scope, ai_commit_msg)

    command_string = f"""
git commit -m "{formatted_commit}"
git push

Would you like to commit your changes? (y/n): """

    should_push_changes = input(command_string)

    if should_push_changes == "n":
        logger.log("👋 Goodbye!")
        return
    elif should_push_changes != "y":
        logger.log("🚨 Invalid input. Exiting.")
        return

    execute_cli_command(["git", "commit", "-m", f'"{formatted_commit}"'], output=True)

    handle_git_push()