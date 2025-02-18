from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

color_sensor = ColorSensor(Port.F)

while True:
    detect_color = color_sensor.color()
    print(f"Detected Color: {detect_color}")
    wait(200)
