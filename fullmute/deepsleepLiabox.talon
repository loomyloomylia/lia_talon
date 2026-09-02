hostname: Liabox
and not tag: user.deep_sleep_enabled
-
^((you are|you're) getting very sleepy box one)|(box one box two switch)$:
    user.sleep_mode_color_preset()
    speech.disable()
    user.enable_deep_sleep()
    