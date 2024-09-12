# Local Development

Install the `gen_ai_commit_message` pip library

```bash
pip install .
```

Use our prefix for AI generated commit message

```bash
git-ai-commit config --prefix=✨
```

Update your pre-commit hooks

```bash
pre-commit install
```

Run the pre-commit hook locally

TODO - make this command more versatile and work on other peoples laptops

```bash
pre-commit try-repo ./ai-commit-msg git-ai-commit --verbose --all-files --hook-stage prepare-commit-msg --commit-msg-filename ./ai-commit-msg/.git/COMMIT_EDITMSG  
```

After a local change to the hook, the follow command will build and install it

```bash
pip install . && pre-commit install && pre-commit autoupdate
```

## Linter

We use the python `black` linter, to lint run

```bash
black .
```

## Directory Structure

- `/cli` - contains logic for handling CLI command

- `/core` - contains LLM and prompting logic

- `/services` - contains logic that interacts with external dependencies

- `/utils` - standard utility functions
