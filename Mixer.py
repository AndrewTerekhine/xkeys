#!/usr/bin/env python

"""
Retrieves Firefox's title and URL and sends them back to UI control like text editor as two lines.

Author Andrew Terekhine
Since 2013-02-25
"""
import os

import Message
import SystemUtil

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

def volumeUp():
    os.popen("pamixer --increase 5 --allow-boost")
    volume=SystemUtil.getProcessOutput("pamixer --get-volume")
    Message.hint(volume)

def volumeDown():
    os.popen("pamixer --decrease 5")
    volume=SystemUtil.getProcessOutput("pamixer --get-volume --allow-boost")
    Message.hint(volume)
