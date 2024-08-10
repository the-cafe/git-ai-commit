# Setup Anthropic Models

Sign up and obtain an Anthropic API key from [anthropic.com](https://console.anthropic.com/settings/keys)

Locally store your new API key by running the following commands

```bash
git_ai_commit config --anthropic_api_key=<INSERT-API-KEY>
```

Switch the default model to an Anthropic model. See the [full list of model here](https://docs.anthropic.com/en/docs/about-claude/models)

```bash
git_ai_commit config --model=claude-3-sonnet-20240229 
```
