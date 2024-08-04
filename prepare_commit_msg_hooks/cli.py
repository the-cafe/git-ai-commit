from __future__ import annotations

import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print(args)
    return 0

if __name__ == '__main__':
    sys.exit(main())