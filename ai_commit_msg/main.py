from __future__ import annotations

import argparse
import sys
from typing import Sequence
import os
from ai_commit_msg.cli.config_handler import config_handler
from ai_commit_msg.cli.gen_ai_commit_message_handler import gen_ai_commit_message_handler
from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.utils.logger import Logger

SUPPORTED_COMMANDS = ['config']

def args_has_supported_command():
    sys_argv = sys.argv

    if len(sys_argv) < 2:
        return False

    command = sys_argv[1]
    return command in SUPPORTED_COMMANDS

def is_cli():
    return os.environ.get('PRE_COMMIT') == '1'

def main(argv: Sequence[str] | None = None) -> int:
    if is_cli():
        prepare_commit_msg_hook()
        return 0

    if not args_has_supported_command():
        gen_ai_commit_message_handler()
        return 0

    parser = argparse.ArgumentParser(description="CLI tool")
    subparsers = parser.add_subparsers(dest='command', required=False)

    # Config command
    config_parser = subparsers.add_parser('config', help='Configure the tool')
    config_parser.add_argument('--openai-key', required=True, help='Open AI API key, this will only be stored locally')

    args = parser.parse_args(argv)

    if args.command == 'config':
        config_handler(args)

    return 0

if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
