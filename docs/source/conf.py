# Configuration file for the Sphinx documentation builder.
import sys
import os
# -- Project information

project = 'ORCA'
copyright = '2023, Idaho National Laboratory'
author = ''

release = '0.1'
version = '0.1.0'

#These directories need to be added to the path for sphinx to find the docstrings therein
sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../tests"))
sys.path.insert(0, os.path.abspath("../../tests/data"))
sys.path.insert(0, os.path.abspath("../../tests/Optimization"))
sys.path.insert(0, os.path.abspath("../../tests/RewardForecast"))
# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.plantuml',
    'sphinx_needs',
]

# make everyone provide an ID for their requirements
#needs_id_required = True
# the ID must match this regex
#needs_id_regex = "^[A-Z0-9_]{5,}"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
