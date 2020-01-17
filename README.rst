datacoco-batch
=================

.. image:: https://badge.fury.io/py/datacoco-batch.svg
    :target: https://badge.fury.io/py/datacoco-batch
    :alt: PyPI Version

.. image:: https://api.codacy.com/project/badge/Grade/36df276fb1fe47d18ff1ea8c7a0aa522
    :target: https://www.codacy.com/manual/equinoxfitness/datacoco-batch?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=equinoxfitness/datacoco-batch&amp;utm_campaign=Badge_Grade
    :alt: Code Quality Grade

.. image:: https://api.codacy.com/project/badge/Coverage/36df276fb1fe47d18ff1ea8c7a0aa522
    :target: https://www.codacy.com/manual/equinoxfitness/datacoco-batch?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=equinoxfitness/datacoco-batch&amp;utm_campaign=Badge_Coverage
    :alt: Coverage

.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
    :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg
    :target: https://github.com/equinoxfitness/datacoco-batch/blob/master/CODE_OF_CONDUCT.rst
    :alt: Code of Conduct

Batch is a simple interface for managing the state of jobs and workflows in batchy microservice.

Installation
------------

datacoco-batch requires Python 3.6+

::

    python3 -m venv <virtual env name>
    source <virtual env name>/bin/activate
    pip install datacoco-batch

Quickstart
----------

::

    self.batchy = Batch(
                wf=test_workflow,
                server="server.com",
                port="80",
            )

    self.batchy.open()

    self.batchy.get_status()

    self.batchy.close()

Sample output

::

    {
        "global": {
            "batch_id": "123456789",
            "status": "success",
            "failure_cnt": 0,
            "open_cnt": 2,
            "batch_start": "2020-01-17T06:58:01.234567",
            "batch_end": "2020-01-17T07:18:08.012345"
            }
        }

Development
-----------

Getting Started
~~~~~~~~~~~~~~~

It is recommended to use the steps below to set up a virtual environment for development:

::

    python3 -m venv <virtual env name>
    source <virtual env name>/bin/activate
    pip install -r requirements.txt

Testing
~~~~~~~

::

    pip install -r requirements-dev.txt

To run the testing suite, simply run the command: ``tox`` or ``python -m unittest discover tests``

Contributing
------------

Contributions to datacoco\_batch are welcome!

Please reference guidelines to help with setting up your development
environment
`here <https://github.com/equinoxfitness/datacoco-batch/blob/master/CONTRIBUTING.rst>`__.