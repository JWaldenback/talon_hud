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
        current_microphone = actions.sound.active_microphone()
        if current_microphone == "None":
            #https://github.com/chaosparrot/talon_hud/blob/master/CUSTOMIZATION.md#log-messages
            actions.user.hud_add_log('success', 'Microphone enabled')
        else:
            actions.user.hud_add_log('error', 'Microphone disabled')
        
        actions.user.hud_toggle_microphone()