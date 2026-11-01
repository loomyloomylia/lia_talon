app: endless_legend_2
mode: user.game
-
tag(): user.parrot_active
settings():
    user.mouse_wiggle = true
    user.game_dpad_mode = "arrows"
    user.mouse_hide_mouse_gui = true
    user.mouse_wheel_down_amount = 360
    user.mouse_continuous_scroll_amount = 36


#^quick action repeat$:
    #user.set_global_variable_str("foundry_quick_action", "repeat")


^test endless legend$:
    print("endless legend working")
