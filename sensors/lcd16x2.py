import time
from multiprocessing import Process

from grove.display import JHD1802
# LCD 16x2 Characters
dobj = JHD1802()

def display_message(message):
    rows, cols = dobj.size()
    dobj.setCursor(0, 0)
    dobj.write(message)
    time.sleep(10)
    dobj.clear()


def display(message):
    action_process = Process(target=display_message, args=(message, ))

    # We start the process and we block for 5 seconds.
    action_process.start()
    action_process.join(timeout=5)

    # We terminate the process.
    action_process.terminate()