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
claw = Motor(Port.C)

# sensors
touch = TouchSensor(Port.S1)

# constants
shoulder_speed = 100
elbow_speed = 100
claw_speed = 100

# functions
def move_shoulder(degrees):
    shoulder.run_target(shoulder_speed, degrees)

def move_elbow(degrees):
    elbow.run_target(elbow_speed, degrees)


# center shoulder
ev3.speaker.say("centering shoulder")
while not touch.pressed():
    shoulder.run(shoulder_speed)
shoulder.stop(Stop.HOLD)

# move elbow
# this goes down
elbow.run_target(elbow_speed, 90)


