#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Starts incremental search in emacs.

Author Andrew Terekhine
Since 2011-11-23
"""

import Common
import os
import KeyboardUtil
import SendToUi
import locale
import SystemUtil

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

BOOKMARK = "a r c h"

def open():
    Common.openProcessWithTitleCheck("emacs", "Dropbox/config/emacs/com.txt.gpg", "Starting emacs",
        "~/Dropbox/config/emacs/com.txt.gpg")

def scanForKeyword():
    SendToUi.sendKey("Control+Home Control+e underscore underscore")

def search(keyword):
    KeyboardUtil.setDefaultLanguage()
    open()
    scanForKeyword()
    if keyword != "":
        SendToUi.sendKey(keyword)

def startSearch():
    search("")

def toInbox():
    search("i n b o x")

def toInboxHome():
    search("i n b o x h o m e")

def toInboxWeek():
    search("i n b o x w e e k")

def toInboxMonth():
    search("i n b o x m o n t h")

def toInboxYear():
    search("i n b o x y e a r")

def toPlan():
    search("p l a n")

def toBookmark():
    search(BOOKMARK)