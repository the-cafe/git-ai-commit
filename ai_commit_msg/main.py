from __future__ import annotations
import argparse
import sys
import os
from typing import Sequence

from ai_commit_msg.cli.config_handler import config_handler
from ai_commit_msg.cli.gen_ai_commit_message_handler import gen_ai_commit_message_handler
from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.utils.logger import Logger

def called_from_git_hook():
    return os.environ.get('PRE_COMMIT') == '1'

def main(argv: Sequence[str] = sys.argv[1:]) -> int:
    if called_from_git_hook():
        return prepare_commit_msg_hook()

    if len(argv) == 0:
        return gen_ai_commit_message_handler()

    parser = argparse.ArgumentParser(description="CLI tool")
    subparsers = parser.add_subparsers(dest='command', required=False)

    # Config command
    config_parser = subparsers.add_parser('config', help='Configure the tool')
    config_parser.add_argument('-k', '--openai-key', dest='openai_key', help='Set OpenAI API key')
    config_parser.add_argument('-r', '--reset', action='store_true', help='Reset the OpenAI API key')
    config_parser.add_argument('-l', '--logger', type=lambda x: (str(x).lower() == 'true'), help='Enable or disable logging (true/false)')

    # Help command
    subparsers.add_parser('help', help='Display this help message')

    args = parser.parse_args(argv)

    if args.command == 'config':
        config_handler(args)
    elif args.command == 'help':
        parser.print_help()
    elif not args.command:
        prepare_commit_msg_hook()

    ## Only in main script, we return zero instead of None when the return value is unused
    return 0

if __name__ == '__main__':
    Logger().log("sys.argv: " + str(sys.argv))
    raise SystemExit(main(sys.argv[1:]))
