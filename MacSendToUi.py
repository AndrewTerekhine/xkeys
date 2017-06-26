#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sends series of characters to UI. Mac version. Based on applescript.

Author Andrew Terekhine
Since 2014-11-23
"""
import os
import string
import time

import MacClipboardUtil
import MacCommon
import MacUtil
import SystemUtil

if SystemUtil.isMac():
    import applescript

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

def sendUnicodeTextAsKeyCodes(text):
    if len(text) == 0:
        return
    text = text.strip()
    command = "\nkeystroke \""
    for c in text:
        command += ("0x" + hex(ord(c))[2:].zfill(4))
    content = "tell application \"System Events\"" + command + "\" using option down\n end tell"
    script = applescript.AppleScript(content)
    script.run()

def sendTextAndSpacesAsKeyCodes(text):
    if len(text) == 0:
        return
    text = "\nkeystroke \"" + string.replace(text.strip(), " ", "\"\nkey code 49\nkeystroke \"") + "\"\n"
    content = "tell application \"System Events\"" + text + "end tell"
    script = applescript.AppleScript(content)
    script.run()

def sendText(text):
    content = "tell application \"System Events\"\nkeystroke \"" + text + "\"\nend tell"
    script = applescript.AppleScript(content)
    script.run()

def sendGeneratedPassword():
    """
    Sends an auto generated password
    """
    text = os.popen("openssl rand -base64 8 |md5 |head -c10;echo").read()
    sendText(text)

def newTask():
    """
    Sends a task template
    """
    output = MacUtil.timeStamp()

    text = "task\n" + output + "  \n\nsolution\n\ninfo\n\nkeywords"
    sendText(text)

    content = "tell application \"System Events\"\nkey code 126\nkey code 126\nkey code 126\nkey code 126\nkey code 126\nkey code 126\nkey code 115\nkey code 49\nkey code 49\nkey code 49\nkey code 49\nkey code 119\nkey code 49\nkey code 126\nkey code 119\nkey code 49\nend tell"
    script = applescript.AppleScript(content)
    script.run()

def date():
    sendText(MacUtil.date())

def timeStamp():
    sendText(MacUtil.timeStamp())

def timeStampShort():
    sendText(MacUtil.timeStampShort())

def getSelection():
    storedClipboard = beforeSetClipboard()
    time.sleep(0.1)
    text = MacClipboardUtil.paste()
    afterSetClipboard(storedClipboard)
    return text

def beforeSetClipboard():
    storedClipboard = MacClipboardUtil.paste()
    #SendToUi.key("Control") # since the control key could be already pressed by calling shortcut we need to release it
    time.sleep(0.1)

    # emacs processing
    # this triggers a custom macro in emacs - if nothing is selected it selects the whole line otherwise do nothing
    if (MacCommon.isAtiveTitle(MacCommon.EMACS_TITLE)):
        MacUtil.run("tell application \"System Events\"\nkeystroke \"t\" using control down\nend tell")
        time.sleep(0.1)

    content = "tell application \"System Events\"\nkeystroke \"c\" using control down\nend tell"
    script = applescript.AppleScript(content)
    script.run()

    return storedClipboard

def afterSetClipboard(storedClipboard):
    MacClipboardUtil.copy(storedClipboard)

def openSelection():
    text = getSelection()
    text = SystemUtil.transformUrlBeforeOpen(text)
    os.popen("open " + text)
    return None

# Not tested
def runSelection():
    text = getSelection()
    common = SystemUtil.transformUrlBeforeOpen(text)
    os.popen("open -a " + common)
    return None