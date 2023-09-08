import random

import pytest

from src.mikes_toolbox2.my_toolbox import mess_up_casing

def test_assert_casing():
    STR_IN = "this is a string"
    STR_OUT = mess_up_casing(my_string=STR_IN)

    assert len(STR_IN) == len(STR_OUT)          # Length has not changed
    assert STR_IN.lower() == STR_OUT.lower()    # letters have not changed except casing

