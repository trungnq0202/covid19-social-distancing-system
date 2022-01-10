import time
from multiprocessing import Process

from grove.display import JHD1802
# LCD 16x2 Characters
dobj = JHD1802()

def display_message(message):
    rows, cols = dobj.size()
    dobj.setCursor(0, 0)
    dobj.write(message)
    time.sleep(5)
    dobj.clear()


def main():
    import time

    lcd = JHD1802()
    rows, cols = lcd.size()
    print("LCD model: {}".format(lcd.name))
    print("LCD type : {} x {}".format(cols, rows))

    lcd.backlight(False)
    time.sleep(1)

    lcd.backlight(False)
    lcd.setCursor(0, 0)
    lcd.write("hello world!")
    lcd.setCursor(0, cols - 1)
    lcd.write('X')
    lcd.setCursor(rows - 1, 0)
    for i in range(cols):
        lcd.write(chr(ord('A') + i))

    time.sleep(3)
    lcd.clear()

if __name__ == '__main__':
    display_message("hello")
