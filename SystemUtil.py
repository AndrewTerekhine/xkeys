#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Set of system utils.

Author Andrew Terekhine
Since 2011-11-23
"""
import os
import subprocess
import string
import ClipboardUtil
import SendToUi
import Message
import Common
import SendToUi

"""
Gets window name by process id
"""
def getWindowNameByProcessId(processId):
    windowName = os.popen("wmctrl -l -p | grep '" + processId + "'").read().rstrip()
    return windowName

def getSelection():
    storedClipboard = SendToUi.beforeSetClipboard()
    text = ClipboardUtil.pasteFromClipboardXsel()
    SendToUi.afterSetClipboard(storedClipboard)
    return text

def getUserFolder():
    return os.getenv("HOME")

def transformUrlBeforeOpen(url):
    url = string.strip(url) # strips leading and trailing white spaces
    if string.find(url, Common.WWW_PREFIX) == 0:
        url = Common.HTTP_PREFIX + url
    if string.find(url, Common.USER_FOLDER_PREFIX) == 0:
        url = string.replace(url, Common.USER_FOLDER_PREFIX, getUserFolder())

    # todo add customization
    if string.find(url, "D:\Dropbox") == 0:
        url = string.replace(url, "D:\Dropbox", "Dropbox")
        url = string.replace(url, "\\", "/")
    return url

def openSelection(app, url):
    text = getSelection()
    url = transformUrlBeforeOpen(url + text)
    subprocess.Popen([app, url])
    return None

def runSelection():
    text = getSelection()

    common = transformUrlBeforeOpen(text)

    subprocess.Popen(common, shell=True)
    return None

def getProcessOutput(commandText):
    return os.popen(commandText).read().rstrip()
