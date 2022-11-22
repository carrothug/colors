import os
import sys

sys.path.insert(
    0, os.path.abspath("../../src/colors")
)  # Source code dir relative to this file


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "colors"
copyright = "2022, jj"
author = "jj"
release = "0.4"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Core library for html generation from docstrings
    "sphinx.ext.autosummary",  # Create neat summary tables
]

autosummary_generate = True  # Turn on sphinx.ext.autosummary

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
