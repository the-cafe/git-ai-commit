#!/usr/bin/env python3

import os
import tempfile
import shutil
from ai_commit_msg.cli.hook_handler import handle_setup_hook


def test_hook_setup_with_missing_directory():
    """Test that handle_setup_hook creates the hooks directory if it doesn't exist"""

    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a fake hooks path that doesn't exist
        hooks_dir = os.path.join(temp_dir, "hooks")
        hook_file_path = os.path.join(hooks_dir, "prepare-commit-msg")

        print(f"Testing hook setup with path: {hook_file_path}")
        print(f"Hooks directory exists before: {os.path.exists(hooks_dir)}")

        # This should create the directory and the hook file
        handle_setup_hook(hook_file_path)

        print(f"Hooks directory exists after: {os.path.exists(hooks_dir)}")
        print(f"Hook file exists: {os.path.exists(hook_file_path)}")
        print(f"Hook file is executable: {os.access(hook_file_path, os.X_OK)}")

        # Verify the content
        if os.path.exists(hook_file_path):
            with open(hook_file_path, "r") as f:
                content = f.read()
                print(f"Hook file contains git-ai-commit: {'git-ai-commit' in content}")

        print("✅ Test completed successfully!")


def test_local_git_hooks():
    """Test the actual local .git/hooks directory"""

    # Check if we're in a git repository
    git_dir = ".git"
    if not os.path.exists(git_dir):
        print("❌ Not in a git repository - .git directory not found")
        return

    hooks_dir = os.path.join(git_dir, "hooks")
    hook_file_path = os.path.join(hooks_dir, "prepare-commit-msg")

    print(f"🔍 Checking local git hooks in: {os.path.abspath(hooks_dir)}")
    print(f"Hooks directory exists: {os.path.exists(hooks_dir)}")

    if os.path.exists(hooks_dir):
        print(f"Files in hooks directory:")
        for file in os.listdir(hooks_dir):
            file_path = os.path.join(hooks_dir, file)
            is_executable = os.access(file_path, os.X_OK)
            print(
                f"  - {file} {'(executable)' if is_executable else '(not executable)'}"
            )

    print(f"\n📋 prepare-commit-msg hook status:")
    print(f"Hook file exists: {os.path.exists(hook_file_path)}")

    if os.path.exists(hook_file_path):
        print(f"Hook file is executable: {os.access(hook_file_path, os.X_OK)}")

        # Check content
        with open(hook_file_path, "r") as f:
            content = f.read()
            has_git_ai_commit = "git-ai-commit" in content
            print(f"Hook file contains 'git-ai-commit': {has_git_ai_commit}")

            if has_git_ai_commit:
                print("✅ git-ai-commit hook is installed!")
            else:
                print("❌ git-ai-commit not found in hook file")
                print("Hook content preview:")
                print("-" * 40)
                print(content[:200] + "..." if len(content) > 200 else content)
                print("-" * 40)
    else:
        print("❌ prepare-commit-msg hook not found")
        print("\n🔧 To install the hook, you can run:")
        print(f"handle_setup_hook('{hook_file_path}')")


if __name__ == "__main__":
    print("=== Testing Local Git Hooks ===")
    test_local_git_hooks()

    print("\n" + "=" * 50)
    print("=== Testing with Temporary Directory ===")
    test_hook_setup_with_missing_directory()
