import os
from os import path
import sys
root = path.realpath(path.join(path.dirname(__file__), '..', '..'))
sys.path.insert(1, root)

copyright = '2020, Hypernet Labs'
extensions = ['sphinx.ext.extlinks', 'sphinxcontrib.redoc']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'sphinx'

redoc = [
    {
        'name': 'Galileo API Documentation',
        'page': 'index',
        'spec': 'https://api.galileoapp.io/galileo/user_interface/v1/openapi.yaml',
        'opts': {
            'lazy-rendering': True,
            'suppress-warnings': True,
            'expand-responses': [200]
        },
    },
]

if not os.environ.get('READTHEDOCS') == 'True':
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Unfortunately, Sphinx doesn't support code highlighting for standard
# reStructuredText `code` directive. So let's register 'code' directive
# as alias for Sphinx's own implementation.
#
# https://github.com/sphinx-doc/sphinx/issues/2155
from docutils.parsers.rst import directives
from sphinx.directives.code import CodeBlock
directives.register_directive('code', CodeBlock)
