hostname: LiaBox2
and not tag: user.deep_sleep_enabled
-
^((you are|you're) getting very sleepy box two)|(box one box two switch)$:
    app.notify("I'm eeby")
    speech.disable()
    user.enable_deep_sleep()
    