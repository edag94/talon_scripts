from talon import Context, Module, actions, imgui, registry

mod = Module()

@mod.action_class
class user_actions:
    def shortcat():
        """open shortcat"""
        actions.key("shift-cmd-space")