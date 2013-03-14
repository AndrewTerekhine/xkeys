# Author Andrew Terekhine
# Since 2011-02-01

import subprocess
import Common
import KeyboardUtil

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

def fireFox():
    Common.openProcess('firefox', '- Firefox -', 'Firefox', '')

def idea():
    Common.openProcess('intellijidea-ce', 'Intellij', 'Idea')

def calendar():
    subprocess.Popen(['firefox', 'https://www.google.com/calendar/b/0/render?tab=mc&pli=1'])

def gnomeTerminal():
    KeyboardUtil.setDefaultLanguage()
    Common.openProcess('gnome-terminal', 'at@at-arch-laptop', '', '')
