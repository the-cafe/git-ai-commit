from __future__ import annotations
import argparse
import sys
import os
from typing import Sequence
from ai_commit_msg.cli.config_handler import config_handler
from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.utils.logger import Logger

def main(argv: Sequence[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    # If no arguments are provided or if the first argument is a file path, run prepare_commit_msg_hook
    if not argv or (argv and os.path.exists(argv[0])):
        prepare_commit_msg_hook()
        return 0

    parser = argparse.ArgumentParser(description="CLI tool")
    subparsers = parser.add_subparsers(dest='command', required=False)

    # Config command
    config_parser = subparsers.add_parser('config', help='Configure the tool')
    config_parser.add_argument('-k', '--openai-key', dest='openai_key', help='Set OpenAI API key')
    config_parser.add_argument('-r', '--reset', action='store_true', help='Reset the OpenAI API key')
    config_parser.add_argument('-l', '--logger', type=lambda x: (str(x).lower() == 'true'), help='Enable or disable logging (true/false)')

    # Help command
    help_parser = subparsers.add_parser('help', help='Display this help message')

    args = parser.parse_args(argv)

    if args.command == 'config':
        config_handler(args)
    elif args.command == 'help':
        parser.print_help()
    elif not args.command:
        prepare_commit_msg_hook()

    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
