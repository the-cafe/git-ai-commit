from __future__ import annotations

import argparse
from typing import Sequence
from prepare_commit_msg_hooks.openai_service import OpenAiService

def handle_config(args):
    OpenAiService.set_openai_api_key(args.openai_key)

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CLI tool")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Config command
    config_parser = subparsers.add_parser('config', help='Configure the tool')
    config_parser.add_argument('--openai-key', required=True, help='Open AI API key, this will only be stored locally')

    args = parser.parse_args(argv)

    if args.command == 'config':
        handle_config(args)

    return 0

if __name__ == '__main__':
    raise SystemExit(main())