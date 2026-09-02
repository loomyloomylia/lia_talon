mode: command
and not mode: sleep
tag: user.mass_number_entry
-
# tag(): user.unprefixed_numbers

{user.number_small}+:
    user.mass_number_entry_insert(number_small_list)

    # 12345 235423 235423enter23enter23enter23enter23enter23enter23enter23enter2opattern3enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter23enter
anchor <number>:
    user.mass_number_entry_anchor(number)

down <number>:
    user.mass_number_entry_down(number)
up <number>:
    user.mass_number_entry_up(number)

seek <number>:
    user.mass_number_entry_seek(number)

<user.ordinals>: 
    skip()

eighteen:
    skip()