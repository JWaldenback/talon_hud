from talon import Module, actions, Context

mod = Module()

@mod.action_class
class Actions:
    def poll_microphone():
        """sdf"""


ctx=Context()

@ctx.action_class("user")
class UserActions:
    def poll_microphone():
        """sdf"""