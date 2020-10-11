"""
Animation Count Module
----------------------
Terminal print output animation count.
"""

import time

def count_down(print_text, count, sleep):
    """
    Print text and animation count down.

    Args:
        print_text (str): Enter the text to be printed.
        count (int): Counter number.
        sleep (float): How fast the counts is supposed to be.
    Returns:
        print: Count down animation.
    Usage:

    .. code::
    
        count_down('Your text ', 20, 0.1)
    """

    animation = '\\|/-'
    while (count >= 0):
        print('\r', print_text, count, animation[count % len(animation)], end = ' ', flush = True)
        count -= 1
        time.sleep(sleep)

def count_up(print_text, count, sleep):
    """
    Print text and animation count up.

    Args:
        print_text (str): Enter the text to be printed.
        count (int): Counter number.
        sleep (float): How fast the counts is supposed to be.
    Returns:
        print: Count up animation.
    Usage:

    .. code::
    
        count_up('Your text ', 500, 0.001)
    """

    count_up = 0
    animation = '\\|/-'
    while (count >= count_up):
        print('\r', print_text, count_up, animation[count_up % len(animation)], end = ' ', flush = True)
        count_up += 1
        time.sleep(sleep)