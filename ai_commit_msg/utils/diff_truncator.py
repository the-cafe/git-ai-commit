def truncate_diff(diff: str, max_lines: int = 500) -> str:
    lines = diff.split('\n')
    if len(lines) <= max_lines:
        return diff

    # Keeping the first 100
    truncated = lines[:100]

    truncated.append("... (diff truncated due to length) ...")

    # Keeping the last 400 lines
    truncated.extend(lines[-400:])

    return '\n'.join(truncated)
