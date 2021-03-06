import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#Setting up echo and trigger pin
TRIG = 3
ECHO = 4
maxtime = 0.04

#defining pin as input and output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def distance():
    GPIO.output(TRIG, False)
    time.sleep(0.01)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    start_time = time.time()
    timeout = start_time + maxtime
    while GPIO.input(ECHO) == 0 and start_time < timeout:
        start_time = time.time()
        
    end_time = time.time()
    timeout = end_time + maxtime
    while GPIO.input(ECHO) == 1 and end_time < timeout:
        end_time = time.time()

    t = end_time - start_time
    dist = (t*34300)//2
    return dist

while True:
    d = distance()
    print("dist: ", d)
    