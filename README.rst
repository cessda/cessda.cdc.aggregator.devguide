CESSDA Metadata Aggregator Documentation
========================================

ReadTheDocs compatible documentation for CESSDA Metadata Aggregator (CDC Aggregator).


Development install & serve
---------------------------

Developed in Ubuntu 20.04 with Python 3.8.

.. code-block::

   pip install -r requirements.txt
   pip install sphinx-autobuild
   rm -r docs/_build/ && sphinx-autobuild --host 0.0.0.0 --port 6543 docs/ docs/_build
