********************************
Datacoco Batch
********************************

Getting started with Datacoco Batch

.. image:: https://img.shields.io/pypi/v/datacoco-batch.svg
   :target: https://pypi.python.org/pypi/datacoco-batch
   :alt: Pypi Version
.. image:: https://travis-ci.org/readthedocs/datacoco-batch.svg?branch=master
   :target: https://travis-ci.org/readthedocs/datacoco-batch
   :alt: Build Status
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
  :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

Batch is a simple interface for managing the state of jobs and workflows in batchy microservice.

Local setup
============

::

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements-dev.txt

Please install `pre-commit <https://pre-commit.com>`__ git hooks to use
`Black <https://black.readthedocs.io/en/stable/>`__ autoformatting and
flake8 PEP8 validations by running:

::

    pre-commit install


Tests
============
To run the testing suite, the following commands are required:

.. code-block:: console

  pip install -r requirements-dev.txt
  tox
