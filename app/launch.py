''' Launcher/entry point. '''

#Import hooks
try:
    import pyi_splash
except:
    print('launcher.py couldn\'t import pyi_splash module')
import cython
import functools
import keyboard
import logging, sys
from datetime import datetime, timedelta #for timed_cache wrapper
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer
from tkinter import *
from tkinter import messagebox
from threading import Thread, Event
from time import sleep
from typing import List
#App
import gui #gui.py - GUI + main app module
import settings #settings.py - App settings
from offsets import Offsets #offsets.py - All offsets

#Entry point
if __name__ == "__main__":
    gui.main()
