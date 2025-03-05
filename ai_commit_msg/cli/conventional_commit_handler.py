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


def select_commit_type():
    Logger().log("Select a commit type:")

    # Display commit types with descriptions
    for i, (type_key, description) in enumerate(COMMIT_TYPES.items(), 1):
        Logger().log(f"{i}. {type_key}: {description}")

    # Add custom option
    Logger().log(f"{len(COMMIT_TYPES) + 1}. custom: Enter a custom type")

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
                Logger().log("Invalid choice. Please try again.")
        except ValueError:
            Logger().log("Please enter a valid number.")


def get_scope():
    scope = input("Enter scope (optional, press Enter to skip): ")
    return scope.strip()


def conventional_commit_handler(args):
    logger = Logger()

    # Get the diff
    if hasattr(args, "diff") and args.diff is not None:
        with open(args.diff, "r") as file:
            diff = file.read()
    elif hasattr(args, "unstaged") and args.unstaged:
        logger.log("Fetching your unstaged changes...\n")
        unstaged_changes_diff = execute_cli_command(["git", "diff"])
        diff = unstaged_changes_diff.stdout
    else:
        logger.log("Fetching your staged changes...\n")

        if len(GitService.get_staged_files()) == 0:
            logger.log(
                "🚨 No files are staged for commit. Run `git add` to stage some of your changes"
            )
            return

        staged_changes_diff = execute_cli_command(["git", "diff", "--staged"])
        diff = staged_changes_diff.stdout

    # Generate the commit message body
    try:
        ai_commit_msg = generate_commit_message(diff, conventional=True)
    except AIModelHandlerError as e:
        logger.log(f"Error generating commit message: {e}")
        logger.log("Please enter your commit message manually:")
        ai_commit_msg = input().strip()
        if not ai_commit_msg:
            logger.log("No commit message provided. Exiting.")
            return

    # Get commit type and scope
    commit_type = select_commit_type()
    scope = get_scope()

    # Format the conventional commit
    formatted_commit = print_conventional_commit(commit_type, scope, ai_commit_msg)

    # Ask if user wants to commit and push
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

    # Commit the changes
    execute_cli_command(["git", "commit", "-m", formatted_commit], output=True)

    # Handle git push with the shared utility function
    handle_git_push()

    return 0
