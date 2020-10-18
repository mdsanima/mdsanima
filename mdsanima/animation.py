"""
Animation Module
----------------
Terminal print output animation.
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

def anim_ascii():
    """
    Print ascii foto animation.

    Returns:
        print: Ascii animation.
    Usage:

    .. code::
    
        anim_ascii()
    """

    count_up = 0
    ascii_foto = """oool:;,''',,'',:okKNNNNNKOxoc;;;:ldkkOOO000000000000KKKKKKKKK0OkkOXNNNNNN
coddlc:;,'',,,,cx0XXXXKOxoc;;;;;:oxkkOOO000000000000KKKKKKKK000kxkOKXNNXX
';lxxdlc:;,',;;ck0K00Odl:,,'',::ldkkkkOOO0000000000000KKKKK00KKOkddkKXXXX
'',:dxdolc:;,,:ldOkxol;,''''',:coxkkkOOOO00000000000000KKKKKK000Oxoox0XXX
..',,coddlcc:;:codo:;,'''''',;cldxkOOO000000000000000000000000000OxodkKNX
...''',:lolccc::cl:;,'''''',';ldxkOOOOOOO00000000000000000OOOOOOOkxdxk0KN
;'...''';:loocccc:;,'..'',;;';oxxkkkkkkOOOOOOOO00OOkdolllloddddddooodxxk0
cc;'...',,;coolc:;;,'..'',:;,:cccc::;;;:cllooolllc:;;cloxO00K00000OOxddxO
';cl:'...'',:ool;,;,...',,::,;,',lddddll:,'.....'..:dOOO0K00000O0KKXKkodk
''',cl:'...',;:;,,;'..'';;:c;,',':xOOOO0KO:..',;''cO0Oxox0000000KKOkOxox0
..''',:c:,..',,'',,...',::cl;'',,;xK00xok0o''ckOd,;xOxoldOOkkkkOOkdodolx0
.''''''';cc;''''','...';:;c:,'',;:oO0OdlxOo',dO00l;cdl:lxOOkO00OOOOkxdok0
,'....'''',;;,'''''...,:;:c:,,,,;;:oxo:lxOl':xO00k:,,',coxOOOO0K0000OxxO0
'''......''''''''''..',,;::;,,,',,',,,';:;',lxO0K0x:'''ckOOkO00KKK0kddkOK
,,,,,,;;;;:::,''',,''''',;,,,,',,,,,,''...':lxO00K0ko:;;coxkkOkkkxocodkOK
cccccccclllolc;,,;;;'''''.''',,,,,''''''';cloxO00KK00kdollooodddxdc:ldk0X
lllllooooddddlc:;:;,'......''',,,,,;;:cloooodkO000KKKOOOkkOO00000xllok0XN
llllllllooloolcc:;,'......',,;:clodxxkkkxdooooxOO00OO000000000000xodxOXNW
ccccclodlcccloolc,'........',:ldxkkkkkkkxdoc;,:dkOkdk000000000K0kolox0NWW
cccccdkOkxdooddl:,'''.......,:ldxxkkkkkkxdl;,,;lxkkk0000O0000K0Od::ckXNWW
ccccokOOOOOxdoc:;,'''.......';codxxxxxxxdoc;,,;cllclxO0000000K0ko:coOXNNW
clloxOOOOOkxoc:;,''..........,:loddxxxdoc:,,,;cooolloxkkO000000kdokKXXNNW
llldkOOOOOKN0dl::;,'.........',:lodddolc:::;:cloddxxxkkxkO0000OkkOKXNWWWW
ccoxOOOOOKNNXKK0Oxc:c::c,',;,'';:cloollclc;;;:cloodxxkkkOO000OOk0XNWWNWWW
llxkOOOOOXWWWNXK0OO0KXK0xc:lc,',;;:ccllooolccodxxkkOOOOOOO000OO0XWWWWWWMM
loxOOOOO0NWNNNXKXKXNWWMWNOddl;',;;;;::cloooooddxxkkOOOOOkkO00OKNNWWWWWWMM
lxkOOkO0XWNXNWNNXNWWWWWWNXK0Odc;;;;;;,,;clooddxxxkOOOOOkxdxOO0XNNNWWWWWWW
okkOOkOKNWNNWWWWNNWWWWWWWWWWWNKkxdc,''',;:lodxxddxkOOOkdookKXNNNWNNNNWWWW
xkkkkkkkOOO0KKXK0OkxOXWWWWWWNWKOxoc;,,''',;:llollldddol::oO0000KKKKXNNNNN
kkkkkxdooloooddooddooxKXK00Okkxl;,;;;;,''''',;;;,;:;;;,,:xOOOkxOOOOO00KXX
kkkkxl,';;cl:;;:ldoccdkkxdoolc:;'',,,,,,,''..'''''''',;ldkOOOxdxkkOOkkOO0
kkkkd;....';;;,;codoodddolllc:::,',,,,,,,,,,''''..',:oxkOOkkkxdxxkkkkO0OO
kxxdc...',:coxxxkkkkxxdooollc::::;;,,,,;;;;::cclccldxkkkkkkxxxxxxkkkxxkO0
"""
    while (2440 >= count_up):
        print(ascii_foto[count_up % len(ascii_foto)], end = '', flush = True)
        count_up += 1
        time.sleep(0.0001)