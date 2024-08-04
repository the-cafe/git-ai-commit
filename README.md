# AI Commit Message

Tl;DR - An pre-commit hook that generates the perfect commit message for you

TODO - Insert video of usage

## Getting Started

1. Install the [`pre-commit`](https://pre-commit.com/) git hooks framework

```bash
brew install pre-commit
pre-commit --version 
```

2. Create a `.pre-commit-config.yaml` files and add the following config

```yaml
repos:
  - repo: TODO - insert public github repo
    hooks:
    -   id: gen_ai_commit_message
```

3. Based on the config above, install al your git hooks

```bash
pre-commit install
```

4. Setup your openai key

```bash
gen_ai_commit_message_cli config --openai-key=<insert-your-key>
```

## CLI

TODO - add document on your CLI interface and options
