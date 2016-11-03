import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.IN)
while True:
        while GPIO.input(5)==0:
            start = time.time()
        while GPIO.input(5)==1:
            end = time.time()
        duration = end - start
        distance = duration*17150
        print "distance",distance,"cm"
        time.sleep(1)
GPIO.cleanup()
