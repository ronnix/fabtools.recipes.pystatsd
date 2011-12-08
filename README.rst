Description
===========

`Fabric <http://fabfile.org/>`_ task to install `pystatsd <http://github.com/sivy/py-statsd>`_, using `fabtools <http://github.com/ronnix/fabtools>`_.

How to use
==========

Import the task in your project's ``fabfile.py`` to make it available::

    from fabtools.recipes.pystatsd import install_pystatsd

Then you can call it from the ``fab`` command::

    fab install_pystatsd
