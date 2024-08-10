from datetime import datetime, timedelta, timezone

from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.services.git_service import GitService

def get_current_time():
  EST = timezone(timedelta(hours=-5))  # Adjusted to UTC-5 for Eastern Standard Time
  now_utc = datetime.now(timezone.utc)  # Get the current time in UTC
  now_est = now_utc.astimezone(EST)  # Convert UTC to Eastern Standard Time

  # Format the datetime object to exclude milliseconds
  current_time = now_est.strftime('%Y-%m-%dT%H:%M:%S%z')  # ISO 8601 format without milliseconds

  return str(current_time)

class Logger:
  def __init__(self):
    repo_git_directory = GitService.get_git_directory()
    self.log_file = repo_git_directory + "/ai_commit_message.log"

  def log(self, message):
    print(message)

    # Check if the logger is enabled
    if not self.is_enabled():
      return

    new_line = "" if message.endswith('\n') else "\n"
    log_line = self.get_prefix() + message + new_line

    with open(self.log_file, 'a') as file:
      file.write(log_line)

  def get_prefix(self):
    logged_string = "[" + get_current_time() + "] "
    return logged_string

  def is_enabled(self):
    return ConfigService().logger_enabled
