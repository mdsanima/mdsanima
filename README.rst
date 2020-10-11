Welcome to MDSANIMA Python Package
==================================

|latest-version-on-pypi| |supported-python-version| |documentation| |downloads|

.. |latest-version-on-pypi| image:: https://img.shields.io/pypi/v/mdsanima.svg
    :alt: Latest Version on PyPi
    :target: https://pypi.org/project/mdsanima

.. |supported-python-version| image:: https://img.shields.io/pypi/pyversions/mdsanima.svg
    :alt: Supported Python Versions
    :target: #Installation

.. |documentation| image:: https://readthedocs.org/projects/mdsanima/badge/?version=latest
    :alt: Documentation
    :target: https://mdsanima.readthedocs.io

.. |downloads| image:: https://pepy.tech/badge/mdsanima
    :alt: Downloads
    :target: https://pepy.tech/project/mdsanima

The package_ contains modules that will help in calculating rendering time.
The package also includes a module for print your text with an animation counting up or down.

.. _package: https://pypi.org/project/mdsanima/

Install Package
---------------

.. warning::

    :guilabel:`MDSANIMA` package only works in ``Python 3.6`` or later.

.. prompt:: bash $

    python -m pip install mdsanima              # install latest version
    python -m pip install mdsanima==0.1.1       # install specific version

Upgrade Package
---------------

.. prompt:: bash $

    python -m pip install --upgrade mdsanima    # upgrade to latest version

Uninstall Package
-----------------

.. prompt:: bash $

    python -m pip uninstall mdsanima            # uninstall package

Usage
-----
Module ``render_time`` returns print of render stats.

    >>> from mdsanima import render_time
    >>> render_time(512, 1, 0, 24, 128)

Module ``count_down`` and ``count_up`` returns print text and count animation.

    >>> from mdsanima import count_down
    >>> from mdsanima import count_up
    >>> count_down('Your text ', 20, 0.1)
    >>> count_up('Your text ', 500, 0.001)

Documentation
-------------
Full :guilabel:`MDSANIMA` package documentation can be found here documentation_

.. _documentation: https://mdsanima.readthedocs.io

Languages and Tools
-------------------
This tools and languages we're using every day.

|ubuntu| |visual-studio-code| |python| |html| |css| |jacascript| |firebase| |azure| |aws| |sql| |mysql| |git| |github| |terminal|

.. |ubuntu| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/ubuntu/ubuntu.png
    :alt: Ubuntu
    :target: https://mdsanima.com
    :height: 30px
    :width: 30px

.. |visual-studio-code| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png
    :alt: Visual Studio Code
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |python| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png
    :alt: Python
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |html| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png
    :alt: HTML5
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |css| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png
    :alt: CSS3
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |jacascript| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png
    :alt: JavaScript
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |firebase| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/firebase/firebase.png
    :alt: Google Firebase
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |azure| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/azure/azure.png
    :alt: Microsoft Azure
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |aws| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/aws/aws.png
    :alt: AWS
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |sql| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/sql/sql.png
    :alt: SQL
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |mysql| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/mysql/mysql.png
    :alt: MySQL
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |git| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png
    :alt: Git
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |github| image:: https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png
    :alt: GitHub
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

.. |terminal| image:: https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png
    :alt: Terminal
    :target: https://app.mdsanima.com
    :height: 30px
    :width: 30px

3D Stuff
--------
These application we're using every day.

|blender| |houdini| |unrealengine| |cinema4d| |nuke| |gimp|

.. |blender| image:: https://cdn.jsdelivr.net/npm/simple-icons@3.11.0/icons/blender.svg
    :alt: Blender
    :target: https://www.blender.org
    :height: 30px
    :width: 30px

.. |houdini| image:: https://cdn.jsdelivr.net/npm/simple-icons@3.11.0/icons/houdini.svg
    :alt: SideFx Houdini
    :target: https://www.sidefx.com
    :height: 30px
    :width: 30px

.. |unrealengine| image:: https://cdn.jsdelivr.net/npm/simple-icons@3.11.0/icons/unrealengine.svg
    :alt: Epic Games Unreal Engine 4
    :target: https://unrealengine.com
    :height: 30px
    :width: 30px

.. |cinema4d| image:: https://cdn.jsdelivr.net/npm/simple-icons@3.11.0/icons/cinema4d.svg
    :alt: Maxon Cinema 4D
    :target: https://maxon.net
    :height: 30px
    :width: 30px

.. |nuke| image:: https://cdn.jsdelivr.net/npm/simple-icons@3.11.0/icons/nuke.svg
    :alt: Foundry Nuke
    :target: https://foundry.com
    :height: 30px
    :width: 30px

.. |gimp| image:: https://cdn.jsdelivr.net/npm/simple-icons@3.11.0/icons/gimp.svg
    :alt: Gimp
    :target: https://gimp.org
    :height: 30px
    :width: 30px

Latest YouTube Videos
---------------------

- `4K Sky Timelaps Starlink SpaceX Satellite`_
- `Sharp Old Radio 3D Model Turntable`_
- `Lego Architect 3D Model Turntable`_
- `Lego Mindstorms Reptar 3D Model Turnable`_
- `Lego Mindstorms Grip3r 3D Model Turnable`_

.. _4K Sky Timelaps Starlink SpaceX Satellite: https://www.youtube.com/watch?v=dW9VRi_NmZQ
.. _Sharp Old Radio 3D Model Turntable: https://www.youtube.com/watch?v=qAER517bznI
.. _Lego Architect 3D Model Turntable: https://www.youtube.com/watch?v=jLsj7MqR85Y
.. _Lego Mindstorms Reptar 3D Model Turnable: https://www.youtube.com/watch?v=uyqqlyDHJ-Y
.. _Lego Mindstorms Grip3r 3D Model Turnable: https://www.youtube.com/watch?v=VRYSmrVAXew

Latest Blog Post
----------------

- `Starlink SpaceX Satellite`_
- `Starlink SpaceX Elon Musk Satellite Photography`_
- `Fruits Dance Man Mograph Animation`_
- `Strawberry Dance Man Animation`_
- `Mograph Animation`_

.. _Starlink SpaceX Satellite: https://blendervisual.blogspot.com/2020/07/4k-sky-timelaps-starlink-spacex.html
.. _Starlink SpaceX Elon Musk Satellite Photography: https://blendervisual.blogspot.com/2020/05/starlink-spacex-elon-musk-satellite.html
.. _Fruits Dance Man Mograph Animation: https://blendervisual.blogspot.com/2019/12/fruits-dance-man-mograph-animation.html
.. _Strawberry Dance Man Animation: https://blendervisual.blogspot.com/2019/12/strawberry-dance-man-cinema-4d.html
.. _Mograph Animation: https://blendervisual.blogspot.com/2019/12/mograph-animation-cinema-4d-and.html

Connect With Me
---------------
Hi there, I'm Marcin Różewski aka MDSANIMA_. These are all my social media and websites, check it out please. Thanks.

.. _MDSANIMA: https://mdsanima.com

|twitter_toudajew_badge| |twitter_str9led_badge| |twitter_mdsanima_badge|

.. |twitter_toudajew_badge| image:: https://img.shields.io/twitter/follow/toudajew?color=1DA1F2&logo=twitter&style=flat
    :alt: Twitter TOUDAJEW Follow
    :target: https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fgithub.com%2Ftoudajew&screen_name=toudajew

.. |twitter_str9led_badge| image:: https://img.shields.io/twitter/follow/str9led?color=1DA1F2&logo=twitter&style=flat
    :alt: Twitter STR9LED Follow
    :target: https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fgithub.com%2Fstr9led&screen_name=str9led

.. |twitter_mdsanima_badge| image:: https://img.shields.io/twitter/follow/mdsanima?color=1DA1F2&logo=twitter&style=flat
    :alt: Twitter MDSANIMA Follow
    :target: https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fgithub.com%2Fmdsanima&screen_name=mdsanima

My Social Media and Websites.

|website| |blog_blender| |github_account| |youtube| |vimeo| |twitch| |twitter_toudajew| |linkedin| |instagram_mdsanima| |facebook| |mailchimp_subscribe| |turbosquid|

|github-status|

.. |website| image:: https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg
    :alt: MDSANIMA
    :target: https://mdsanima.com
    :height: 30px
    :width: 30px

.. |blog_blender| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/blogger.svg
    :alt: BLOG BLENDER
    :target: https://blendervisual.blogspot.com
    :height: 30px
    :width: 30px

.. |github_account| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg
    :alt: GITHUB 
    :target: https://github.com/mdsanima
    :height: 30px
    :width: 30px

.. |youtube| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/youtube.svg
    :alt: YOUTUBE
    :target: https://youtube.com/mdsanima
    :height: 30px
    :width: 30px

.. |vimeo| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/vimeo.svg
    :alt: VIMEO
    :target: https://vimeo.com/str9led
    :height: 30px
    :width: 30px

.. |twitch| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitch.svg
    :alt: TWITCH
    :target: https://www.twitch.tv/str9led
    :height: 30px
    :width: 30px

.. |twitter_toudajew| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg
    :alt: TWITTER TOUDAJEW
    :target: https://twitter.com/toudajew
    :height: 30px
    :width: 30px

.. |linkedin| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg
    :alt: LINKEDIN
    :target: https://www.linkedin.com/in/mdsanima
    :height: 30px
    :width: 30px

.. |instagram_mdsanima| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg
    :alt: INSTAGRAM MDSANIMA
    :target: https://instagram.com/mdsanima
    :height: 30px
    :width: 30px

.. |facebook| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/facebook.svg
    :alt: FACEBOOK MDSANIMA
    :target: https://www.facebook.com/mdsanima
    :height: 30px
    :width: 30px

.. |mailchimp_subscribe| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/mailchimp.svg
    :alt: MAILCHIMP MAILING LIST
    :target: https://mdsanima.mailchimpsites.com
    :height: 30px
    :width: 30px

.. |turbosquid| image:: https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/turbosquid.svg
    :alt: TURBOSQUID 3D MODEL SHOP
    :target: https://goo.gl/7TYKfT
    :height: 30px
    :width: 30px

.. |github-status| image:: https://github-readme-stats.codestackr.vercel.app/api?username=mdsanima&show_icons=true&hide_border=true
    :alt: MDSANIMA GitHub Stats

License
-------
Mdsanima is released under the terms of `MIT License`_

.. _MIT License: LICENSE