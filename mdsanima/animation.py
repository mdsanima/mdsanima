'''
Animation Count Module
----------------------
This is a Simple Print Animation Count.
'''

import time

def count_down(print_text, count, sleep):
    '''
    Print text and animation countdown.

    Parameter:
        ``print_text`` `str`: Print text.
        ``count`` `int`: Number which to count.
        ``sleep`` `float`: How fast the countdown is supposed to be.
    '''
    animation = '\\|/-'
    while (count >= 0):
        print('\r', print_text, count, animation[count % len(animation)], end = ' ', flush = True)
        count -= 1
        time.sleep(sleep)

def count_up(print_text, count, sleep):
    '''
    Print text and animation count up.

    Parameter:
        ``print_text`` `str`: tu spisujemy co ma wyswietlic print.
        ``count`` `int`: tu wpisujemy ilosc followers, friend, tweet.
        ``sleep`` `float`: How fast the count up is supposed to be.
    '''
    count_up = 0
    animation = '\\|/-'
    while (count >= count_up):
        print('\r', print_text, count_up, animation[count_up % len(animation)], end = ' ', flush = True)
        count_up += 1
        time.sleep(sleep)