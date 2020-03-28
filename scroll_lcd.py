#!/usr/bin/python

from RPLCD import CharLCD
from RPi import GPIO
import time

framebuffer = [
    'Hello!',
    '',
]

def main():
    lcd = CharLCD(pin_rs=26,pin_e=24,pins_data=[32,18,16,12],numbering_mode=GPIO.BOARD)

    print('Enter some text: ', end = '')
    
    long_string = input()

    while True:
        loop_string(long_string, lcd, framebuffer, 1, 16)
 
def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.2):
    padding = ' ' * num_cols
    s = padding + string + padding
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)

def write_to_lcd(lcd, framebuffer, num_cols):
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')
 
if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
