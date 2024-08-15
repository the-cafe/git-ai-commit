from ai_commit_msg.core.gen_commit_msg import generate_commit_message
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.logger import Logger
from ai_commit_msg.services.model_error_handling import AIModelHandlerError

def prepare_commit_msg_hook():

  existing_content = GitService.read_commit_editmsg_file()

  filtered_content = "\n".join([line for line in existing_content.splitlines() if not line.strip().startswith('#')])

  if(filtered_content != ""):
    Logger().log("Commit message already exists, skipping AI commit message generation")
    return

  staged_diff = GitService.get_staged_diff()

  try:
      commit_message = generate_commit_message(staged_diff.stdout)
      GitService.update_commit_message(commit_message)
  except AIModelHandlerError as e:
      error_message = f"Error in AI commit message generation: {e}\n"
      if e.error_type == "EXCEEDED_TOKEN_SIZE":
          error_message += "The input is too long. Please write your commit message manually.\n"
      elif e.error_type == "RATE_LIMIT_ERROR":
          error_message += "You've hit the rate limit. Please write your commit message manually.\n"
      else:
          error_message += "An unexpected error occurred. Please write your commit message manually.\n"

      GitService.update_commit_message(error_message)
  except Exception as e:
      error_message = f"Unexpected error in AI commit message generation: {str(e)}\n"
      error_message += "Please write your commit message manually.\n"
      GitService.update_commit_message(error_message)

  return
