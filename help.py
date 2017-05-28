import PycklePi #importing the module
import time # importing the time module
import RPi.GPIO # You will need to install this module by running setup.py
# This is the function 'function'
def function():
    print "A Button Was Clicked!"
    PycklePi.LEDon(18)
    time.sleep(2)
    PycklePi.LEDoff(18)
# Setting up the module / Mandatory for every script
PycklePi.setup()
# Setting up a LED
PycklePi.ledSetup(18)
# Setting up a button(s)
PycklePi.butSetup(17)
PycklePi.butSetup(23)
PycklePi.butSetup(22)
# Turning on a LED
PycklePi.LEDon(18)
# Turning off a LED
PycklePi.LEDoff(18)
# If button pushed, go to function (in this case function 'function')
PycklePi.butPush(17, function)
# If any of the buttons are pushed, go to function after it (in this case, function 'function' for all of them)
PycklePi.butPush2(17, function, 23, function)
# If any of the buttons are pushed, go to function after it (in this case, function 'function' for all of them)
PycklePi.butPush3(17, function, 23, function, 22, function)
