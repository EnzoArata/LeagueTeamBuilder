import tempfile
import sys
import os

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    print('Running in a PyInstaller bundle')
    SCRIPT_DIR = sys._MEIPASS
else:
    print('Running in a normal Python process')
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))