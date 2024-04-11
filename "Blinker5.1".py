
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Setup
ledRed = LED(14)
ledGreen = LED(18)
ledBlue = LED(24)

# GUI
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Calibri', size = 12, weight = "bold")

#Functions

def ledRedToggle():
        if ledRed.is_lit:
                ledRed.off()
                ledRedButton["text"] = "Turn on RED LED"
        else:
                ledRed.on()
                ledRedButton["text"] = "Turn off RED LED"

def ledGreenToggle():
        if ledGreen.is_lit:
                ledGreen.off()
                ledGreenButton["text"] = "Turn on GREEN LED"
        else:
                ledGreen.on()
                ledGreenButton["text"] = "Turn off GREEN LED"

def ledBlueToggle():
        if ledBlue.is_lit:
                ledBlue.off()
                ledBlueButton["text"] = "Turn on BLUE LED"
        else:
                ledBlue.on()
                ledBlueButton["text"] = "Turn off BLUE LED"

def exitToggle():
        win.destroy()

# Window
ledRedButton = Button(win, text = 'Turn RED LED on', font = myFont, command = ledRedToggle, bg = 'bisque2', height = 1, width = 24)
ledRedButton.grid(row = 0, column = 1)
ledGreenButton = Button(win, text = 'Turn GREEN LED on', font = myFont, command = ledGreenToggle, bg = 'bisque2', height = 1, width = 24)
ledGreenButton.grid(row = 1, column = 1)
ledBlueButton = Button(win, text = 'Turn BLUE LED on', font = myFont, command = ledBlueToggle, bg = 'bisque2', height = 1, width = 24)
ledBlueButton.grid(row = 2, column = 1)

# Exit
exitButton = Button(win, text = 'EXIT', font = myFont, command = exitToggle, bg = 'bisque2', height = 1, width = 24)
exitButton.grid(row = 3, column = 1)

win.mainloop()
