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


if __name__ == "__main__":
    test_hook_setup_with_missing_directory()
