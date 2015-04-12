HowOld
======
This tool is intended as an exercise in basic Python packaging practices and language features. It is built around the ``datetime`` module from the Python Standard Library and the third-party package ``Click``.

This tool serves no actual purpose other than a rather impractical way of expressing your age, but it will be usable nonetheless with some useful options planned for it.

Installation
------------
There are several ways to install a Python package on your system. The most popular and straightforward one is the use of ``pip`` and ``virtualenv``. This document will cover a few common use cases.

First things first, is to install ``pip``. which can be installed with easy_install. Run the following command (may require administrator rights)::

    easy_install pip

or to run as administrator (this will prompt you for your password)::

    sudo easy_install pip

If pip was installed successfully you can either proceed to the installation procedure for end users, or you can proceed to install ``virtualenv``. Which will allow you to cleanly separate third-party packages and any dependencies from your global python distribution.

This is the most recommended way if you are a python developer and want to write, use or modify python packages in any way possible. Follow `these <http://www.jontourage.com/2011/02/09/virtualenv-pip-basics/>`_
instructions for a good primer on the use of ``virtualenv``. 

Installation for End Users
^^^^^^^^^^^^^^^^^^^^^^^^^^  
To install ``howold`` isolated from the global site-packages you can use the so called user scheme for Python packages. The following steps will cover this scheme as the default way. This section assumes you have pip installed on your system.

First, unpack the latest version of this program with your favorite archive manager or use the following command inside the download folder (substitute pound sign with the correct version)::

    tar -xvzf Howold-0.#.#.tar.gz

Navigate to the unpacked folder and run the following commands::

    export PYTHONUSERBASE=$HOME/.local/bin
    pip install --user .

Most likely, the ``PYTHONUSERBASE`` will not be present in the ``PATH`` variable of your system. To be able to use this script as a command, add the following line to ``~/.profile`` with your favorite text editor (make sure you put the colon in the correct place)::

    export PATH=$HOME/.local/bin:$PATH

To reflect the changes to this file immediately run::
    
     source .profile

If all was correct you should be able to run the command ``howold`` anywhere from the terminal and you should see the help text.
