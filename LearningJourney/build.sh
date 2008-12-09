#!/usr/bin/env python

buildout_url = "http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py"

import urllib
import os

if not os.path.exists('bootstrap.py'):
    f = urllib.urlopen(buildout_url)
    out = open('bootstrap.py','w')
    out.write(f.read())

import bootstrap
