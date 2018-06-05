`Pullrequest-cli`_
==================

A command line program in python. Lets you collect all pull requests
assigned to you

Installation
------------

You can install it using pip

::

   pip install pullrequest-cli

or

You can clone the repository

::

   git clone https://bookinman@bitbucket.org/bookinman/pullrequest-cli.git

Then in the project directory

::

   pip install -e .

Usage
-----

The Pullrequest-cli can be invoked with ``pullrequest-cli`` command:

::

   pullrequest-cli <username> <repository-name> [options]

.. figure:: https://image.ibb.co/n27QtJ/usage.gif
   :alt: Usage Example

   Usage Example

Positional arguments:
~~~~~~~~~~~~~~~~~~~~~

-  ``username`` - Bitbucket username
-  ``repository`` - Bitbucket repository name

Optional arguments:
~~~~~~~~~~~~~~~~~~~

-  ``-h`` or ``--help`` - Help message
-  ``--password <PASSWORD>`` or ``-p <PASSWORD>`` - Your bitbucket
   account password. For private repositories only
-  ``--browser`` or ``-b`` - Open in browser

.. _Pullrequest-cli: https://libraries.io/pypi/pullrequest-cli