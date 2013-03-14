#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Keyboard language swithing, detection of current language, etc.

Author Andrew Terekhine
Since 2012-11-23
"""
import os
import Common
import Message
import SystemUtil

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

def switchLanguage():
    setLanguage(Common.SECOND_LANGUAGE if getLanguage() == Common.DEFAULT_LANGUAGE else Common.DEFAULT_LANGUAGE)

def getLanguage():
    return SystemUtil.getProcessOutput("setxkbmap -print | grep xkb_symbols | awk -F'+' '{print $2}'")

def setLanguage(language):
    Message.hint(language)
    os.popen("setxkbmap " + language)

def setDefaultLanguage():
    if getLanguage() != Common.DEFAULT_LANGUAGE:
        setLanguage(Common.DEFAULT_LANGUAGE)

def setSecondLanguage():
    if getLanguage() != Common.SECOND_LANGUAGE:
        setLanguage(Common.SECOND_LANGUAGE)