# AI Commit Message

Install the `gen_ai_commit_message` pip library

```bash
pip install .
```

Update your pre-commit hooks

```bash
pre-commit install
```

Run the pre-commit hook locally

```bash
pre-commit try-repo /Users/seifmamdouh/ai-commit-msg gen_ai_commit_message --verbose --all-files --hook-stage prepare-commit-msg --commit-msg-filename /Users/seifmamdouh/ai-commit-msg/.git/COMMIT_EDITMSG  
```
