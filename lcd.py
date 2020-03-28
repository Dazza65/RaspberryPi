#!/usr/bin/python

from RPi import GPIO
from RPLCD.gpio import CharLCD
import time

def main():
 
  while True:
    display('Hello Alana', 'and Lauren!')
    display('this is what you', 'can do coding')
    display('Dad is the', 'GREATEST')
 

def display(line1, line2):
    lcd.clear()
    lcd.cursor_pos = (0,0)
    lcd.write_string(line1)
    lcd.cursor_pos = (1,0)
    lcd.write_string(line2)
    time.sleep(3)
 
if __name__ == '__main__':
 
  try:
    lcd = CharLCD(pin_rs=26,pin_e=24,pins_data=[32,18,16,12],numbering_mode=GPIO.BOARD)
    smiley = (
        0b00000,
        0b01010,
        0b01010,
        0b00000,
        0b10001,
        0b10001,
        0b01110,
        0b00000,
    )
    lcd.create_char(0,smiley)
    main()
  except KeyboardInterrupt:
    pass
  finally:
    display('Goodbye!', '       \x00')
    time.sleep(3)
    GPIO.cleanup()
