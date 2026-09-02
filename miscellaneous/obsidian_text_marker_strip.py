from talon import Module, actions, Context
import re

mod = Module()

@mod.action_class
class Actions:
    def imo_fix_prose(s: str) -> str:
        """
        Mangles the input string in the appropriate manner."
        https://www.cursorless.org/docs/user/how-to/#how-do-i-run-a-custom-python-transformation-on-a-target
        """
        # replace multiple spaces with a single space
        s = re.sub(r" {2,}", " ", s)

        # remove leading spaces
        s = re.sub(
            pattern=r"^ +",
            repl="",
            string=s,
            flags=re.MULTILINE,
        )

        # Get rid of ellipses & fix capitalization after them
        def _fix_ellipsis(match: re.Match) -> str:
            text = match.group(0).lower().replace(".", "").strip()
            return " " + text

        s = re.sub(
            pattern=r"\s*\.{3}\s*[A-Z]*",
            repl=_fix_ellipsis,
            string=s,
        )
        return s