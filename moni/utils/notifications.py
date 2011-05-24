#!/usr/bin/env python

##############################################################################
# notifications.py
# Base notifications library
#
# [2010-11-06] kkelley: Initial Creation

##############################################################################
# Config

import cStringIO
import smtplib
import time

##############################################################################
# Code

class Notification(MoniBase):
    def __init__(self):
        self.x = y


class EmailNotification(Notification):
    def __init__(self):
        self.HEADERS = None
        self.TO = None
        self.CC = None
        self.REPLYTO = None
        self.FROM = None
        self.SUBJECT = None
        self.BODY = None
        self.EMAIL = None
        self.MAILSERVER = None
        self.SMTP = None

    def BuildHeaders(self):
        to = self.TO
        cc = self.CC
        reto = self.REPLYTO
        from = self.FROM
        subj = self.SUBJECT

        if type(to) != type([]):
            to = [to]

        if cc is not None:
            if type(cc) != type([]):
                cc = [cc]

            head_to = "To: %s\r\nCc: %s" % ((', '.join(to)), (', '.join(cc)))

            to = set(to + cc)
        else:
            head_to = "To: %s" % (', '.join(to))

        head_from = "From: %s" % (from)
        head_reto = "Reply-To: %s" % (reto)
        head_subj = "Subject: %s" % (subj)
        head_date = "Date: %s" % time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))

        headers = '\r\n'.join([head_from, head_reto, head_to, head_subj, head_date])

        self.TO = to
        self.HEADERS = headers

    def BuildEmail(self):
        s = cStringIO.StringIO()
        s.write('%s\r\n' % (self.HEADERS))
        s.write('%s\n' % (self.BODY))

        self.EMAIL = s

    def OpenSMTPConnection(self):
        if self.MAILSERVER is not None:
            smtp = smptlib.SMTP(self.MAILSERVER)
        else:
            smtp = None

        self.SMTP = smtp

    def CloseSMTPConnection(self):
        if self.SMTP is not None:
            self.SMTP.quit()
            self.SMTP = None

    def SendEmailNotification(self):
        if self.SMTP is None:
            self.OpenSMTPConnect()

        if self.HEADERS is None:
            self.BuildHeaders()

        if self.EMAIL is None:
            self.BuildEmail()

        self.SMTP.sendmail(self.FROM, self.TO, self.EMAIL.getvalue())
