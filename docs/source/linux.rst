Developer Help
==============
In this section are **important information**, coding tips, Windows and Linux tips, links etc. 

Check it out if you don't know something. I will write here various things that may be useful one day.

Linux Help
==========
In this section you will find some useful information about using ``Linux Ubuntu 18.04``. Of course you can also use WSL or WSL2.

Create Swap File
----------------
Quick tutorial how to create a swap file. `Swap File`_ Tutorial.

.. _Swap File: https://linuxize.com/post/create-a-linux-swap-file/

.. code::

    sudo fallocate -l 1G /swapfile
    sudo dd if=/dev/zero of=/swapfile bs=1024 count=1048576
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    sudo swapon --show
    sudo free -h
    remove swap
    sudo rm /swapfile

WLS GUI Config
--------------
Quick tutorial how to create a WSL GUI. `Config GUI Linux`_ Tutorial on YouTube.

.. _Config GUI Linux: https://www.youtube.com/watch?v=6x_okhl_CF4

Config GUI
~~~~~~~~~~

.. code::

    sudo apt update &&  sudo apt upgrade
    sudo sed -i 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
    sudo /etc/init.d/ssh restart
    sudo passwd ubuntu
    sudo apt install xrdp xfce4 xfce4-goodies tightvncserver
    echo xfce4-session$ /home/ubuntu/.xsession
    echo xfce4-session> /home/ubuntu/.xsession
    sudo cp /home/ubuntu/.xsession /etc/skel
    sudo sed -i '0,/-1/s//ask-1/' /etc/xrdp/xrdp.ini
    sudo service xrdp restart
    sudo apt install -y ubuntu-desktop xrdp         # additional package
    sudo reboot

Connect Putty
~~~~~~~~~~~~~

.. code::

    tunel:  secure port:5901
	destination -> private ip -> 111.11.11.111:3389

Connect WSL
~~~~~~~~~~~

.. code::

    echo xfce4-session > /.xsession
    sudo /etc/init.d/xrdp start

RDP Connection
~~~~~~~~~~~~~~

.. code::

    RDP remote desktop connection
    Computer 127.0.0.1:3390
    Computer localhost:3390