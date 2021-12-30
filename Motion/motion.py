
# Raspberry Pi Motion Detection System with System Arming Toggle
# Original Author: Haydn Stucker
# Created: 12/28/2021
# Version: 1.0.2

# Author of Previous Modification: Haydn Stucker
# Date of Previous Modification: 12/30/2021

# DESCRIPTION OF PROJECT
# This project is a Raspberry Pi motion detection system
# using a PIR motion sensor and state LEDs. The objective
# of this system is to visually and audibly alert a manager
# when a person has entered a room. Any configuration of LEDs,
# buttons, audio files, and speaker can be used.

# INSTRUCTIONS TO ACTIVATE PROJECT
# When activting this project, make sure that the audio files
# are in the same folder/location as this Python script on the
# Raspberry Pi. Also make sure that the system audio is set to
# method you are connecting the speaker (BlueTooth or Analog).

# Import Packages
from gpiozero import LED
from gpiozero import MotionSensor
from gpiozero import Button
import pygame
import mutagen.mp3
import time

# Initialize Audio File to be Played
file = "ludicrous_speed_go.mp3"

# Use Mutagen to set the proper Sample Rate for the File
mp3 = mutagen.mp3.MP3(file)
pygame.mixer.init(frequency = mp3.info.sample_rate)
pygame.mixer.music.load(file)

# Define LED Pins (signal, armed, unarmed)
signal_led = LED(17)
armed_led = LED(27)
disarmed_led = LED(22)

# Define Button and Motion Sensor Pins
button = Button(23)
pir = MotionSensor(4)

# Initialize all LEDs to Off Setting
signal_led.off()
armed_led.off()
disarmed_led.off()
# 
# Helper Functions to handle Motion and No Motion
def motion():
#     print("Motion Detected!\n")
    signal_led.on()
    pygame.mixer.music.play()
    time.sleep(10)
    
def no_motion():
#     print("Motion Stopped!\n")
    signal_led.off()

# Initialize the State of the System
armed = False
print("\nSYSTEM ACTIVE\n")

# Operational Protocols
while True:
    # Detect a Button Press
    if button.is_pressed:
#         print("System State Change")
        armed = not armed
        time.sleep(0.1)
#         print(str(armed) + "\n")
    
    # Protocol for Armed System
    if armed == True:
#         print("System is armed...\n")
        disarmed_led.off()
        armed_led.on()
        
        pir.when_motion = motion
        pir.when_no_motion = no_motion
        
        time.sleep(0.1)
    # Protocol for Unarmed System
    else:  
#         print("System is disarmed...\n")
        armed_led.off()
        disarmed_led.on()
        
        pir.when_motion = None
        pir.when_no_motion = None
        
        time.sleep(0.1)
