import RPi.GPIO as GPIO
#from gpiozero import DistanceSensor
import time
from datetime import datetime, timedelta



def sense_distance():
    ms = timedelta(microseconds=1)
    GPIO.setmode(GPIO.BCM)
    trigger = 23
    echo = 24
    GPIO.setup(trigger ,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    print("Reseting triggers")

    # reset trigger pin, and let the sensor settle
    GPIO.output(trigger, False)
    time.sleep(2)
    print("Trigger it")
    # send a 10 us pulse to the trigger pin
    GPIO.output(trigger, True)
    time.sleep(11E-6)
    GPIO.output(trigger, False)
    
    print("waiting for input")

    # the time we want is the total time echo = HI so we take the last timestamp 
    # it was LO and the last timestamp it was HI, take the diff between them
    while GPIO.input(echo)==0:
        pulse_start = datetime.now()
    while GPIO.input(echo)==1:
        pulse_end = datetime.now()     
    time_delta = (pulse_end - pulse_start)  / (2 * ms)
    time_delta -= 0 # we need to calibrate this
    #like, 1mm is een dt van ~3us, en in deze order of magnitude zijn spelen processing shit een rol
    # distance is time in ms * speed of sound in mm/ms
    distance = time_delta * 343
    return distance

def higherlevel_distance():
    sensor = DistanceSensor(23,24)
    distance = sensor.distance * 1000
    return distance


if __name__ == "__main__":
    print("trying lowlevel stuff")
    d = sense_distance()
    print(f"distance is {d} mm or {d/1000} m")

    print("Trying higher level function:")
    d2 = higherlevel_distance()
    print(f"distance is {d2} mm or {d2/1000} m")