# Author Andrew Terekhine
# Since 2011-02-01 test

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

import subprocess

def hint(text):
    subprocess.call(('notify-send', "-t", "1000", text))
