from talon import Module,Context,actions,cron
import random
from copy import deepcopy
from pathlib import Path
from typing import Callable
from datetime import datetime 
mod = Module()

mod.tag("random_name_selection_active", "Whether or not my random name selection system is turned on and listening")

script_path = Path(__file__).resolve()

script_directory = script_path.parent

filename = "im2period.txt"
filepath = script_directory/filename

file1 = open(filepath, "r")
name_list = [line.strip() for line in file1.readlines()]
file1.close()

unused_names = deepcopy(name_list)
used_names = []

print(name_list)

ctx = Context()
ctx.matches = """
mode: command
mode: sleep
hostname: LiaBox2
"""

ui_active_context = Context()
ui_active_context.matches = """
mode:command
mode:sleep
and not mode: user.game
hostname: LiaBox2
tag: user.random_name_selection_active
"""
#and not tag: user.deep_sleep_enabled
# (command OR [sleep and not game]) and LiaBox2 and tag1 and not tag2

def mode_switch_wrapper(action: Callable, mode: str):
    global parrot_config
    action()
    # parrot_config = mode
    actions.user.parrot_config_set_mode(mode)

FONT_SIZE = 30
SIZE_ONE = 150
SIZE_TWO = 300

def random_name_overlay():
    div, text, screen, button = actions.user.ui_elements(["div", "text", "screen", "button"])

    def name_row(number: str):
        return div(flex_direction = "row", id = f"{number}_row", margin_bottom = 0, margin_right = 0)[
            div(flex_direction = "row", background_color="#444444", padding = 16, border_width = 1 )[
                text(f"{number.capitalize()}", id = f"{number}_prefix", width=SIZE_ONE, font_size = FONT_SIZE)
            ],
            div(id = "command_name", flex_direction = "row", background_color="#444444", padding = 16, border_width = 1)[
                text("", width=SIZE_TWO, id = f"{number}_name", font_size = FONT_SIZE)
            ]
        ]

    return screen(justify_content = "flex_end", align_items = "flex_end", screen = 0)[
        # div(flex_direction = "row", margin_bottom = 0, margin_left = 0, background_color="#444444", width = 400)[ 
        #     button("Submit", on_click=populate_ui, border_radius=8, padding=12, padding_left=24, padding_right=24)
        # ],
        
        div(id = "all_elements")[
            name_row("next"),
            name_row("second"),
            name_row("third"),
            div(flex_direction = "row", id = f"fourth_row", background_color = "#444444",align_items = "flex_end",  margin_bottom = 0, margin_right = 0, padding = 16, border_width = 1)[
                # div(flex_direction = "row", background_color="#444444", padding = 16, border_width = 1 )[
                #     text(f"", id ="", width=SIZE_ONE, font_size = FONT_SIZE)
                # ],
                text(f"", id = "time_text", width= SIZE_ONE, font_size = FONT_SIZE )
                # div(id = "command_name", flex_direction = "column", background_color="#444444", padding = 16, border_width = 1, align_items = "flex_end")[
                #     text(f"", id = "time_text", width= SIZE_ONE, font_size = FONT_SIZE )
                # ]
                # text("", width=SIZE_TWO, id = f"", font_size = FONT_SIZE)
            ],
        ]
    ]

queue = []

def populate_ui():
    ref = actions.user.ui_elements(["ref"])
    next_ref = ref("next_name")
    second_ref = ref("second_name")
    third_ref = ref("third_name")

    # next_ref.text = second_ref.text
    # second_ref.text = third_ref.text
    # third_ref.text = new_name
    change_flag = False
    
    if len(queue) > 2:
        third_ref.text = queue[2]
        if not change_flag:
            change_flag = True
            actions.user.ui_elements_highlight_briefly("third_row", "#338833")
            
    if len(queue) > 1:
        second_ref.text = queue[1]
        if not change_flag:
            change_flag = True
            actions.user.ui_elements_highlight_briefly("second_row", "#338833")
    if len(queue) > 0:
        next_ref.text = queue[0]
        if not change_flag:
            change_flag = True
            actions.user.ui_elements_highlight_briefly("next_row", "#338833")

    
cron_job = None       
        

def queue_random_name():
    global unused_names,used_names
    new_name = unused_names.pop(random.randrange(0, len(unused_names)))
    used_names.append(new_name)

    queue.append(new_name)
    if len(queue)  > 3 :
        queue.pop(0)
        

    if len(unused_names) == 0:
        assert len(used_names) == len(name_list), "Don't know what the hell's going on"
        unused_names = used_names
        used_names = []
    
    populate_ui()

def clear_recent_name_and_queue():
    global unused_names,used_names
    if len(queue) == 0:
        return 
    queue.pop(len(queue) - 1)
    queue_random_name()

def dequeue_in_disgrace():
    # index = len(queue) - 1
    actions.user.ui_elements_highlight_briefly("next_row", "#883333")
    actions.sleep(0.5)
    queue_random_name()


def enter_ready_state():
    actions.user.parrot_config_set_mode("ready")
    actions.user.ui_elements_highlight("all_elements")

def enter_waiting_state():
    actions.user.parrot_config_set_mode("waiting")
    actions.user.ui_elements_unhighlight("all_elements")
    
def pair_return_generator(func: Callable, func2: Callable):
    def call_pair(func: Callable, func2: Callable):
        func()
        func2()
        
    return lambda : call_pair(func, func2)
    
def time_update():
    now = datetime.now()
    time_text = now.strftime("%H:%M:%S")
    ref = actions.user.ui_elements(["ref"])
    time_ref = ref("time_text")
    time_ref.text = time_text

def wakeup():
    actions.speech.enable()
    actions.user.ui_elements_highlight_briefly("all_elements", "#338833")

def go_to_sleep():
    actions.speech.disable()
    actions.user.ui_elements_highlight_briefly("all_elements", "#883333")

def toggle_speech():
    if actions.speech.enabled():
        actions.user.ui_elements_highlight_briefly("all_elements", "#883333")
        actions.speech.disable()
    else:
        actions.speech.enable()
        actions.user.ui_elements_highlight_briefly("all_elements", "#338833")

    

"""random, name, overlay

"""
waiting_config = {
    "palate_click:th_150": ('and to ready state', enter_ready_state),
}

ready_config = {
    "palate_click:th_150": ('and to ready state', lambda : enter_waiting_state()),
    "clock:th_150": ('he new name', pair_return_generator(queue_random_name, enter_waiting_state)),
    "alveolar_click:th_150": ('he new name', pair_return_generator(dequeue_in_disgrace, enter_waiting_state)),
    # "tut:th_150": ('he new name', pair_return_generator(dequeue_in_disgrace, enter_waiting_state)),

}

always_on_config = {
    "clock:th_150": ('he new name', lambda : queue_random_name()),
    "palate_click:th_150": ('deco in disgrace', lambda : clear_recent_name_and_queue()),
    "tut:th_150": ('pointer mode', lambda : actions.user.button("1")),
    #"alveolar_click:th_150": ('toggle speech', lambda : toggle_speech()),
}

parrot_config = {
    "default": always_on_config,
    "ready": ready_config,
    "waiting": waiting_config
}

@ui_active_context.action_class("user")
class RandomNameActiveActions:
    def parrot_config():
        return parrot_config



@mod.action_class
class RandomNameActions:
    def reset_random_name_overlay():
        """"""
        global queue, name_list, unused_names, used_names
        actions.user.hide_random_name_overlay()
        queue = []
        unused_names = deepcopy(name_list)
        used_names = []
        

    def load_random_name_list():
        """"""
        global unused_names, used_names, name_list
        actions.skip()


    def show_random_name_overlay():
        """"""
        global cron_job
        actions.user.ui_elements_show(random_name_overlay)
        actions.user.load_random_name_list()
        ctx.tags = ["user.random_name_selection_active", "user.parrot_active"]
        if cron_job is None:
            cron_job = cron.interval(f"1000ms", time_update)


    def hide_random_name_overlay():
        """"""
        global cron_job
        actions.user.ui_elements_hide(random_name_overlay)
        ctx.tags = []
        if cron_job is not None:
            cron.cancel(cron_job)
            cron_job = None
            

    
