"""Some tools."""

import six


def to_bytes(s, encoding="utf-8"):
    """Convert a string to bytes."""
    if isinstance(s, six.binary_type):
        return s
    if six.PY3:
        return bytes(s, encoding)
    return s.encode(encoding)


def to_list(stringlist, unquote=True):
    """Convert a string representing a list to real list."""
    stringlist = stringlist[1:-1]
    return [
        string.strip('"') if unquote else string
        for string in stringlist.split(",")
    ]
