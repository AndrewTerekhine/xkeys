#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sends series of characters to UI. Based on xdotool. This tool must be installed.
This class uses fastest way: clipboard and xdotool.

Author Andrew Terekhine
Since 2011-11-23
"""
import os
import datetime
import sys
import ClipboardUtil
import time
import KeyboardUtil
import Message
from ClipboardUtil import pasteFromClipboardXsel, copyToClipboardXclip
from Tkinter import Tk
import tkSimpleDialog
import Common

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

def sendText(text):
    """
    Sends series of characters to any UI control. Uses fastest way: usage of clipboard and xdotool.
    """
    from subprocess import Popen, PIPE
    client = Popen(['xclip', '-selection', 'clipboard'], stdin=PIPE)
    client.stdin.write(text)
    client.stdin.close()
    client.wait()
    os.popen('xdotool key Shift+Insert')

def sendKey(keyName):
    """
    Sends a key
    """
    os.popen('xdotool key ' + keyName)

def keyWithClearModifiers(keyName):
    """
    Clear active modifiers if anyand sends a key
    """
    os.popen('xdotool key --clearmodifiers' + keyName)

def isoDate():
    """
    Sends a date in ISO format
    """
    time.sleep(0.1) # wait a little in order to be sure that user not pressing a hotkey anymore
    output = datetime.datetime.now().strftime("%Y-%m-%d")
    storedClipboard = ClipboardUtil.pasteFromClipboardXsel()
    sendText(output)
    ClipboardUtil.copyToClipboardXclip(storedClipboard)

def beforeSetClipboard():
    storedClipboard = pasteFromClipboardXsel()
    #SendToUi.key("Control") # since the control key could be already pressed by calling shortcut we need to release it
    time.sleep(0.1)

    # emacs processing
    # this triggers a custom macro in emacs - if nothing is selected it selects the whole line otherwise do nothing
    if Common.isAtiveTitle(Common.EMACS_TITLE):
        sendKey("Control+t")

    sendKey("Control+Insert")
    return storedClipboard


def afterSetClipboard(storedClipboard):
    copyToClipboardXclip(storedClipboard)

def hi():
    KeyboardUtil.setDefaultLanguage()
    storedClipboard = beforeSetClipboard()
    sendText("Hi ,")
    sendKey("Return Return Return Return")
    sendText("Regards,")
    sendKey("Return")
    sendText(Common.NAME)
    sendKey("Up Up Up Up Up End Left")
    afterSetClipboard(storedClipboard)

def newTask():
    """
    Sends a task template
    """
    KeyboardUtil.setDefaultLanguage()
    output = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    Tk().withdraw()
    text = tkSimpleDialog.askstring('Task category', 'Category::')

    if text is None or text == "": sys.exit()

    #works as well
    #time.sleep(0.24)
    #output = system.exec_command("date +%Y%m%d%H%M%S")
    #time = output.stdout.readline()
    storedClipboard = ClipboardUtil.pasteFromClipboardXsel()
    sendText("task " + text + "\n" + "    " + output + " " +  "\n\n" + "solution" + "\n\n" + "info" + "\n\n" + "keywords")
    sendKey("Home Up Up Up Up Up Up End")
    ClipboardUtil.copyToClipboardXclip(storedClipboard)

#todo place a correct call to xbindkeys config
def sendKeyAltSpace():
    sendKey("alt+space")