#
# conf.py
#
# Copyright The GOLDS-UFSC Contributors.
#
# GOLDS-UFSC Documentation
#
# This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
# International License. To view a copy of this license,
# visit http://creativecommons.org/licenses/by-sa/4.0/.
#
#

import sys
import ast

# Project information
project     = 'golds-ufsc'
copyright   = 'The GOLDS-UFSC Contributors'
author      = 'SpaceLab'
release     = 'rev C'
title       = 'GOLDS-UFSC'
doc_id      = 'SpaceLab.DMO.2020.06.001'

# General configuration
numfig = True

extensions = ['sphinxcontrib.bibtex', 'sphinx_subfigure']

# Path to your .bib file
bibtex_bibfiles = ['references.bib']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Identify the Sphinx builder being used
if '-b' in sys.argv:
    builder = sys.argv[sys.argv.index('-b') + 1]
elif '-M' in sys.argv:
    builder = sys.argv[sys.argv.index('-M') + 1]
else:
    builder = 'html'  # default builder

# Exclude the PDF-specific index from the HTML build
if builder in ['html', 'dirhtml']:
    exclude_patterns.append('pdf-index.rst')

# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "_static/golds-ufsc-mission-patch.png"
html_theme_options = {
    'logo_only': True,
}

# Navigation bar title
html_title = "GOLDS-UFSC Documentation"
html_short_title = "GOLDS-UFSC Documentation"

# PDF output configuration
latex_documents = [
    (
        'pdf-index',                        # Root document (e.g., 'index' or 'pdf-index')
        doc_id + '-' + release.replace(' ', '-') + '.tex',    # Output LaTeX file name (no spaces)
        title,                              # Document title (can be empty to use the root doc's title)
        author,                             # Author name(s).
        'manual',                           # Document type: 'manual' or 'howto'
        True,                               # toctree_only: if True, only include docs in toctree
    ),
]

latex_toplevel_sectioning = 'chapter'
latex_show_pagerefs = True
latex_show_urls = 'footnote'

# Replace with the path to your local override file
latex_elements_file = "latex/latex_elements_custom.txt"

latex_elements = dict()

with open(latex_elements_file, "rt") as file:
    latex_config = file.read()
    if latex_elements == {}:
      latex_elements = ast.literal_eval(latex_config)

latex_additional_files = [
    'latex/spacelab_book.sty',
    'figures/by-sa.pdf',
    'figures/spacelab-logo-full-color-rgb-1000px@72ppi.png',
]
latex_appendices = ['link_budget', 'packets', 'edc_report']
