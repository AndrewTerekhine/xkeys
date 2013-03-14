#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sends series of characters to UI. Based on xdotool. This tool must be installed.
This class uses fastest way: clipboard and xdotool.

Author Andrew Terekhine
Since 2012-12-06
"""
import sys
import Common
import KeyboardUtil
import SendToUi
import time

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

def fireFoxAltWToCtrlW():
    if Common.isAtiveTitle(Common.FIREFOX_TITLE):
        SendToUi.sendKey("Alt")
        SendToUi.sendKey("Control+w")