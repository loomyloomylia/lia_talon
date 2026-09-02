app: vscode
-

# extends user/community/apps/vscode/vscode.talon

strip markers <user.cursorless_target>:
    old = user.cursorless_get_text(cursorless_target, true)
    new = user.imo_fix_prose(old)
    destination = user.cursorless_create_destination(cursorless_target)
    user.cursorless_insert(destination, new)