# https://github.com/dwighthouse/unofficial-talonvoice-docs/blob/master/docs/KeysList.md
# https://talon.wiki/key_action/

key(scroll_lock:down): 
    user.hud_toggle_microphone()
    #https://github.com/chaosparrot/talon_hud/blob/master/CUSTOMIZATION.md#log-messages
    user.hud_add_log('success', 'Microphone activated/deactivated')
    #user.engine_mimic("Microphone activated/deactivated")
    #speech_system.engine_mimic("Microphone activated/deactivated")