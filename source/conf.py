# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'template-intergrated'
copyright = '2025, brucekomike'
author = 'brucekomike'
release = 'v0.1.0'
language='en'
# 'en' 'jp' 'zh_CN'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_inline_tabs",
"sphinxext.opengraph",
'sphinx_copybutton',
'myst_parser',
'sphinx.ext.githubpages',
]
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
source_suffix = {
   '.rst': 'restructuredtext',
   '.txt': 'markdown',
   '.md': 'markdown',
   '': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'Makefile', 
  '.gitignore', '.gitattributes', '.git',
  '*.py', '*.bat', '*.sh', 
  'requirements.txt', '*venv', 
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = "frameworker doc"
html_last_updated_fmt = ''
html_css_files = [
        "footer.css",
]
html_theme_options = {
    "source_repository": "https://github.com/brucekomike/frameworker-docs",
    "source_branch": "main",
    "source_directory": "source/",
    "navigation_with_keys": True,
}
html_logo = '_static/frameworker.svg'
html_favicon = '_static/frameworker.svg'
