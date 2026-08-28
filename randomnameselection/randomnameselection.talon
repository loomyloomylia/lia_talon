mode: command
hostname: LiaBox2
-
^show random name overlay$:
    user.show_random_name_overlay()

^hide random name overlay$:
    user.hide_random_name_overlay()

^refresh random name overlay$:
    user.hide_random_name_overlay()
    user.show_random_name_overlay()

^full reset random name overlay$:
    user.reset_random_name_overlay()