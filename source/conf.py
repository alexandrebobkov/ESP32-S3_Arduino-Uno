# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ESP32-S3 Arduino Uno'
copyright = '2026, Alexander Bobkov'
author = 'Alexander Bobkov'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_simplepdf",
]
#pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Alexander Bobkov'),]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
#'alabaster'
html_static_path = ['_static']

# -- Options for simplepdf output --------------------------------------------
#simplepdf_css = '_static/simplepdf_alex.css'
simplepdf_coverpage = True
simplepdf_toc_depth = 3
simplepdf_title = 'ESP32-S3 Arduino Uno DevBoard'
simplepdf_author = 'Alexander B'
simplepdf_file_name = 'ESP32-S3_Arduino-Uno.pdf'
simplepdf_vars = {
#    'cover-overlay': '#047e2c',
#    'cover-bg': "#034b1b",
#    'primary-opaque': 'rgba(26, 150, 26, 0.8)',
    'primary': "#1A961A",
    'secondary': "#379683",
    'cover-bg': 'url(cover-bg.jpg) no-repeat center',
#   'cover-bg': 'url(ESP32C3_Breadboard-Adapter.jpg) no-repeat center',
    'cover': "#EC4A0A",
    'links': "#790000",
    'bottom-center-content': '"Building Your Custom-Made ESP32-S3 Development Board"',
    'bottom-right-content': '"Alexander B"',
}
