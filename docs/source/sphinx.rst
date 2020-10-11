Sphinx Auto Documentation
=========================
Python Sphinx_ package automatically generates technical documentation for python modules ``.py`` ``.rst`` and ``.md`` files.

.. _Sphinx: https://www.sphinx-doc.org/en/master/

Install Sphinx
--------------

.. code::

    python -m pip install sphinx                    # install sphinx package
    python -m pip install sphinx-autoapi            # install sphinx extensions package
    python -m pip install sphinx-tabs               # install sphinx extensions package
    python -m pip install sphinx-prompt             # install sphinx extensions package
    python -m pip install sphinx-bootstrap-theme    # install sphinx theme package
    python -m pip install sphinx-rtd-theme          # install sphinx theme package
    python -m pip install recommonmark              # install markdown pacage

Create Sphinx Documentation
---------------------------

.. code::

    mkdir docs
    cd docs
    sphinx-quickstart

Select create documentation with build and source separation. Edit ``conf.py`` file. Add extension and change the themes.

Windows PowerShell

.. code::

    .\make.bat html

Linux

.. code::

    make html

Add directives to the .rst file to make your docs quickly. All directives avaiable in Sphinx_ Documentation.

.. code::

    .. include:: ../../CHANGELOG.rst

    .. automodule:: mdsanima.animation
        :members:

    .. automodule:: mdsanima.render
        :members:

    .. toctree::
        :maxdepth: 2

        developer

    .. tip::

        Tip text

    .. tabs::

        .. tab: First Tab

            Text or directives as you like

        .. tab: Last Tab

            Text or directives as you like

Add your files .rst as you liked, check that everything is correct in the documentation and then type:

Windows PowerShell

.. code::

    .\make.bat clean

Linux

.. code::

    make clean

Add to Read The Docs
--------------------
Quickstart for GitHub Hosted Projects. By the end of this quickstart, you will have a new project automatically updated when you push to GitHub.

- Create an account on `Read the Docs`_. You will get an email verifying your email address which you should accept within 7 days.
- Log in and click on ``Import a Project``.
- Click ``Connect to GitHub`` in order to connect your account's repositories to GitHub.
- When prompted on GitHub, give access to your account.
- Click ``Import a Repository`` and select any desired repository.
- Change any information if desired and click ``Next``.
- All done. Commit away and your project will auto update.

.. _Read the Docs: https://readthedocs.org