from talon import Context,Module,actions
from ....community.lang.tags.operators import Operators

ctx = Context()
ctx.matches = """
app: obsidian
hostname: LiaBox2
"""

parrot_config = {
    "tut:th_150": ('press the pointer mode', lambda : actions.user.button("1"))
}
# operators = Operators(
#     MATH_SUBTRACT=" - ",
#         MATH_ADD=" + ",
#         MATH_MULTIPLY=" * ",
#         MATH_DIVIDE=" / ",
#         MATH_INTEGER_DIVIDE=" // ",
#         MATH_MODULO=" % ",
#         MATH_EXPONENT=" ** ",
#         MATH_EQUAL=" == ",
#         MATH_NOT_EQUAL=" != ",
#         MATH_GREATER_THAN=" > ",
#         MATH_GREATER_THAN_OR_EQUAL=" >= ",
#         MATH_LESS_THAN=" < ",
#         MATH_LESS_THAN_OR_EQUAL=" <= ",
# )


class ObsidianActions:
    def parrot_config():
        return parrot_config
    # def code_get_operators() -> Operators :
    #     return operators