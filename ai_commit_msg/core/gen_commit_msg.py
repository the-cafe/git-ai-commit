
from ai_commit_msg.services.git_service import GitService
from ai_commit_msg.services.openai_service import OpenAiService
from ai_commit_msg.utils.utils import execute_cli_command

def generate_commit_message():
  staged_diff = GitService.get_staged_diff()

  COMMIT_MSG_SYSTEM_MESSAGE = '''
You will be provided with a set of code changes in diff format.
Your task is to read each file and explain every major change in a concise way.

Be sure to include details of major changes

You don't need to add any punctuation or capitalization.

Instead of and, use a comma to save characters.
Only respond with a short sentence no longer than 50 characters that I can use for my commit message
    '''

  ai_gen_commit_msg = OpenAiService().chat_with_openai([
        {"role": "system", "content": COMMIT_MSG_SYSTEM_MESSAGE},
        {"role": "user", "content": staged_diff.stdout},
    ])


  return ai_gen_commit_msg.strip()
