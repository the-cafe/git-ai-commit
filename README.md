# 🤖 `git-ai-commit`

<a href="https://pypi.org/project/git-ai-commit"><img src="https://img.shields.io/pypi/v/git-ai-commit" alt="Current version"></a>

> let AI write your commit messages

Tl;DR

- A CLI and git hook that generates the perfect commit message every time you run `git commit`

- Integrates with the [`pre-commit`](https://pre-commit.com/) framework, works alongside all your git hooks

- Supports all projects and programming languages

## 📺 Usage

![Usage Demo](assets/videos/ai-commit-msg.gif)

This tool currently supports the following LLM source...

- **Open AI**: `gpt-4o-mini`(default), `gpt-4`, `gpt-3.5`, and [more...](https://github.com/ming1in/ai-commit-msg/blob/a1e62be64c1f877bfa26c45d2d61508f94504ec0/ai_commit_msg/utils/models.py#L1)

- **Anthropic**: `claude-3-haiku`, `claude-3-sonnet`, `claude-3-opus`
  - [Wiki: Setup Anthropic Model](./wiki/anthropic.md)

- **Local Ollama**: `llama3`, `mistral`, `phi-3`, `gemma`, and [more..](https://github.com/ming1in/ai-commit-msg/blob/a1e62be64c1f877bfa26c45d2d61508f94504ec0/ai_commit_msg/utils/models.py#L1)
  - [Wiki: Using local Ollama LLM model](./wiki/ollama.md)

## 🚀 Let's Get Started

1. To install the AI Commit Message tool, run:

```bash
pip install git-ai-commit

git-ai-commit --version # Check the installed version 
```

2. Run the command to start configuring your tool:

```bash
git-ai-commit config --setup
```

### 🪝 Integrate with `pre-commit` framework

`git-ai-commit` integrated easily with your other git hook using the `pre-commit` framework.

1. Install the [`pre-commit`](https://pre-commit.com/) git hooks framework

```bash
brew install pre-commit
pre-commit --version 
```

2. Create a `.pre-commit-config.yaml` files and add the following config.

```bash
touch .pre-commit-config.yaml 
```

```yaml
default_install_hook_types: 
  # make sure you include `prepare-commit-msg` in `default_install_hook_types`
  - prepare-commit-msg
repos:
  - repo: https://github.com/ming1in/ai-commit-msg
    rev: v1.0.0
    hooks:
    -   id: git-ai-commit
```

3. Based on the config above, install your git hooks script

```bash
pre-commit install 
```

4. Setup your OpenAI key, [see their docs for help](https://platform.openai.com/docs/quickstart)

```bash
git-ai-commit config --openai-key=...
```

## 🛠️ CLI Commands & Options

✨ `git-ai-commit  config`

This command will display your current config settings. Config flags can be used to configure various settings in your configuration. For example...

```bash
git-ai-commit config

git-ai-commit config --openai-key=... --model=gpt-4o-mini
```
  
`-k` `--openai-key`

Set or update the OpenAI API key to access their GPT models

`-a` `--anthropic-key`

Set or update the Anthropic API key to access their Claude models

`-m` `--model`

*default:  "gpt-4o-mini"*

Select a model to power our tool from our supported provider. To use a [Ollama](./wiki/ollama.md) model, prefix `ollama/<model>`.

`-ou` `--ollama-url`

*default:  "[gpt-4o-mini](http://localhost:11434/api/chat)"*

Set the URL for interacting with your local Ollama models.

`-s` `--setup`

Config your git hook, model, and API keys via the NUX flow.

`-l` `--logger`

*default:  false*

A toggle for enabling logs that are saved to a local file - `.git/ai_commit_message.log`. This was intended to be used as a local debug tool.

`-r` `--reset`

Resets the entire config to its default state. This will reset all settings, including API keys and model.

`-p` `--prefix`

Set a prefix for generate commit messages.

---

📌 `git-ai-commit  help`, `-h`

Displays a list of available command and options to help you setup our tool.

```bash
git-ai-commit help # -h
```

---
🪝 `git-ai-commit hook`

```bash
git-ai-commit hook --setup
```

`-s` `--setup`

Adds a basic git hook by generating a `.git/hooks/prepare-commit-msg` script in your git repo

`-r` `--remove`

Removes the git hook.

`-x` `--run`

Executes the custom logic for the git hooks. This option was intended to only run from the `prepare-commit-msg` git hook.

## 🤝 Wanna Contribute?

If you would like to contribute code and improve our product, please read our
[Local Development Wiki](./wiki/local_development.md) to get started

## 🎉 Fun Facts

- In this repository, every commit prefixed with `✨` was generated by AI
