# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'CESSDA Metadata Aggregator'
copyright = '2021, Toni Sissala'
author = 'Toni Sissala'

# The full version, including alpha/beta/rc tags
release = '0.2.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # Autodoc renders api documentation from source code
    'sphinx.ext.autodoc',
    # Viewcode enable users to view code directly from documentation.
    'sphinx.ext.viewcode',
    # For MD support
    'myst_parser',
    'sphinxcontrib.openapi'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Autodoc options

autodoc_default_options = {
    'special-members': '__init__'
}


# -- Customized configuration for CDCAGG project ---------------------------

import os
import shutil
import filecmp
from glob import iglob
from pkg_resources import get_distribution

import cdcagg_common
import cdcagg_docstore
import cdcagg_oai
import cdcagg_client


HERE = os.path.abspath(__file__)


def _copy_docs_here(source_dir, sub_dir):
    """Copy .rst files recursively from `source_dir`.
    Place them into `sub_dir`.
    """
    if not os.path.isabs(source_dir):
        raise ValueError("source dir %s is not absolute path." % source_dir)
    if not os.path.exists(source_dir):
        raise ValueError("source dir %s does not exist." % source_dir)
    here_dir = os.path.dirname(HERE)
    if sub_dir.endswith(os.sep):
        # Make sure sub_dir does not end with os.sep
        sub_dir = sub_dir[:-1]

    def _copy_sourcepath_here(pathname):
        for sourcepath in iglob(pathname, recursive=True):
            source_relpath = sourcepath.replace(source_dir, "", 1)
            if source_relpath.startswith(os.sep):
                relpath = sub_dir + source_relpath
            else:
                relpath = os.path.join(sub_dir, source_relpath)
            targetpath = os.path.join(here_dir, relpath)
            targetdir = os.path.dirname(targetpath)
            if not os.path.exists(targetdir):
                os.makedirs(targetdir)
            if os.path.exists(targetpath):
                if not filecmp.cmp(sourcepath, targetpath):
                    print("Create file: %s" % targetpath)
                    shutil.copy(sourcepath, targetpath)
            else:
                print("Create file: %s" % targetpath)
                shutil.copy(sourcepath, targetpath)
    pathname = '{source}{sep}**{sep}*.rst'.format(source=source_dir,
                                                  sep=os.sep)
    _copy_sourcepath_here(pathname)
    pathname = '{source}{sep}**{sep}*.md'.format(source=source_dir,
                                                 sep=os.sep)
    _copy_sourcepath_here(pathname)
    pathname = '{source}{sep}LICENSE.txt'.format(source=source_dir,
                                                 sep=os.sep)
    _copy_sourcepath_here(pathname)
    pathname = '{source}{sep}openapi.json'.format(source=source_dir,
                                                  sep=os.sep)
    _copy_sourcepath_here(pathname)


_copy_docs_here(os.path.abspath(os.path.join(os.path.dirname(cdcagg_common.__file__), '..')),
                os.path.join('ext', 'cdcagg_common'))
_copy_docs_here(os.path.abspath(os.path.join(os.path.dirname(cdcagg_docstore.__file__), '..')),
                os.path.join('ext', 'cdcagg_docstore'))
_copy_docs_here(os.path.abspath(os.path.join(os.path.dirname(cdcagg_oai.__file__), '..')),
                os.path.join('ext', 'cdcagg_oai'))
_copy_docs_here(os.path.abspath(os.path.join(os.path.dirname(cdcagg_client.__file__), '..')),
                os.path.join('ext', 'cdcagg_client'))


cdcagg_common_version = get_distribution('cdcagg_common').version
cdcagg_oai_version = get_distribution('cdcagg_oai').version
cdcagg_docstore_version = get_distribution('cdcagg_docstore').version
cdcagg_client_version = get_distribution('cdcagg_client').version

rst_epilog = \
""".. |cdcagg_common_version| replace:: %s
.. |cdcagg_docstore_version| replace:: %s
.. |cdcagg_oai_version| replace:: %s
.. |cdcagg_client_version| replace:: %s
""" % (cdcagg_common_version,
       cdcagg_docstore_version,
       cdcagg_oai_version,
       cdcagg_client_version)
