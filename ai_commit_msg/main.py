from __future__ import annotations
import argparse
import sys
from typing import Sequence
from ai_commit_msg.cli.config_handler import config_handler
from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.utils.logger import Logger

SUPPORTED_COMMANDS = ['config', 'help']

def args_has_supported_command():
    sys_argv = sys.argv
    if len(sys_argv) < 2:
        return False
    command = sys_argv[1]
    return command in SUPPORTED_COMMANDS or command == '-h'

def display_help():
    help_text = f"""
    Available commands:
    config Configure the tool
        -k, --openai-key Set OpenAI API key
        -r, --reset Reset the OpenAI API key
        -l, --logger Enable or disable logging (true/false)
    help, -h Display this help message
"""
    print(help_text)

def main(argv: Sequence[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    # If no arguments are provided, run the prepare_commit_msg_hook
    if not argv:
        prepare_commit_msg_hook()
        return 0

    # If only '-h' is provided, display help
    if len(argv) == 1 and argv[0] == '-h':
        display_help()
        return 0

    if not args_has_supported_command():
        prepare_commit_msg_hook()
        return 0

    parser = argparse.ArgumentParser(description="CLI tool", add_help=True)
    subparsers = parser.add_subparsers(dest='command', required=False)

    # Config command
    config_parser = subparsers.add_parser('config', help='Configure the tool')
    config_parser.add_argument('-k', '--openai-key', dest='openai_key', help='Set OpenAI API key')
    config_parser.add_argument('-r', '--reset', action='store_true', help='Reset the OpenAI API key')
    config_parser.add_argument('-l', '--logger', type=lambda x: (str(x).lower() == 'true'), help='Enable or disable logging (true/false)')

    # Help command
    help_parser = subparsers.add_parser('help', aliases=['-h'], help='Display available commands')
    help_parser.set_defaults(command='help')

    args = parser.parse_args(argv)

    if args.command == 'help' or args.command == '-h':
        display_help()
    elif args.command == 'config':
        config_handler(args)

if __name__ == '__main__':
    raise SystemExit(main())
