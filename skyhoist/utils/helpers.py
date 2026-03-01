import re

def clean_arn(arn):
    """
    Extracts the name from a long ARN.
    Example: 'arn:aws:iam::123456789012:user/admin' -> 'user/admin'
    """
    if not arn or not isinstance(arn, str):
        return "Unknown"
    match = re.search(r'[^:]+$', arn)
    return match.group(0) if match else arn

def format_finding_severity(severity):
    """Returns a color-coded string for the CLI."""
    if severity == "CRITICAL":
        return "[!]"
    return "[*]"