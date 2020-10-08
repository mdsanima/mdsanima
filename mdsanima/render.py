'''
Render Time Module
------------------
This is a Simple Render Time Calculator.
'''

import time
from datetime import datetime, timedelta
from humanfriendly import format_timespan

def render_time(frame, rt_hours, rt_min, rt_sec, node=1):
    '''
    Simple Render Time Calculator.

    Parameters:
        ``frame`` `int`: How many frame you have to calculate render time.
        ``rt_hours`` `int`: Hours render time one frame.
        ``rt_min`` `int`: Minutes render time one frame.
        ``rt_sec`` `int`: Seconds render time one frame.
        ``node`` `int`: How many node you have. Default 1 node.
    Returns:
        `print`: Your render time stats.
    '''
    hours_conv = rt_hours * 60 * 60     # convert hours to second
    minutes_conv = rt_min * 60          # convert minutes to second

    time_conv = hours_conv + minutes_conv + rt_sec
    render_time_val = time_conv * frame
    rt = format_timespan(render_time_val)

    time_conv_span = format_timespan(time_conv)

    now = datetime.now()
    now_conv = now.strftime("%Y-%m-%d %H:%M:%S")
    end_time = now + timedelta(seconds=render_time_val)
    end_time_conv = end_time.strftime("%Y-%m-%d %H:%M:%S")

    node_time = render_time_val / node
    rt_node = format_timespan(node_time)

    end_time_node = now + timedelta(seconds=node_time)
    end_time_node_conv = end_time_node.strftime("%Y-%m-%d %H:%M:%S")

    fps_23 = frame / 23.98
    fps_23_conv = format_timespan(fps_23)
    fps_24 = frame / 24
    fps_24_conv = format_timespan(fps_24)
    fps_25 = frame / 25
    fps_25_conv = format_timespan(fps_25)
    fps_29 = frame / 29.97
    fps_29_conv = format_timespan(fps_29)
    fps_30 = frame / 30
    fps_30_conv = format_timespan(fps_30)
    fps_50 = frame / 50
    fps_50_conv = format_timespan(fps_50)
    fps_59 = frame / 59.94
    fps_59_conv = format_timespan(fps_59)
    fps_60 = frame / 60
    fps_60_conv = format_timespan(fps_60)

    print('=========================================================================')
    print('                     MDSANIMA RENDER TIME CALCULATOR')
    print('=========================================================================')
    print('         HOW MANY FRAME |', frame, 'frames')
    print('-------------------------------------------------------------------------')
    print('               23.98fps |', '{:>37}'.format(fps_23_conv), 'animation')
    print('                  24fps |', '{:>37}'.format(fps_24_conv), 'animation')
    print('                  25fps |', '{:>37}'.format(fps_25_conv), 'animation')
    print('               29.97fps |', '{:>37}'.format(fps_29_conv), 'animation')
    print('                  30fps |', '{:>37}'.format(fps_30_conv), 'animation')
    print('                  50fps |', '{:>37}'.format(fps_50_conv), 'animation')
    print('               59.94fps |', '{:>37}'.format(fps_59_conv), 'animation')
    print('                  60fps |', '{:>37}'.format(fps_60_conv), 'animation')
    print('-------------------------------------------------------------------------')
    print('  RENDER TIME ONE FRAME |', time_conv_span)
    print('          HOW MANY NODE |', node, 'node')
    print('=========================================================================')
    print('{:>25}'.format('1 NODE RENDER TIME |'), rt)
    print('{:>25}'.format('START RENDERING |'), now_conv)
    print('{:>25}'.format('STOP RENDERING |'), end_time_conv)


    if node == 1:
        print('=========================================================================')
    else:
        print('-------------------------------------------------------------------------')
        print('{:>6}'.format(node), 'NODE RENDER TIME |', rt_node)
        print('{:>25}'.format('START RENDERING |'), now_conv)
        print('{:>25}'.format('STOP RENDERING |'), end_time_node_conv)
        print('=========================================================================')