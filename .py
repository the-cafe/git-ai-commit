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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
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
      warning_message = GitService.get_warning_banner(e)
      GitService.update_commit_message(warning_message)
  except Exception as e:
      warning_message = GitService.get_unexpected_error_banner(e)
      GitService.update_commit_message(warning_message)

  return
