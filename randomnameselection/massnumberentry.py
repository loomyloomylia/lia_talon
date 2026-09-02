from talon import Context, Module, actions

mod = Module()

mod.tag("mass_number_entry", desc="Modifies behavior of dictating numbers for the purpose of mass entry into the great book")

mod.setting(
    "mass_number_entry_delimiter",
    type=str,
    default="enter",
    desc="Key to hit after every entry number while tag is activated"
)

ctx = Context()
ctx.matches = """
mode: command
and not mode: sleep
"""
anchor = 1

DELAY = 0.1



@mod.action_class
class MassNumberEntryActions:
    def enable_mass_number_entry():
        """"""
        ctx.tags = ["user.mass_number_entry"]

    def disable_mass_number_entry():
        """"""
        ctx.tags = []

    def mass_number_entry_insert(number_list: str):
        """"""
        global anchor
        for number in number_list:
            actions.insert(number)
            actions.sleep(DELAY)
            actions.key("enter")
            actions.sleep(DELAY)
            anchor += 1
            

        # temp = "\n".join(number_list)
        # print(temp)
        # actions.insert(temp)
        # for number in number_list:
        #     actions.insert(f"{number}\n")

    def mass_number_entry_anchor(number: int):
        """"""
        global anchor
        anchor = number

    def mass_number_entry_down(steps: int):
        """"""
        global anchor
        for i in range(steps):
            actions.sleep(DELAY)
            actions.key("down")
            anchor += 1

    def mass_number_entry_up(steps: int):
        """"""
        global anchor
        for i in range(steps):
            actions.sleep(DELAY)
            actions.key("up")
            anchor -= 1

    def mass_number_entry_seek(location: int):
        """"""
        global anchor
        print(location, type(location))
        if location < anchor:
            actions.user.mass_number_entry_up(anchor - location)
        else:
            actions.user.mass_number_entry_down(location - anchor)
            
            
            
        
            
        
        

"""
131415161718
13
131415
"""