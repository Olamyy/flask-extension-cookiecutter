======================
Flask Extension Cookiecutter
======================

Cookiecutter_ template for writing flask extensions.

* GitHub repo: https://github.com/Olamyy/flask-extension-cookiecutter/
* Documentation: https://github.com/Olamyy/flask-extension-cookiecutter/blob/master/README.rst
* Free software: MIT license

Features
--------
* Creating Main Extension Class
* Extension specific tests
* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4, 3.5
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Bumpversion_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate your extension by running::

    cookiecutter https://github.com/Olamyy/flask-extension-cookiecutter/

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Run the script `travis_pypi_setup.py` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your extension by pushing a new tag to master.


Not Exactly What You Want?
--------------------------
Check out

* `mitsuhiko/flask-extension-wizard`_: is a wizard that also helps create flask extensions.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this

.. _Travis-CI: http://travis-ci.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _PyPi: https://pypi.python.org/pypi

.. _`mitsuhiko/flask-extension-wizard`: https://github.com/mitsuhiko/flask-extension-wizard
