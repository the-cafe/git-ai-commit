from __future__ import annotations

import os

from datetime import datetime, timedelta, timezone

def get_current_time():
  EST = timezone(timedelta(hours=-5))  # Adjusted to UTC-5 for Eastern Standard Time
  now_utc = datetime.now(timezone.utc)  # Get the current time in UTC
  now_est = now_utc.astimezone(EST)  # Convert UTC to Eastern Standard Time

  # Format the datetime object to exclude milliseconds
  current_time = now_est.strftime('%Y-%m-%dT%H:%M:%S%z')  # ISO 8601 format without milliseconds

  return str(current_time)

def write_to_logs(message, log_path):
  new_line = "" if message.endswith('\n') else "\n"
  logged_string = "[" + get_current_time() + "] " + str(message) + new_line
  print(logged_string)

  open_mode = "a" if os.path.exists(log_path) else "w"

  with open(log_path, open_mode) as file:
    file.write(logged_string)