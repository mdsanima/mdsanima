Terminal Command
================
This is a list of useful Terminal Command. Works on Windows PowerShell Terminal, Linux Ubuntu and WSL Windows Subsystem for Linux.

Python
------
List of useful Python Terminal Command.

.. code::

    python -m pip install mdsanima                      # install package
    python -m pip install mdsanima==0.1.1               # install specific version
    python -m pip install --upgrade mdsanima            # upgrade to latest version
    python -m pip install --force-reinstall mdsanima    # force reinstall
    python -m pip uninstall mdsanima                    # uninstall package
    ​python -m pip list                                  # list of installed packages
    nohup python -u script.py > output.log &            # run python script background save log

Linux
-----
List of useful Linux Terminal Command.

.. code::

    ls -l -a -h                             # show list hide file show MB
    sudo curl ifconfig.me                   # show ip
    df -H /                                 # disc spaces
    free -h                                 # ram info
    neofetch                                # system info
    glances                                 # system info
    htop                                    # system stats
    nvidia-smi                              # show gpu stats
    sudo ubuntu-drivers autoinstall         # install gpu drivers
    watch -n 0.5 nvidia-smi                 # show gpu stats and refresh
    cat file.txt                            # print file
    nano file.txt                           # edit file
    sudo rm -r file*                        # delete all files
    pkill "python*"                         # kill all python process
    ssh-keygen -C "your@email.com"          # create ssh key
    aliases                                 # show all your aliases
    aliases my_ali="sudo rm -r file*"       # create aliases
    history                                 # command line history
    sudo apt-get update && apt-get upgrade  # update and upgrade
    tmux --help                             # multi window show help