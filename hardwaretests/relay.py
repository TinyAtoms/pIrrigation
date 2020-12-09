# import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
import time
from datetime import datetime, timedelta



def activate_relay(relay, t):
    GPIO.setmode(GPIO.BCM)
    trigger = 23
    echo = 24
    GPIO.setup(trigger ,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)

    # reset trigger pin, and let the sensor settle
    GPIO.output(trigger, False)
    time.sleep(2)



if __name__ == "__main__":
    d = activate_relay(1,timedelta(seconds=2))
    print "distance is"
    print d + "mm"
    # print(f"distance is {d} mm or {d/1000} m")
