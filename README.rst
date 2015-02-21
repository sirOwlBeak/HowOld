AgeToSeconds
============
This tool is intended as a little programming excercise in Python and to learn the basics of packaging a Python project. It is built around the `datetime` module in Python.

This tool serves no actual purpose other than a rather impractical way of expressing your age. It will however be a useable tool with a command line interface and lots of options to format the output.

Installation
------------
You can either install this package directly inside the global site-packages, which is usually not recommended if you are a developer, or you can use a virtual environment to cleanly separate this package your global python distribution.

To install directly into your global site-packages , navigate to the AgeToSeconds folder and use the following command::

    ~/AgeToSeconds$ pip install .

To contribute to this package you can use virtualenv to make a local copy of your python distribution. Navigate to the AgeToSeconds folder and use the following commands::

    ~/AgeToSeconds$ virtualenv venv
    ~/AgeToSeconds$ source venv/bin/activate
    (venv)~/AgeToSeconds$ pip install -e .
