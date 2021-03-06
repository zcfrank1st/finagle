# -*- coding: utf-8 -*-
#
# Documentation config
#

import sys, os

sys.path.append(os.path.abspath('exts'))
sys.path.append(os.path.abspath('utils'))

import sbt_versions

# highlight_language = 'scala'
highlight_language = 'text'  # this way we don't get ugly syntax coloring
extensions = ['sphinx.ext.extlinks', 'includecode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['metrics/*', 'shared-modules/*']

sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'flask'
html_short_title = 'Finagle'
html_static_path = ['_static']
html_sidebars = {
   'index':    ['sidebarintro.html', 'searchbox.html'],
    '**':      ['sidebarlogo.html', 'sidebarintro.html', 'localtoc.html', 'relations.html',
                'searchbox.html']
}
html_theme_options = {
  'index_logo': None
}

# These don't seem to work?
html_use_smartypants = True
html_show_sphinx = False
html_style = 'finagle.css'

project = u'Finagle'
copyright = u'2016 Twitter, Inc'
htmlhelp_basename = "finagle"
release = sbt_versions.find_release(os.path.abspath('../../../project/Build.scala'))
version = sbt_versions.release_to_version(release)

# e.g. :issue:`36` :ticket:`8`
extlinks = {
  'issue': ('https://github.com/twitter/finagle/issues/%s', 'issue #'),
  'ex': ('https://github.com/twitter/finagle/blob/finagle-example/src/main/scala/%s', 'Finagle example '),
  'api': ('http://twitter.github.io/finagle/docs/#%s', ''),
  'util': ('http://twitter.github.io/util/docs/#%s', ''),
  'util-stats-src':("https://github.com/twitter/util/blob/master/util-stats/src/main/scala/%s", 'util-stats github repo'),
  'util-core-src':("https://github.com/twitter/util/blob/master/util-core/src/main/scala/%s", 'util-core github repo'),
  'finagle-mux-src':("https://github.com/twitter/finagle/blob/master/finagle-mux/src/main/scala/%s", 'finagle-mux github repo'),
  'finagle-http-src':("https://github.com/twitter/finagle/blob/master/finagle-http/src/main/scala/%s", 'finagle-http github repo'),
  'finagle-thriftmux-src':("https://github.com/twitter/finagle/blob/master/finagle-thriftmux/src/main/scala/%s", 'finagle-thriftmux github repo'),
  'src':("https://github.com/twitter/finagle/blob/master/finagle-core/src/main/scala/%s", 'finagle-core github repo')
}

rst_epilog = '''
.. _Finagle Examples: https://github.com/twitter/finagle/tree/finagle-example
'''

pygments_style = 'flask_theme_support.FlaskyStyle'

# fall back if theme is not there
try:
    __import__('flask_theme_support')
except ImportError, e:
    print '-' * 74
    print 'Warning: Flask themes unavailable.  Building with default theme'
    print 'If you want the Flask themes, run this command and build again:'
    print
    print '  git submodule update --init'
    print '-' * 74

    pygments_style = 'tango'
    html_theme = 'default'
    html_theme_options = {}
