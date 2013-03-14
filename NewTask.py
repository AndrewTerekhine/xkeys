#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sends series of characters to UI. Based on xdotool. This tool must be installed.
This class uses fastest way: clipboard and xdotool.

Author Andrew Terekhine
Since 2011-11-23
"""
from Tkinter import Tk

import datetime
import sys
import tkSimpleDialog
import ClipboardUtil
import SendToUi

output = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

Tk().withdraw()
text = tkSimpleDialog.askstring('Task category', 'Category::')

if text is None or text == "": sys.exit()

#works as well
#time.sleep(0.24)
#output = system.exec_command("date +%Y%m%d%H%M%S")
#time = output.stdout.readline()
storedClipboard = ClipboardUtil.pasteFromClipboardXsel()
SendToUi.sendText("task " + text + "\n" + "    " + output + " " +  "\n\n" + "solution" + "\n\n" + "info" + "\n\n" + "keywords")
SendToUi.sendKey("Home Up Up Up Up Up Up End")
ClipboardUtil.copyToClipboardXclip(storedClipboard)