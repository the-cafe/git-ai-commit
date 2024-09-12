from ai_commit_msg.services.openai_service import OpenAiService


def help_ai_handler(args, help_menu):
    user_message = " ".join(args.message)

    prompt = [
        {
            "role": "system",
            "content": f"""
Hey GPT, based on the follow documentation on the CLI's arugments

{help_menu}

what are set of arguments and options should i use if someone requests for help?

Please only respond with the exact command that should be used and nothing else.

If you are unable to find a command from the list of CLI arguments, just exactly say

```
Sorry, I can't find a command for that...

run `git-ai-commit help` to see the full list of commands
```
""",
        },
        {
            "role": "user",
            "content": user_message,
        },
    ]

    ai_gen_commit_msg = OpenAiService().chat_with_openai(prompt)

    print(ai_gen_commit_msg)
