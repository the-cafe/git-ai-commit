from __future__ import annotations

import argparse
from typing import Sequence
from ai_commit_msg.cli.config_handler import config_handler
from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CLI tool")
    subparsers = parser.add_subparsers(dest='command', required=False)

    # Config command
    config_parser = subparsers.add_parser('config', help='Configure the tool')
    config_parser.add_argument('--openai-key', required=True, help='Open AI API key, this will only be stored locally')

    args = parser.parse_args(argv)

    if args.command == 'config':
        config_handler(args)
    else:
        prepare_commit_msg_hook()

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
