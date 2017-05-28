import time
import RPi.GPIO as GPIO

def setup():
    try:
        # Pin Setup:
        GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
        GPIO.setwarnings(False)
    except Exception as e:
        print "Error!"
        print e
    
def ledSetup(LEDpin):
    try:
        GPIO.setup(LEDpin, GPIO.OUT) # LED pin set as output
    except Exception as e:
        print "Error!"
        print e
        
def butSetup(butPin):
    try:
        GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    except Exception as e:
        print "Error!"
        print e

def LEDoff(LEDpin):
    try:
        GPIO.output(LEDpin, GPIO.LOW)
    except Exception as e:
        print "Error!"
        print e

def LEDon(LEDpin):
    try:
        GPIO.output(LEDpin, GPIO.HIGH)
    except Exception as e:
        print "Error!"
        print e
        
def butPush(butPin, whattosay):
    try:
        while GPIO.input(butPin) == GPIO.HIGH:
            time.sleep(0.01)
        if GPIO.input(butPin) == GPIO.LOW:
            whattosay()
    except Exception as e:
	print "Error!"
	print e
def butPush2(butPin, whattosay1, butPin1, whattosay):
    while True:
        input_state = GPIO.input(butPin)
        input_state1 = GPIO.input(butPin1)
        if input_state == False:
            whattosay1()
            time.sleep(0.01)
        if input_state1 == False:
            whattosay()
            time.sleep(0.01)

def butPush3(butPin, whattosay1, butPin1, whattosay2, butPin2, whattosay):
    while True:
        try:
            input_state = GPIO.input(butPin)
            input_state1 = GPIO.input(butPin1)
            input_state2 = GPIO.input(butPin2)
            if input_state == False:
                whattosay1()
                time.sleep(0.01)
            if input_state1 == False:
                whattosay2()
                time.sleep(0.01)
            if input_state2 == False:
                whattosay()
                time.sleep(0.01)
        except Exception as e:
            print "Error!"
            print e
def cleanup():
    try:
        GPIO.cleanup()
    except Exception as e:
	print "Error!"
	print e
