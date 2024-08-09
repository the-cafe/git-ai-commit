
from ai_commit_msg.core.gen_commit_msg import generate_commit_message
from ai_commit_msg.utils.utils import execute_cli_command

def gen_ai_commit_message_handler():
    commit_message = "✨" + generate_commit_message()

    command_string = f"""
  git commit -m "✨{commit_message}"
  git push

  Would you like to commit your changes? (y/n): """

    should_push_changes = input(command_string)

    if(should_push_changes == 'n'):
      print("👋 Goodbye!")
      return
    elif should_push_changes != 'y':
      print("🚨 Invalid input. Exiting.")
      return

    execute_cli_command(['git', 'commit', '-m', "✨" + ai_gen_commit_msg])
    execute_cli_command(['git', 'push'])
