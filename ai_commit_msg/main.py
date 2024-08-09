from __future__ import annotations
import argparse
import sys
import os
from typing import Sequence
from ai_commit_msg.cli.config_handler import config_handler
from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.utils.logger import Logger

def custom_help():
    help_text = """    Available commands:
    config Configure the tool
        -k, --openai-key Set OpenAI API key
        -r, --reset Reset the OpenAI API key
        -l, --logger Enable or disable logging (true/false)
    help, -h Display this help message"""
    sys.exit(0)

def main(argv: Sequence[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    # If no arguments are provided or if the first argument is a file path, run prepare_commit_msg_hook
    if not argv or (argv and os.path.exists(argv[0])):
        prepare_commit_msg_hook()
        return 0

    # Check for help command before parsing arguments
    if '-h' in argv or 'help' in argv:
        custom_help()

    parser = argparse.ArgumentParser(description="CLI tool", add_help=False)
    subparsers = parser.add_subparsers(dest='command', required=False)

    # Config command
    config_parser = subparsers.add_parser('config', help='Configure the tool', add_help=True)
    config_parser.add_argument('-k', '--openai-key', dest='openai_key', help='Set OpenAI API key')
    config_parser.add_argument('-r', '--reset', action='store_true', help='Reset the OpenAI API key')
    config_parser.add_argument('-l', '--logger', type=lambda x: (str(x).lower() == 'true'), help='Enable or disable logging (true/false)')

    args = parser.parse_args(argv)

    if args.command == 'config':
        config_handler(args)
    elif not args.command:
        prepare_commit_msg_hook()

    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
