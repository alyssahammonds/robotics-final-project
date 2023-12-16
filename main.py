#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile


# this program will move the that is holding a pen to draw a polygon

ev3 = EV3Brick()
#beep
ev3.speaker.beep()

# motors
shoulder = Motor(Port.A)
elbow = Motor(Port.B)

# sensors
touch = TouchSensor(Port.S1)

# constants - these can be changed
shoulder_speed = 100
elbow_speed = 100

# functions
def move_shoulder_left():
    shoulder.run_target(shoulder_speed, 90)

def move_shoulder_right():
    shoulder.run_target(shoulder_speed, 0)

def move_elbow_forward():
    elbow.run_target(elbow_speed, 90)

def move_elbow_backward():
    elbow.run_target(elbow_speed, 0)

# center shoulder
ev3.speaker.say("Centering base")
while not touch.pressed():
    shoulder.run(shoulder_speed)    
shoulder.stop(Stop.HOLD)


# drawing functions
# take shape from user

elbow.run_target(elbow_speed, -90)
shoulder.run_target(shoulder_speed, 0)

