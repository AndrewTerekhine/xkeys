import os
import subprocess
import string
import Message

NAME = "Andrew"
EMACS_TITLE = " - emacs - "
FIREFOX_TITLE = "Firefox"
INTELLIJ_IDEA_TITLE = "IntelliJ IDEA"
WWW_PREFIX = "www."
USER_FOLDER_PREFIX = "~"
HTTP_PREFIX = "http://"
DEFAULT_LANGUAGE = "us"
SECOND_LANGUAGE = "ru"


def getPid(processName):
    pid = os.popen("pidof " + processName).read().rstrip()
    return pid

def openProcess(processName, title, message, argument):
    if getPid(processName) == "":
        command = processName + " " + argument
        subprocess.Popen(processName)
#        subprocess.call(command, shell=True)
#        subprocess.Popen([processName, argument], creationflags=DETACHED_PROCESS)

        if Message != "":
            Message.hint(message)
    else:
        os.popen("wmctrl -R '" + title + "'")

def openProcessWithTitleCheck(processName, title, message, args):
    if isWindowExist(title):
        os.popen("wmctrl -R '" + title + "'")
    else:
        if Message != "":
            Message.hint(message)
        subprocess.Popen([processName, args])

def isAtiveTitle(title):
    windowName=os.popen("xdotool getactivewindow getwindowname").read().rstrip()
    index = string.find(windowName, title)
    return index != -1

def isWindowExist(title):
    windowName=os.popen("wmctrl -l | grep '" + title + "'").read().rstrip()
    index = string.find(windowName, title)
    return index != -1