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
column_anchor = 1

DELAY = 0.1
focused_columns = []

def number_too_big(number: int):
    return number > 50

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
        # if column_anchor != 1:
        #     actions.user.mass_number_entry_column_seek(1)
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
        global anchor, column_anchor
        if number_too_big(number):
            return 
        # if column_anchor != 1:
            # actions.user.mass_number_entry_column_seek(1)
        anchor = number
        column_anchor = 1

    def mass_number_entry_down(steps: int):
        """"""
        global anchor 
        if number_too_big(steps):
            return
        # if column_anchor != 1:
        #     actions.user.mass_number_entry_column_seek(1)
        for i in range(steps):
            actions.sleep(DELAY)
            actions.key("down")
            anchor += 1

    def mass_number_entry_up(steps: int):
        """"""
        global anchor
        if number_too_big(steps):
            return
        # if column_anchor != 1:
        #     actions.user.mass_number_entry_column_seek(1)
        for i in range(steps):
            actions.sleep(DELAY)
            actions.key("up")
            anchor -= 1

    def mass_number_entry_seek(location: int):
        """"""
        global anchor
        if number_too_big(location):
            return
        print(location, type(location))
        if location < anchor:
            actions.user.mass_number_entry_up(anchor - location)
        else:
            actions.user.mass_number_entry_down(location - anchor)

    def mass_number_entry_column_seek(digit: int):
        """"""
        global anchor,column_anchor
        if digit > 10:
            return 
            
        while column_anchor < digit:
            actions.sleep(DELAY)
            actions.key("tab")
            column_anchor += 1
        while column_anchor > digit:
            actions.sleep(DELAY)
            actions.key("shift-tab")
            column_anchor -= 1

    def mass_number_entry_column_focus(number_list: list):
        """"""
        global focused_columns
        print(number_list)
        focused_columns = number_list

    def mass_number_entry_fill(number_list: list):
        """"""
        global anchor 
        print(number_list)
        if len(number_list) != len(focused_columns):
            print("number of columns does not match")
            return 
        for i in range(len(number_list)):
            actions.user.mass_number_entry_column_seek(int(focused_columns[i]))
            actions.sleep(DELAY)
            actions.insert(number_list[i])
            actions.sleep(DELAY)
        actions.user.mass_number_entry_column_seek(int(focused_columns[i]))
        actions.sleep(DELAY)
        actions.key("enter")
        anchor += 1
            
        
            
            
            
        
            
        
        

"""
131415161718
13
131415
"""