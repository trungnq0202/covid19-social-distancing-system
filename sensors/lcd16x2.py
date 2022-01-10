import time

from grove.display import JHD1802
# LCD 16x2 Characters
dobj = JHD1802()

def display_message(message):
    rows, cols = dobj.size()
    dobj.setCursor(0, 0)
    dobj.write(message)
    time.sleep(10)
    dobj.clear()