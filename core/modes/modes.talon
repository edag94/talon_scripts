not mode: sleep
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
    mode.disable("user.game")
^dict$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
    mode.disable("user.game")
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
    mode.disable("user.game")
^mand$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
    mode.disable("user.game")
^game mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.disable("dictation")
    mode.disable("user.gdb")
    mode.enable("user.game")
