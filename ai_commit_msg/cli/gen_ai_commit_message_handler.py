from ai_commit_msg.core.gen_commit_msg import generate_commit_message
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.utils import execute_cli_command
from ai_commit_msg.services.model_error_handling import AIModelHandlerError

def gen_ai_commit_message_handler():
    if(len(GitService.get_staged_files()) == 0):
      print("🚨 No files are staged for commit. Run `git add` to stage some of your changes")
      return

    staged_diff = GitService.get_staged_diff()

    try:
        ai_gen_commit_msg = generate_commit_message(staged_diff.stdout)
    except AIModelHandlerError as e:
        print(f"Error generating commit message: {e}")
        print("Please enter your commit message manually:")
        ai_gen_commit_msg = input().strip()
        if not ai_gen_commit_msg:
            print("No commit message provided. Exiting.")
            return

    command_string = f"""
git commit -m "{ai_gen_commit_msg}"
git push

Would you like to commit your changes? (y/n): """

    should_push_changes = input(command_string)

    if(should_push_changes == 'n'):
      print("👋 Goodbye!")
      return
    elif should_push_changes != 'y':
      print("🚨 Invalid input. Exiting.")
      return

    execute_cli_command(['git', 'commit', '-m', ai_gen_commit_msg], output=True)
    current_branch = GitService.get_current_branch()
    has_upstream = GitService.has_upstream_branch(current_branch)

    if has_upstream:
        execute_cli_command(['git', 'push'], output=True)
        return

    set_upstream = input(f"No upstream branch found for '{current_branch}'. This will run: 'git push --set-upstream origin {current_branch}'. Set upstream? (y/n): ")
    if set_upstream.lower() == 'y':
        execute_cli_command(['git', 'push', '--set-upstream', 'origin', current_branch], output=True)
        print(f"🔄 Upstream branch set for '{current_branch}'")
    else:
        print("Skipping push. You can set upstream manually")

    return 0
