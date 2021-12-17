Developer Documentation
=======================

All components are hosted at Bitbucket. Development follows `CESSDA
Technical Guidelines`_.

All commits are tested in CESSDA CI Platform. The platform also
perfoms static analysis using pylint and SonarQube. All components
follow Python PEP8, with an exception in maximun line length. PEP8
mandates 80 characters for each line, but the components allow 120
characters for each line. This exception is reflected in ``.pylintrc``
files in each project's root.

Python dependencies are version locked for each component in
``requirements.txt`` files. Every install should use the versions
specified in order to maintain stability and security.

All components rely on `Kuha2`_ interfaces and they all depend on
Kuha2 Python packages.


.. _CESSDA Technical Guidelines: https://docs.tech.cessda.eu
.. _Kuha2: https://kuha2.readthedocs.io


DocStore HTTP API
-----------------

This is rendered from DocStore openapi.json. Use Swagger GUI for a
more complete rendering that includes examples and schemas of request
and response payloads.

.. openapi:: ext/cdcagg_docstore/openapi.json


Python API
----------

.. toctree::

   cdcagg_common <cdcagg_common_api>
   cdcagg_docstore <cdcagg_docstore_api>
   cdcagg_oai <cdcagg_oai_api>
   cdcagg_client <cdcagg_client_api>
