# Configuration file for the Sphinx documentation builder.
import sys
import os
# -- Project information

project = 'ORCA'
copyright = '2024, Idaho National Laboratory'
author = ''

release = '0.1'
version = '0.1.0'

#These directories need to be added to the path for sphinx to find the docstrings therein
# 
sys.path.insert(0, os.path.abspath(os.path.join('..', '..')))

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
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

# turn on autosummary option
autosummary_generate = True 

# -- Options for EPUB output
epub_show_urls = 'footnote'

# tell autodoc not to import the dependencies when making the documentation
# note: these dependencies were manually copied.  There should be a better way...
autodoc_mock_imports = [
    "anyio",
    "argon2-cffi",
    "argon2-cffi-bindings",
    "asttokens",
    "attrs",
    "backcall",
    "backports.functools-lru-cache",
    "beautifulsoup4",
    "bleach",
    "certifi",
    "cffi",
    "colorama",
    "comm",
    "contourpy",
    "cycler",
    "debugpy",
    "decorator",
    "defusedxml",
    "entrypoints",
    "exceptiongroup",
    "executing",
    "fastjsonschema",
    "flit_core",
    "FMPy",
    "fonttools",
    "gekko",
    "idna",
    "imageio",
    "imageio-ffmpeg",
    "importlib-metadata",
    "importlib-resources",
    "ipykernel",
    "ipython",
    "ipython-genutils",
    "ipywidgets",
    "jedi",
    "Jinja2",
    "jsonschema",
    "jupyter",
    "jupyter_client",
    "jupyter-console",
    "jupyter_core",
    "jupyter-events",
    "jupyter_server",
    "jupyter_server_terminals",
    "jupyterlab-pygments",
    "jupyterlab-widgets",
    "kiwisolver",
    "lark",
    "lxml",
    "MarkupSafe",
    "matplotlib",
    "matplotlib-inline",
    "mistune",
    "msgpack",
    "munkres",
    "nbclassic",
    "nbclient",
    "nbconvert",
    "nbformat",
    "nest-asyncio",
    "notebook",
    "notebook_shim",
    "numpy",
    "overrides",
    "packaging",
    "pandas",
    "pandocfilters",
    "parso",
    "pickleshare",
    "Pillow",
    "pip",
    "pkgutil_resolve_name",
    "platformdirs",
    "ply",
    "prometheus-client",
    "prompt-toolkit",
    "psutil",
    "pure-eval",
    "pycparser",
    "pydmd",
    "Pygments",
    "pyomo",
    "pyparsing",
    "PyQt5",
    "PyQt5-sip",
    "pyrsistent",
    "pyserial",
    "python-dateutil",
    "python-json-logger",
    "pytz",
    "pywin32",
    "pywinpty",
    "PyYAML",
    "pyzmq",
    "qtconsole",
    "QtPy",
    "rfc3339-validator",
    "rfc3986-validator",
    "scipy",
    "Send2Trash",
    "setuptools",
    "sip",
    "six",
    "sniffio",
    "soupsieve",
    "stack-data",
    "tclab",
    "terminado",
    "tinycss2",
    "toml",
    "tomli",
    "tornado",
    "traitlets",
    "typing_extensions",
    "typing-utils",
    "tzdata",
    "unicodedata2",
    "wcwidth",
    "webencodings",
    "websocket-client",
    "wheel",
    "widgetsnbextension",
    "zipp",
]
