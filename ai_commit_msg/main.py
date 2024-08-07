from __future__ import annotations

from ai_commit_msg.prepare_commit_msg_hook import prepare_commit_msg_hook

def main() -> int:
    prepare_commit_msg_hook()

    return 0

if __name__ == '__main__':
    raise SystemExit(main())
