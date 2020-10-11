Blender Rendering
=================
How to Blender command line rendering works. Let me show you an example on an instance with AWS Spot.
Of course, you can use any other provider as you like.

Create AWS Spot Instance
------------------------
- Log in to your ``AWS`` account. 
- Go to ``EC2 Dashboard``. 
- Then go to ``Instances``.
- Select ``Launch Instances``. 
- Choose an Amazon Machine Image AMI.
- Select this one ``Ubuntu Server 18.04 LTS``.
- Next choose an Instance Type.
- For testing choose ``t2.large``.

.. tip::

   The best instance for rendering is ``Compute Optimized``.

- Click ``Next: Configure Instance Details``.
- Now configure your instance as you like.
- Select Purchasing option ``Request Spot Instance``

.. warning::

   This option is several times cheaper than a regular instance. 
   But it can happen that you get disconnected from the instance. 
   Spot instances are the unused computing power of Amazon's cloud. 
   If they need that power again, you'll be disconnected. 
   Relax, your data will not be deleted, because we will do EFS 
   Elastic File Storage and connect to this instance.

- Click ``Next: Add Storage``.
- Default its fine.
- Click ``Next: Add Tags``.
- Default its fine.
- Click ``Next: Configure Security Group``
- Default ist fine too for testing.
- Finnaly click ``Review and Launch``.
- Click ``Launch``.
- Create new SSH Key. Save this file on your machine.

At this point we have created one spot instance and next we are going to connect ``EFS`` Elastic File System.

Now we wait about 2 minutes until our instance is fully operational.

Connect to Spot Instance
------------------------
At this point, we can connect to the instance, we can do it in 2 ways.

Connect with PuTTy on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The first time we need to convert your SSH key so that PuTTYy can read it.

- Click RMB on the PuTTy icon in your system toolbar. 
- Choose the PuTTY Key Generator.
- Load your SSH Key.
- Click ``Save public key`` and choose your location.
- File should be a name like this ``ssh-key-conv.ppk``.

At this point, we have the key converted. All you need to do now is fire up PuTTy Configuration.

- Fill it up ``Host Name``. Should look like this ``ec2-1-11-111-111.us-east-2.compute.amazonaws.com`` or IP address ``1.11.111.111``.
- In the ``Category`` choose ``Connection`` and ``SSH``. Next choose ``Auth``.
- Then enter the path to the converted ssh key in ``Private key file for authentication:``.
- Finally click ``Open``. That's it, now we are logged in to the spot instance.

Conncet with SSH on Linux WSL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This option is much simpler. Only put the command in to terminal.

.. code::

    ssh -i "ssh-key.pem" ubuntu@ec2-1-11-111-111.us-east-2.compute.amazonaws.com

Done.

EFS Elastic File System
-----------------------
- Go to ``Amazon Elastic File System EFS`` in your AWS dashboard.
- Create file system.
- Save the ``IP address`` on your ``Availability Zone`` where your spot instance works. Should look like this ``222.22.2.222``.

Now go to the terminal and enter this command.

.. code::

    apt-get update && apt-get install nfs-common -y
    cd /mnt
    mkdir efs
    ls
    sudo mount -t nfs4 222.22.2.222:/ /mnt/efs

Everything is ready, now you can mount this EFS to multiple instances. 
Just put the command showed up above for each instance. `YouTube Tutorial EFS`_

.. _YouTube Tutorial EFS: https://www.youtube.com/watch?v=NR8rVsSn_dY

Command Line Rendering
----------------------
Now we can start the actual rendering of our scenes in the Blender and Cycles render engine. We will use ``Blender Command Line Rendering``.

Download Blender
~~~~~~~~~~~~~~~~
In the terminal put this command.

.. code::

    wget https://your_serwer.com/aws/blender-2.90.0-linux64.tar.xz
    wget https://your_serwer.com/aws/your_blender_scene_v01_aws.tgz

If you don't have your own server where you store files, you can use this command.

.. note::

    You must be in the folder where you have the files to send ``./`` or just put path.

In Microsoft PowerShell Terminal.

.. code::

    pscp -i "C:\path\ssh-key-conv.ppk" ./blender-2.90.0-linux64.tar.xz ubuntu@1.11.111.111:/mnt/efs/
    pscp -i "C:\path\ssh-key-conv.ppk" ./your_blender_scene_v01_aws.tgz ubuntu@1.11.111.111:/mnt/efs/

In Linux WSL Terminal.

.. code::

    scp -i "/home/name/path/ssh-key.pem" ./blender-2.90.0-linux64.tar.xz ubuntu@1.11.111.111:/mnt/efs/
    scp -i "/home/name/path/ssh-key.pem" ./your_blender_scene_v01_aws.tgz ubuntu@1.11.111.111:/mnt/efs/

.. tip::

    SSH key in Windows should be in the ``C:\Users\name\.ssh\`` directory.
    SSH key in Linux should be in the ``/home/name/.ssh/`` directory.

These commands allow you to upload files from your computer to the AWS server. 
You can also reverse the operations and download files from the server.
You just need to change the path. I'll show it in a moment how to download the files.

All downloaded files should be in ``/mnt/efs/``.

.. code::

    cd /mnt/efs/                                # go to direcotry
    tar -xf ./blender-2.90.0-linux64.tar.xz     # unpack Blender file
    mv ./blender-2.90.0-linux64 ./b290    # move Blender to directory
    tar -xf ./your_blender_scene_v01_aws.tgz    # unpack Scene file
    mv ./your_blender_scene_v01_aws ./blend     # move Scene to directory

Now Blender is almost ready to go.

Install Pacage
~~~~~~~~~~~~~~
Now update your system and install the necessary packages to run Blender properly.

.. code::

    sudo apt-get update && sudo apt-get dist-upgrade
    sudo apt-get install libboost-all-dev
    sudo apt-get install libgl1-mesa-dev
    sudo apt-get install libglu1-mesa libsm-dev
    sudo apt-get install libxi6
    sudo apt-get install libxrender1

Blender is ready to go.

Render Your Scene
~~~~~~~~~~~~~~~~~
When everything installed properly, we can start rendering.

CPU One Frame
+++++++++++++
This command allow to render only one frame on CPU.

.. code::

    sudo /mnt/efs/b290/blender -b '/mnt/efs/blend/sc_aws.blend' -o '/mnt/efs/blend/01/' -f 1

CPU All Frame
+++++++++++++
This command allow to render all frame on CPU.

.. code::

    sudo /mnt/efs/b290/blender -b '/mnt/efs/blend/sc_aws.blend' -o '/mnt/efs/blend/01/' -s 1 -e 26 -a

GPU All Frame
+++++++++++++
This command allow to render all frame on GPU. You must have a special instance with Elastic GPU, or dedicated e.g. with 8 GPU Nvidia v100.
Check the Amazon EC2 On-Demand Pricing or Spot Instance Pricing. All links at the bottom of the page.

You must be in ``/mnt/efs/``. You must also have a python script ``setgpu.py`` on your server in destination ``/mnt/efs/setgpu.py``.
You can send it at the very beginning or create this file right now, just put this command on the terminal.

.. code::

    cd /mnt/efs/
    nano setgpu.py

You have just created an empty python file. Now put this code in to the setgpu.py file. 
Copy it, and paste it into the nano editor by right clicking on the terminal AWS machine.

.. code:: python

    import re
    import bpy
    scene = bpy.context.scene
    scene.cycles.device = 'GPU'
    prefs = bpy.context.preferences
    prefs.addons['cycles'].preferences.get_devices()
    cprefs = prefs.addons['cycles'].preferences
    print(cprefs)
    # Attempt to set GPU device types if available
    for compute_device_type in ('CUDA', 'OPENCL', 'NONE'):
        try:
            cprefs.compute_device_type = compute_device_type
            print('Device found',compute_device_type)
            break
        except TypeError:
            pass
    # Enable all CPU and GPU devices
    for device in cprefs.devices:
        if not re.match('intel', device.name, re.I):
            print('Activating',device)
            device.use = True

Now just save the file and close it ``crtl + x -> y -> enter``. 

Great now you can run this command to activate gpu rendering.

.. code::

    cd /mnt/efs/
    sudo ./b290/blender -P setgpu.py -b '/mnt/efs/blend/sc_aws.blend' -o '/mnt/efs/blend/01/' -s 1 -e 26 -a

.. tip::

    You can use this command ``/mnt/efs/b290/blender --help`` to show help.

The first part ``sudo /mnt/efs/b290/blender -b`` of the command.

- Allow to start blender in the background ``-b``.

Second part ``'/mnt/efs/blend/sc_aws.blend'`` of the command.

- Your file to be rendered.

Last part ``-o '/mnt/efs/blend/01/' -s 1 -e 26 -a`` of the command.

- Output directory ``-o``.
- Frame to render ``-f 1``.
- Frame start ``-s 1``.
- Frame end ``-e 26``. 
- Animation playback ``-a``.
- Run the given Python script file ``-P setgpu.py``.

Check out the `Blender Ducumentation`_ for more info.

.. _Blender Ducumentation: https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html

Download Ouptut File
~~~~~~~~~~~~~~~~~~~~
Now it's time to download your render file output. We do the same as with `Download Blender`_, we just swap paths like this.

In Microsoft PowerShell Terminal.

.. code::

    cd C:\your_blender_output\              # download all the output file in this directory
    pscp -i "C:\path\ssh-key-conv.ppk" ubuntu@1.11.111.111:/mnt/efs/blend/01/* ./

In Linux WSL Terminal.

.. code::

    cd /home/name/your_blender_output/      # download all the output file in this directory
    scp -i "/home/name/path/ssh-key.pem" ubuntu@1.11.111.111:/mnt/efs/blend/01/* ./

.. tip::

    Right after rendering done in your instance you can exit on the instance and delete it. 
    Files that rendered are on EFS so they will not be deleted. Now just turn on cheaper instance and download all files.

Now you know how to render Blender file in the cloud with command line rendering. So just now use my `Render Time Package`_ and calculate render time for your scenes.

Just type in the terminal.

.. code::

    python -m pip install mdsanima

More Instances
~~~~~~~~~~~~~~
Now you can create more instances with more processors. 
You already have a blender installed on the EFS, so you won't have to repeat this step for each instance. 
You only need to run an instance, connect to it and select files for rendering. 
Enter the command to connect EFS and enter the command for rendering.

Of course it is also possible to run instances on AWS with Linux Ubuntu Elastic GPU or dedicated GPU 
and activate GUI to have a live view. Rather, it only works with a small scene and one On-Demand instance or Spot Instance.
You would have to use this method `Developer Config GUI`_

You can also use the Python AWS API to run an On-Demand Instance or Spot Instance in the command line and python script. 
You will save time and pay less for rendering.

In the future, I will write a some Python Package that will run the given number of instances on AWS. Run the necessary commands to update the servers. 
It will connect all instances from EFS Elastic File System at once and run rendering on all instances simultaneously. 
After rendering is finished, it will automatically delete instances and create one small instance to download all files.

.. _Render Time Package: https://pypi.org/project/mdsanima/
.. _Developer Config GUI: linux.html#config-gui

AWS Useful Links
----------------
Here I will post useful links to Amazon AWS Cloud.

- `Amazon EC2 On-Demand Pricing`_
- `Amazon EC2 P2 Instances`_
- `Amazon EC2 P3 Instances`_
- `Amazon EC2 G3 Instances`_
- `Amazon Elastic Inference Pricing`_
- `Amazon Elastic Graphics`_
- `Amazon Elastic Graphics Documentation`_
- `Recommended GPU Instances`_
- `AWS Pricing Calculator`_

.. _Amazon EC2 On-Demand Pricing: https://aws.amazon.com/ec2/pricing/on-demand/
.. _Amazon EC2 P2 Instances: https://aws.amazon.com/ec2/instance-types/p2/
.. _Amazon EC2 P3 Instances: https://aws.amazon.com/ec2/instance-types/p3/
.. _Amazon EC2 G3 Instances: https://aws.amazon.com/ec2/instance-types/g3/
.. _Amazon Elastic Inference Pricing: https://aws.amazon.com/machine-learning/elastic-inference/pricing/
.. _Amazon Elastic Graphics: https://aws.amazon.com/ec2/elastic-graphics/
.. _Amazon Elastic Graphics Documentation: https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-graphics.html?icmpid=docs_ec2_console
.. _Recommended GPU Instances: https://docs.aws.amazon.com/dlami/latest/devguide/gpu.html
.. _AWS Pricing Calculator: https://calculator.aws/#/