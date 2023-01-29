# read
import time
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()
reader = SimpleMFRC522()

def safe_exit(signum, frame):
    exit(1)

def main():
    while True:
        print("Reading...Please place the card...")
        lcd.text("Waiting for", 1)
        lcd.text("RFID Card", 2)
        id, text = reader.read()
        lcd.clear()
        lcd.text("%s" % (id), 1)
        if text != None or text.len() == 0:
            lcd.text(text, 2)
        else:
            lcd.text("Not Assigned")
        time.sleep(3)
        lcd.clear()
        lcd.text("Waiting for", 1)
        lcd.text("RFID Card", 2)
def destroy():
    lcd.clear()
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
        main()
    # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()