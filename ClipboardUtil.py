#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Clipboard handldling. Based on xsel, xclip tools. These tools must be installed.

Author Andrew Terekhine
Since 2011-11-23
"""

import subprocess
import sys

def pasteFromClipboardXsel():
    try:
        xsel = subprocess.Popen(["xsel", "--output", "--clipboard"], stdout=subprocess.PIPE)
    except OSError:
        sys.exit("xsel must be installed")
    output = xsel.communicate()[0]
    return output

def copyToClipboardXclip(text):
    try:
        xclip = subprocess.Popen(['xclip', '-selection', 'c'], stdin=subprocess.PIPE)
    except OSError:
        sys.exit("xsel must be installed")
    xclip.stdin.write(text)
    xclip.stdin.close()
    retcode = xclip.wait()
    return retcode
