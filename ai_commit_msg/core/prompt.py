COMMIT_MSG_SYSTEM_MESSAGE = '''
You will be provided with a set of code changes in diff format.
Your task is to read each file and explain every major change in a concise way.

Be sure to include details of major changes.

You don't need to add any punctuation or capitalization.

Instead of and, use a comma to save characters.

Only respond with a short sentence no longer than 50 characters that I can use for my commit message
'''

def get_prompt(diff):
  return [
    {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
    {"role": "user", "content": diff},
  ]
