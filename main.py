#!/usr/bin/python3

################################################################################
# main.py: Implementation of GPIO in Python using OOP.
################################################################################
import gpio 

def main():
   """
   main: Connecting a led to pin 17 and a button to pin 27. 
         When the button is pressed, the led is set to blink every 100 ms, 
         otherwise the led is turned off.
   """
   led1 = gpio.output(17)
   button1 = gpio.input(27)
   while True:
      if button1.read():
         led1.blink(100)
      else:
         led1.off()
   return

# Calling the main function to start the program if this is the startup file:
if __name__ == "__main__":
   main()