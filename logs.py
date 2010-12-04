#!/usr/local/bin/python

##############################################################################
# logs.py
# Base Log File Monitoring Library
#
# [2010-12-04] - kkelley: Cleaned up code posted to Google Code at
#                         http://code.google.com/p/moni/
# [2010-11-06] - kkelley: Initial Creation
#

##############################################################################
# Config

import cPickle
import hashlib
import os
import re
import time

##############################################################################
# Code

class Logs(object):
    def __init__(self):
        self.cache = {}
        self.filename = None
        self.pattern = None