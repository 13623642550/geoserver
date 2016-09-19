# -*- coding: utf-8 -*-
#
# GeoServer documentation build configuration file, created by
# sphinx-quickstart on Tue Oct 28 10:01:09 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default value; values that are commented out
# serve to show the default value.

import sys, os, string
   
# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#sys.path.append(os.path.abspath('some/directory'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.extlinks']

#todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['../../theme/_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General substitutions.
project = u'GeoServer'
manual = u'User Manual'
copyright = u'2016, Open Source Geospatial Foundation'

# The default replacements for |version| and |release|, also used in various
# other places throughout the built documents.
#
# The short X.Y version.
version = '2.10'
# The full version, including alpha/beta/rc tags.
release = '2.10-beta'
# Users don't need to see the "SNAPSHOT" notation when it's there
if release.find('SNAPSHOT') != -1:
   release = '2.10.x'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directories, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Options for extlinks
#
# :website:`license <License>`
# :geos:`1234`
# :wiki:`Proposals`
# -----------------------------------

extlinks = { 
    'wiki': ('https://github.com/geoserver/geoserver/wiki/%s',''),
    'website': ('http://geoserver.org/%s',''),
    'user': ('http://docs.geoserver.org/latest/en/user/%s',''),
    'developer': ('http://docs.geoserver.org/latest/en/developer/%s',''),
    'geos': ('https://osgeo-org.atlassian.net/browse/GEOS-%s','GEOS-'),
    'geot': ('https://osgeo-org.atlassian.net/browse/GEOT-%s','GEOT-')
}

# Common substitutions

rst_epilog = "\n" \
 ".. |install_directory_winXP| replace:: :file:`C:\Program Files\\\\GeoServer "+release+"`\n" \
 ".. |install_directory_win| replace:: :file:`C:\\\\Program Files (x86)\\\\GeoServer "+release+"`\n" \
 ".. |install_directory_linux| replace:: :file:`/var/lib/tomcat7/webapps/geoserver`\n" \
 ".. |install_directory_mac| replace:: :file:`/Applications`\n" \
 ".. |data_directory_winXP| replace:: :file:`C:\Program Files\\\\GeoServer "+release+"\\\\data_dir`\n" \
 ".. |data_directory_win| replace:: :file:`C:\\\\Program Files (x86)\\\\GeoServer "+release+"\\\\data_dir`\n" \
 ".. |data_directory_linux| replace:: :file:`/var/lib/tomcat7/webapps/geoserver/data`\n" \
 ".. |data_directory_mac| replace:: :file:`/Applications/GeoServer.app/Contents/Resources/Java/data_dir`"

# Options for HTML output
# -----------------------
html_theme = 'geoserver'
html_theme_path = ['../../themes']

if os.environ.get('HTML_THEME_PATH'):
  html_theme_path.append(os.environ.get('HTML_THEME_PATH'))

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
#html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + " " + release + " " + manual

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '../../themes/geoserver/static/geoserver.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['../../theme/_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'GeoServerUserManual'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', 'GeoServerUserManual.tex', u'GeoServer User Manual',
   u'GeoServer', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '../../themes/geoserver/static/GeoServer_500.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
latex_elements = {
  'fontpkg': '\\usepackage{palatino}',
  'fncychap': '\\usepackage[Sonny]{fncychap}',
'preamble': #"""\\usepackage[parfill]{parskip}
  """
	\\hypersetup{
		colorlinks = true,
    linkcolor = [rgb]{0,0.46,0.63},
    anchorcolor = [rgb]{0,0.46,0.63},
    citecolor = blue,
    filecolor = [rgb]{0,0.46,0.63},
    pagecolor = [rgb]{0,0.46,0.63},
    urlcolor = [rgb]{0,0.46,0.63}
	}

	
"""
}

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
