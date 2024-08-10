# Using local Ollama LLM model

## Setup

Download and install Ollama from [ollama.com](https://ollama.com/)

Install and run `llama3` using ollama. See full list of model at <https://ollama.com/library>

```bash
ollama run llama3
```

Set the following configuration for tool to use the local Ollama model.

- make sure you prefix the model with `ollama`
- default value for `ollama_url` is `http://localhost:11434/api/chat`

```bash
ai_git_commit config --model=ollama/...

ai_git_commit config --ollama_url=http://localhost:11434/api/chat
```
