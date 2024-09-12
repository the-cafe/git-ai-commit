from ai_commit_msg.core.gen_commit_msg import llm_chat_completion


def help_ai_handler(args, help_menu):
    user_message = " ".join(args.message)

    if not user_message:
        print(
            "Let me know what you need help with \n\n git-ai-commit help-ai [message]"
        )
        return

    prompt = [
        {
            "role": "system",
            "content": f"""
Hey GPT, based on the follow documentation on the CLI's arguments

{help_menu}

what are set of arguments and options should i use if someone requests for help?

Please only respond with the exact commands that should be used and nothing else.
""",
        },
        {
            "role": "user",
            "content": user_message,
        },
    ]

    ai_gen_commit_msg = llm_chat_completion(prompt)

    print(ai_gen_commit_msg)

    return
