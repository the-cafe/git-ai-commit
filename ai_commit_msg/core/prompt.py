from ai_commit_msg.services.config_service import ConfigService

def get_prompt(diff):
  max_length = ConfigService().max_length

  COMMIT_MSG_SYSTEM_MESSAGE = f'''
Your a software engineer and you are reviewing a set of code changes.
You will be provided with a set of code changes in diff format.

Your task is to write a concise commit message that summarizes the changes. Only include major code in the commit message. Avoid including details about minor changes.

These are your requirements for the commit message:
- You don't need to add any punctuation or capitalization.
- Instead of and, use a comma to save characters.
- Your response cannot more than {max_length} characters.
'''

  return [
    {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
    {"role": "user", "content": diff},
  ]
