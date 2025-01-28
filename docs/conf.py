# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html



import os
import sys
sys.path.insert(0, os.path.abspath('../'))


code_path = os.path.join(os.path.dirname(__file__), "../", "module1/")
sys.path.append(code_path)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Accelerate'
copyright = '2025, Accelerate Team'
author = 'Accelerate Team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.plantuml',
    'sphinxcontrib.apidoc',
    'sphinx_needs',
    'sphinx.ext.napoleon',
    'sphinx_epytext'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Python doc extensions
# See https://github.com/sphinx-contrib/apidoc/blob/master/README.rst
apidoc_module_dir = '..'
apidoc_output_dir = 'python-doc'
apidoc_toc_file = False
# apidoc_excluded_paths = ['tests']
# apidoc_separate_modules = True

needs_types = [dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"),
               dict(directive="component", title="Specification", prefix="C_", color="#FEDCD2", style="node"),
               dict(directive="impl", title="Implementation", prefix="I_", color="#DF744A", style="node"),
               dict(directive="arch", title="Architecture", prefix="A_", color="#D2244A", style="node")
           ]


needs_extra_options = ['jira']

needs_string_links = {
    
    # Links to the related jira issue
    'jira_link': {
        'regex': r'^(?P<value>\w+)$',
        'link_url': 'https://useblocks.atlassian.net/browse/ADAS-{{value}}',
        'link_name': 'JIRA ADAS #{{value}}',
        'options': ['jira']
    }
}

needs_extra_links = [
   {  # impl -> arch
      "option": "implements",
      "incoming": "implemented_by",
      "outgoing": "implements",
   },
   {  # impl ->req, arch->req
      "option": "fulfil",
      "incoming": "fulfilled by",
      "outgoing": "fulfils",
   }
]