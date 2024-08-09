# Local Development

Install the `gen_ai_commit_message` pip library

```bash
pip install .
```

Update your pre-commit hooks

```bash
pre-commit install
```

Run the pre-commit hook locally

TODO - make this command more versatile and work on other peoples laptops

```bash
pre-commit try-repo /Users/seifmamdouh/ai-commit-msg git_ai_commit --verbose --all-files --hook-stage prepare-commit-msg --commit-msg-filename /Users/seifmamdouh/ai-commit-msg/.git/COMMIT_EDITMSG  
```

After a local change to the hook, the follow command will build and install it

```bash
pip install . && pre-commit install && pre-commit autoupdate
```

## Directory Structure

- `/cli` - contains logic for handling CLI command

- `/core` - contains LLM and prompting logic

- `/services` - contains logic that interacts with external dependencies

- `/utils` - standard utility functions
