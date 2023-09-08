import random

def mess_up_casing(my_string:str) -> str:
    """ Messes up the casing of a string completely """
    return "".join([l.upper() if (round(random.random()) == 1) else l.lower() for l in my_string])


