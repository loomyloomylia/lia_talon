from talon import Module,Context,actions,cron

ctx = Context()
ctx.matches = """
mode: user.game
user.active_manual_game: tabletopsimulator
not hostname: LiaBox2
"""

parrot_config = {
    "palate_click:th_150": ('left click', lambda: actions.user.mouse_button(0, 16000)),
    "tut:th_150": ('right click', lambda: actions.user.mouse_button(1, 16000)),
    "clock:th_150": ('quick action', lambda: actions.core.repeat_phrase(1)),
    "alveolar_click:th_150": ('drag toggle', lambda : actions.user.mouse_drag_toggle(0)),
    "high_whistle:th_500": ('ping', lambda : actions.user.button("tab")),
    # "hiss:db_120": ('tap', lambda: actions.user.button('e')),
    # "shush:db_120": ('untap', lambda: actions.user.button('q')),
    
}
#a
cron_job = None

@ctx.action_class("user")
class TabletopOverrides:
    def foot_switch_top_down():
        """Foot switch button top:down"""
        actions.user.game_speech_toggle()
        
    def foot_switch_top_up(held: bool):
        """Foot switch button top:up"""
        # actions.user.mouse_button_up(2)

    def foot_switch_center_down():
        """Foot switch button center:down"""
        actions.user.mouse_drag(0)

    def foot_switch_center_up(held: bool):
        """Foot switch button center:up"""
        actions.user.mouse_drag_end()

    def foot_switch_left_down():
        """Foot switch button left:down"""
        actions.tracking.control_gaze_toggle(False)

    def foot_switch_left_up(held: bool):
        """Foot switch button left:up"""
        actions.tracking.control_gaze_toggle(True)

    def foot_switch_right_down():
        """Foot switch button right:down"""
        actions.user.button_down("alt")

    def foot_switch_right_up(held: bool):
        """Foot switch button right:up"""
        actions.user.button_up("alt")

    def parrot_config():
        """Returns the current parrot config"""
        return parrot_config

joystick_state = False

mod = Module()
@mod.action_class
class TabletopActions:
    def do_the_thing():
        """"""
        for i in range(20):
            actions.user.button("e")
            actions.sleep(0.2)
    
    def tabletop_joystick_pan(x: float,y: float):
        """"""
        global cron_job
        if not joystick_state:
            if x > 0.3:
                actions.user.button_down("d")
            else:
                actions.user.button_up("d")
                
            if x < -0.3:
                actions.user.button_down("a")
            else:
                actions.user.button_up("a")
                
            if y < -0.3:
                actions.user.button_down("s")
            else:
                actions.user.button_up("s")
                
            if y > 0.3:
                actions.user.button_down("w")
            else:
                actions.user.button_up("w")
        else:
            if y > 0.3:
                if cron_job is None:
                    cron_job = cron.interval("100ms", mouse_scroll_up)
            elif y < -0.3:
                if cron_job is None:
                    cron_job = cron.interval("100ms", mouse_scroll_down)
            else:
                if cron_job is not None:
                    cron.cancel(cron_job)
                    cron_job = None
                
            if x > 0.3:
                actions.user.button_down("right")
            else:
                actions.user.button_up("right")
                
            if x < -0.3:
                actions.user.button_down("left")
            else:
                actions.user.button_up("left")
            
    def tabletop_joystick_click():
        """"""
        global joystick_state
        joystick_state = not joystick_state

ctx2 = Context()
ctx2.matches = """
mode: user.game
and mode: sleep
user.active_manual_game: tabletopsimulator
hostname: LiaBox2
"""

@ctx2.action_class("user")
class LiaBoxToOnlyActions:
    def parrot_config():
        """"""
        return parrot_config
        
    

def mouse_scroll_up():
    actions.user.mouse_scroll_up()

def mouse_scroll_down():
    actions.user.mouse_scroll_down()