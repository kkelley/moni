#!/usr/bin/env python

##############################################################################
# logs.py
# Base Log File Monitoring Library
#
# [2010-12-25] kkelley: Added 'buildBlock' and 'scanBlock' functions.
#   Removed 'scanFile' function. Updated 'runTest'.
#   function.
# [2010-12-04] kkelley: Cleaned up code posted to Google Code at
#   http://code.google.com/p/moni/
# [2010-11-06] kkelley: Initial Creation

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
    def __init__(self, config):
        self.ConfigKeys = ('Debug', 'Logger', 'File', 'FileCache', 'Filename', 'SearchString')

        self.File = None
        self.FileCache = None
        self.FileData = None
        self.Filename = None
        self.Filesize = None
        self.MessageBlock = None
        self.Pattern = None
        self.SearchString = None

        self.Debug = False
        self.Logger = None

        if type(config) is not dict:
            return ('0001', "Configuration data is invalid. Please see README.txt")
        if len(config) < 2:
            return ('0001', "Configuration data is invalid. Please see README.txt")

        for key in self.ConfigKeys:
            try:
                exec("self.%s = config['%s']")
            except:
                continue

    def checkFilesize(self):
        def getFilesize(fn):
            try:
                fs = os.path.getsize(fn)
                return fs
            except OSError, msg:
                return ('0034',  "Unable to get the size of file %s - %s" % (fn, msg))

        if self.Filename is not None:
            fs = getFilesize(self.Filename)
            if fs is tuple:
                return fs
            else:
                self.Filesize = fs
        else:
            return ('0012', "No filename specified.")

    def buildPattern(self):
        if self.SearchString is None:
            return ('0023', "No search string(s) specified.")

        if type(self.SearchString) is list:
            if len(self.SearchString) > 1:
                self.SearchString = "|".join(self.SearchString)
            elif len(self.SearchString) < 1:
                return ('0023', "No search string(s) specified.")
            else:
                self.SearchString = self.SearchString[0]

        self.Pattern = re.compile(self.SearchString)

    def openFile(self):
        if self.Filename is not None:
            try:
                self.File = open(self.Filename, 'r')
            except IOError, msg:
                return ('0010', "Unable to open file: %s - %s" % (self.Filename, msg))
        else:
            return ('0012', "No filename specified")

    def loadFile(self):
        if self.File is not None:
            self.FileData = self.File.readlines()
        else:
            err = self.openFile()
            if err:
                return err

    def parseDate(self, line):
        pass

    def buildBlock(self):
        if self.FileData is not None:
            self.MessageBlock = []
            for line in FileData:
                if self.parseDate(line):
                    self.MessageBlock.append(line)

    def scanBlock(self, Message):
        pass

    def runTest(self):
        if self.Pattern is not None:
            pass

        if self.MessageBlock is not None:
            if len(self.MessageBlock) > 0:
                for Message in self.MessageBlock:
                    self.scanBlock(Message)

##############################################################################
# if __main__

if __name__ == "__main__":
    log_config = {}
    log_config['filename'] = "test.txt"
    log_config['search'] = ["string 1", "string 2"]

    r = Logs(config)
    r.openFile(filename)
    r.loadFile()
