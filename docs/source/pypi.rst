Send to PyPi
============
Instructions on how to create your own python packages and send it to PyPi.

My First Pacage
---------------
Make sure your directory package structure looks like this.

.. code::

    my_package
        __init__.py
        module_1.py
        module_2.py

Code in ``__init__.py`` should look like this.

.. code:: python

    from .module_1 import function_1
    from .module_2 import function_2

Now if you want to call your ``function_1`` in a new ``main.py`` file, outside the ``my_package`` module.

.. code::

    main.py
    my_package
        __init__.py
        module_1.py
        module_2.py

Your code should look like this.

.. code:: python

    from my_package import function_1

Instead of.

.. code:: python

    from my_package.module_1 import function_1

Now your code is shorter. It's time to write you first function.

.. code:: python

    def function_1(x, y, z=10):
        mult = x * y * z

        return value

Pacage Docstring
----------------
Now enter the documentation into the code, the VS code extension will help us Python Docstring Generator ``njpwerner.autodocstring``, or write it yourself.

Each function in the your packages should have its own docstring documentation. 
- Describe in plain language what your function does. 
- Explain what parameters and types function expects.
- Explain what return the function gives.
- You can write a simple example of how to use.

Now you just need to position the cursor after the colon, hit enter. 
Cursor must be on the line directly below the definition to generate full auto populated docstring.

Press enter after opening docstring with triple quotes ``(""" or ''')``
Keyboard shortcut ``ctrl + shift + 2`` or ``cmd + shift + 2`` for mac user.
Documentation is almost ready, just complete the summary, types and description.

.. code:: python

    def function_1(x, y, z=10):
        """Sum of the multiplication x, y and z.

        Args:
            x `int`: Number.
            y `int`: Another number.
            z `int` optional: Another number. Defaults to 10.

        Returns:
            int: sum
        Examples: function_1(64, 128, 256)
        """
        mult = x * y * z

        return value

Add README.md or README.rst file. Add LICENSE file. Create the blank ``setup.py`` file.

Now the directory structure of your package must be as follows.

.. code::

    my_package
        LICENSE
        README.rst
        setup.py
        my_package
            __init__.py
            module_1.py
            module_2.py

Setup File
----------
Open the ``setup.py`` file and paste the code there. You can also add other features to it. Check the pypi_ documentation.

.. _pypi: https://pypi.org

.. code:: python

    '''
    MDSANIMA Setup
    '''

    import sys
    import pathlib
    from setuptools import setup, find_packages

    HERE = pathlib.Path(__file__).parent

    CURRENT_PYTHON = sys.version_info[:2]
    REQUIRED_PYTHON = (3, 6)

    # This check and everything above must remain compatible with Python 2.7.
    if CURRENT_PYTHON < REQUIRED_PYTHON:
        sys.stderr.write("""==========================
    Unsupported Python Version
    ==========================
    This version of MDSANIMA requires Python {}.{}
    but you're trying to install it on Python {}.{}
    """.format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
        sys.exit(1)

    VERSION = '0.1.0'
    PACKAGE_NAME = 'my_package'
    AUTHOR = 'my name'
    AUTHOR_EMAIL = 'myemail@address.com'
    URL = 'https://github.com/mdsanima/mdsanima'

    LICENSE = 'MIT License'
    DESCRIPTION = 'The package contains modules that will help in calculating rendering time.'
    LONG_DESCRIPTION = (HERE / "README.rst").read_text()
    LONG_DESC_TYPE = "text/x-rst"

    INSTALL_REQUIRES = [
            'humanfriendly'
    ]

    KEYWORDS = [
            'mdsanima',
            'render time',
    ]

    setup(name=PACKAGE_NAME,
            version=VERSION,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            long_description_content_type=LONG_DESC_TYPE,
            author=AUTHOR,
            license=LICENSE,
            author_email=AUTHOR_EMAIL,
            url=URL,
            install_requires=INSTALL_REQUIRES,
            packages=find_packages(),
            extras_require={
                "docs": [
                    'sphinx', 
                    'sphinx-autoapi', 
                    'sphinx-rtd-theme', 
                    'sphinx-bootstrap-theme', 
                    'sphinx-prompt', 
                    'sphinx-tabs', 
                    'recommonmark'
                    ],
            },
            python_requires='>=3.6',
            keywords=KEYWORDS,
            classifiers=[
                'Development Status :: 1 - Production/Stable',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Natural Language :: English',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
            ],
        )

.. warning::

   Every time you release a new version of PyPI, you must have to bump version number.

Create Acconut on PyPi
----------------------
We're almost there. Just create an account here `Master PyPi`_. You will need it to ship your package around the world. 
This is your main account. Log in and receive an email with verification.

We will need a second account, which we set up here `Test PyPi`_. This is your test account. 
It will be needed to test the package, if everything is fine we send the package to the main account. 
We set up an account with exactly the same data as the main account. We log in and receive an email with the verification.

.. _Master PyPi: https://pypi.org/account/register
.. _Test PyPi: https://test.pypi.org/account/register

Build Package
-------------
We're almost done. We just need to put commands in to terminal and which will create an installable Python Package from your ``code`` and send it to ``PyPi``.

Install Twine
~~~~~~~~~~~~~
.. prompt:: bash $

    python -m pip install twine

Build Setup
~~~~~~~~~~~
.. prompt:: bash $

    python setup.py sdist bdist_wheel

It created some new directories for us, such as ``dist``, ``build`` and ``your_package.egg-info``.

.. tip::

   Add these directories to the ``.gitignore`` file to prevent installation files from being pushed into the repository.

Check the Build
~~~~~~~~~~~~~~~
.. prompt:: bash $

    twine check dist/*

Send to Test PyPi
~~~~~~~~~~~~~~~~~
.. prompt:: bash $

    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Go to test.pypi.org_ and check if everything is ok, if yes, we can finally send our package to PyPi_.

.. _test.pypi.org: https://test.pypi.org

Finally Send To PyPi
~~~~~~~~~~~~~~~~~~~~
.. prompt:: bash $
    
    twine upload dist/*

.. tip::

   That’s it. Now anyone can install your package with ``python -m pip install my_package``. 
   
   Good job! Keep Coding! :guilabel:`We LOVE PYTHON`

Bash Script
~~~~~~~~~~~
A bash script that builds, checks and deploys the entire package at a time, with only one command.

Creat a new file named ``build_deploy.sh`` in ths same direcotry as ``setup.py``. Put this code on this file.

.. code:: bash

    rm -r dist ;
    python setup.py sdist bdist_wheel ;
    if twine check dist/* ; then
        if [ "$1" = "--test" ] ; then
            twine upload --repository-url https://test.pypi.org/legacy/ dist/*
        else
            twine upload dist/* ;
        fi
    fi

You can also add commands to this script to generate documentation, before making the package or other actions as you like.

Now run this command.

.. prompt:: bash $

    ./build_deploy.sh

or

.. prompt:: bash $

    ./build_deploy.sh --test

.. warning::

    When you run the script for the first time, give execute permission ``chmod + x build_deploy.sh``.

Write Article
~~~~~~~~~~~~~
Done, great job! Now your package can be installed by anyone around the world, but people don't know it yet. 
Write an article on your blog, on social media, informing people about this package. It can be really useful for someone.