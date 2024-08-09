from ai_commit_msg.core.gen_commit_msg import generate_commit_message
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.utils.logger import Logger

def prepare_commit_msg_hook():
  commit_message = "✨" + generate_commit_message()

  Logger().log("Generated commit message: " + commit_message)

  GitService.update_commit_message(commit_message)

  return
