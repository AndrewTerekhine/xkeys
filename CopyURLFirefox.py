#!/usr/bin/env python

"""
Retrieves Firefox's title and URL and sends them back to UI control like text editor as two lines.

Author Andrew Terekhine
Since 2011-02-01
"""

import logging
import os
import subprocess
import sys
import gtk
import ClipboardUtil
import Message
import subprocess
import SendToUi
import SendToUi
import SystemUtil

fireFoxPid=SystemUtil.getProcessOutput("pidof firefox")

if fireFoxPid == "":
    sys.exit("Firefox window is not found")
lines = fireFoxPid.split(None, 4)
fireFoxPid = lines[0]

fireFoxWindowName=SystemUtil.getWindowNameByProcessId(fireFoxPid)
(title,s,url) = fireFoxWindowName.partition('- Firefox -')
lines = title.split(None, 4)
title = lines[4]

# sometimes there are several browser windows are opened get the url of the first window
lines = url.split(None, 2)
url = lines[0]

storedClipboard = ClipboardUtil.pasteFromClipboardXsel()

SendToUi.sendText(title +"\n    " + url.lstrip())

ClipboardUtil.copyToClipboardXclip(storedClipboard)