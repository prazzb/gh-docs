project = 'Doc'
copyright = '2026,prazzb'
author = 'prazzb'

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosectionlabel',
]

html_theme = "sphinx_rtd_theme"
html_show_sourcelink = False # disable rest source of these files
html_show_sphinx = False # do not show created by sphinx
html_show_copyright = False # do not show copyright
todo_include_todos = True # include todos

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
