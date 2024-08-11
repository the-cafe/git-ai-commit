from __future__ import annotations
import argparse
import sys
import os
from typing import Sequence
import configparser

from ai_commit_msg.cli.config_handler import config_handler, handle_config_setup
from ai_commit_msg.cli.gen_ai_commit_message_handler import gen_ai_commit_message_handler
from ai_commit_msg.cli.hook_handler import hook_handler
from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook
from ai_commit_msg.services.config_service import ConfigService
from ai_commit_msg.utils.logger import Logger

def called_from_git_hook():
    return os.environ.get('PRE_COMMIT') == '1'

def get_version():
    config = configparser.ConfigParser()
    config.read('setup.cfg')
    return config['metadata']['version']

def main(argv: Sequence[str] = sys.argv[1:]) -> int:
    if called_from_git_hook():
        return prepare_commit_msg_hook()

    if len(argv) == 0:
        if(ConfigService().last_updated_at == ""):
            handle_config_setup()
            return 0

        return gen_ai_commit_message_handler()

    parser = argparse.ArgumentParser(description="🚀 AI-powered CLI tool that revolutionizes your Git workflow by automatically generating commit messages!")
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {get_version()}')
    subparsers = parser.add_subparsers(dest='command', required=False)

    # Config command
    config_parser = subparsers.add_parser('config', help='🛠️ Configure the tool settings')
    config_parser.add_argument('-k', '--openai-key', dest='openai_key',help='🔑 Set your OpenAI API key for AI-powered commit messages')
    config_parser.add_argument('-r', '--reset', action='store_true',help='🔄 Reset the OpenAI API key to default')
    config_parser.add_argument('-l', '--logger', type=lambda x: (str(x).lower() == 'true'),help='📝 Enable or disable logging (true/false) for debugging')
    config_parser.add_argument('-m', '--model',help= '🧠 Set the OpenAI model to use for generating commit messages')
    config_parser.add_argument('-ou', '--ollama-url', help='🌐 Set the Ollama URL for local LLM models')
    config_parser.add_argument('-a', '--anthropic-key', dest='anthropic_key', help='🔑 Set your Anthropic API key for AI-powered commit messages')
    config_parser.add_argument('-s', '--setup', action='store_true', help='🔧 Setup the tool')

    # Help command
    subparsers.add_parser('help', help='Display this help message')

    # Hook command
    hook_parser = subparsers.add_parser('hook', help='🪝 Run the prepare-commit-msg hook to generate commit messages')
    hook_parser.add_argument('--setup', action='store_true', help='Setup the prepare-commit-msg hook')
    hook_parser.add_argument('--remove', action='store_true', help='Remove the prepare-commit-msg hook')
    hook_parser.add_argument('--run', action='store_true', help='Run the prepare-commit-msg hook')
    args = parser.parse_args(argv)

    if args.command == 'config':
        config_handler(args)
    elif args.command == 'help':
        parser.print_help()
    elif args.command == 'hook':
        hook_handler(args)

    ## Only in main script, we return zero instead of None when the return value is unused
    return 0

if __name__ == '__main__':
    Logger().log("sys.argv: " + str(sys.argv))
    raise SystemExit(main())
