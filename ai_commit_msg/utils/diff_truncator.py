def truncate_diff(diff: str, max_lines: int = 500) -> str:
    lines = diff.split('\n')
    if len(lines) <= max_lines:
        return diff

    # Keep the first 100 lines
    truncated = lines[:100]

    # Add a message indicating truncation
    truncated.append("... (diff truncated due to length) ...")

    # Add the last 400 lines
    truncated.extend(lines[-400:])

    return '\n'.join(truncated)
