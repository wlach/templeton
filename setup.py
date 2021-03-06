# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is templeton.
#    
# The Initial Developer of the Original Code is
# Mozilla foundation
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Mark Cote <mcote@mozilla.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import sys
from setuptools import setup

version = '0.6'

deps = ['web.py', 'tempita', 'python-daemon', 'which']

if sys.version < '2.5' or sys.version >= '3.0':
    print >>sys.stderr, '%s requires Python >= 2.5 and < 3.0' % _PACKAGE_NAME
    sys.exit(1)

try:
    import json
except ImportError:
    deps.append('simplejson')

setup(name='templeton',
      version=version,
      description="Minimal web framework for rapid development of web tools",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Mark Cote',
      author_email='mcote@mozilla.com',
      url='https://github.com/markrcote/templeton',
      license='MPL',
      scripts=['scripts/templeton',
               'scripts/templetond',
               'scripts/templeton.fcgi'],
      packages=['templeton'],
      package_data={'templeton': ['templates/project/html/*',
                                  'templates/project/server/*',
                                  'templates/server/*',
                                  'server/scripts/*',
                                  'server/style/*css',
                                  'server/style/Aristo/*css',
                                  'server/style/Aristo/images/*']},
      include_package_data=True,
      zip_safe=False,
      install_requires=deps,
      )
