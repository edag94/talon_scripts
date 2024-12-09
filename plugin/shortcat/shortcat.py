from talon import Context, Module, actions, imgui, registry

mod = Module()


# @mod.action_class
# class user_actions:
#     def shortcat():
#         """open shortcat"""
#         actions.key("shift-cmd-space")


is_enabled = False


@mod.action_class
class Actions:
    def shortcat_toggle_sleep():
        """Toggles sleep"""

        global is_enabled

        if is_enabled:
            actions.speech.set_microphone("None")
            actions.speech.disable()
            is_enabled = False
        else:
            actions.speech.set_microphone("System Default")
            actions.speech.enable()
            is_enabled = True
    def shortcat():
        """open shortcat"""
        actions.key("shift-cmd-space")
