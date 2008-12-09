#!/bin/sh

URL="http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py"

wget $URL

/usr/bin/env python ./bootstrap.py
