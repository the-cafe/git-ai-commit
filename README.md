# AI Commit Message

**Tl;DR**

- An pre-commit hook that generates the perfect commit message for you

- Supports all projects and programming language, built on the [`pre-commit`](https://pre-commit.com/) git hooks framework

- Works alongside all your other git hooks

## Usage

TODO - Insert video of usage

## Getting Started

1. Install the [`pre-commit`](https://pre-commit.com/) git hooks framework

```bash
brew install pre-commit
pre-commit --version 
```

2. Create a `.pre-commit-config.yaml` files and add the following config

🚨 Make sure you include `prepare-commit-msg` in `default_install_hook_types`🚨

```yaml
default_install_hook_types: 
  - prepare-commit-msg
repos:
  - repo: https://github.com/ming1in/ai-commit-msg
    rev: v0.0.1
    hooks:
    -   id: gen_ai_commit_message
```

3. Based on the config above, install your git hooks script

```bash
pre-commit install
```

4. Setup your OpenAI key, [see their docs for help](https://platform.openai.com/docs/quickstart)

```bash
gen_ai_commit_message_cli config --openai-key=<insert-your-key>
```

## CLI

- **add-config**: ✨
  This command allows you to set a new OpenAI API key for the CLI to use. Replace `<your-new-key>` with your actual API key to enable the functionality.

  ```bash
  gen_ai_commit_message_cli add-config --openai-key=<your-new-key>
  ```

- **delete-config**: ❌
  Use this command to remove the current OpenAI API key from the configuration.

  ```bash
  gen_ai_commit_message_cli delete-config
  ```

- **update-config**: 🔄
  This command updates the existing OpenAI API key. Make sure to provide the new key to ensure continued access to the API.

  ```bash
  gen_ai_commit_message_cli update-config --openai-key=<your-updated-key>
  ```

- **help**: 📚
  This command displays a list of all available commands and their usage, helping users understand how to interact with the CLI.

  ```bash
  gen_ai_commit_message_cli help
  ```

- **update**: ⬆️
  This command checks for the latest version of the package and updates it if a newer version is available.
  ```bash
  gen_ai_commit_message_cli update
  ```

- **Info**: 📚
  This command displays information about the package.

  ```bash
  gen_ai_commit_message_cli info
  ```

- **uninstall**: 🗑️
  This command removes the package from your system 😢.

  ```bash
  gen_ai_commit_message_cli uninstall
  ```

## Fun Facts

- Every commit prefixed with `✨` was generated by AI
