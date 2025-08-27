import re

from mymodule import __version__


def test_version_format():
    SEMVER_REGEX = re.compile(
        r"""
        (0|[1-9]\d*) # Major
        \.
        (0|[1-9]\d*) # Minor
        \.
        (0|[1-9]\d*) # Revision
        """,
        re.VERBOSE,
    )

    assert SEMVER_REGEX.fullmatch(__version__)
