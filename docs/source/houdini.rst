Houdini Rendering
=================
How to Houdini command line rendering works. Let me show you an example on an instance with AWS Spot.
Of course, you can use any other provider as you like.

First things we know to do. You have to do them to start rendering.

- `Create AWS Spot Instance`_
- `Connect to Spot Instance`_
- `Create EFS Elastic File System`_

.. _Create AWS Spot Instance: blender.html#create-aws-spot-instance
.. _Connect to Spot Instance: blender.html#connect-to-spot-instance
.. _Create EFS Elastic File System: blender.html#efs-elastic-file-system

Command Line Rendering
----------------------
Now we can start the actual rendering of our scenes in the Houdini and Mantra render engine. We will use ``Houdini Command Line Rendering``.

Download Houdini
----------------
I will use this `Python Script to Download Houdini`_. Auto install Houdini script for Windows and Linux developed by `@paulwinex <https://github.com/paulwinex>`__

.. _Python Script to download Houdini: https://github.com/paulwinex/houdini_install_script/blob/master/houdini_install.py

Just clone this repository to our AWS Linux Ubuntu Instance. Put this code in the terminal.

.. code::

    cd /mnt/efs/
    git clone https://github.com/paulwinex/houdini_install_script.git

Then run this script like this.

.. code::

    cd /mnt/efs/
    sudo python ./houdini_install.py -u username -p password -i /opt/houdini -s y

Replace ``username`` and ``password`` with your login details from `SideFx Website`_

.. _SideFx Website: https://www.sidefx.com/

Now upload your houidni files to the server you want to render. Use this method of `uploading files to the server`_.

.. _uploading files to the server: blender.html#download-blender

Houdini is Installed and then running this command.

.. code::

    source houdini_setup
    hkey

Install Houdini License
-----------------------
The next steps is to install the Houdini License on the server. Put this command in the terminal.

.. code::

    sesictrl -L

Follow the instructions to download the Server Licenses.

Render Your Scene
-----------------
When everything installed properly, we can start rendering on this server.

You need to create a file like this.

.. code::

    cd /mnt/efs/
    nano render.cmd

Then put this code in to the ``render.cmd`` file.

.. code:: 

    # Rendering From the Command Line
    # Open the Hip File
    mread your_scene_aws.hiplc

    # Bake FEM Simulation
    #render -V /obj/roberto/filecache1/render

    # Turn on Load From Disk
    #opparm /obj/roberto/filecache1/ loadfromdisk on
    #python -c 'hou.parm("/obj/roberto/filecache1/loadfromdisk").set(1)'

    # Render Camera
    render -V cam01

    # quit

Now you can start rendering by typing.

.. code::

    hscript render.cmd

That's it, now you are waiting for the result.

.. warning::

   Remember your paths in the ``.hip`` file must be relative path. Otherwise it won't render properly.

Download Output File
--------------------
Now it's time to download your render file output. Use this method of `downloading files from the server`_.

.. _downloading files from the server: blender.html#download-ouptut-file

That's it, exit the server and delete it. Now you know how to render Houdini file in the cloud with command line rendering. So just now use my `Render Time Package`_ and calculate render time for your scenes.

.. _Render Time Package: https://pypi.org/project/mdsanima/

Just type in the terminal.

.. code::

    python -m pip install mdsanima

Now go into `this step`_

.. _this step: blender.html#more-instances