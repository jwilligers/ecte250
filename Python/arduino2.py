from nanpy import Arduino as A
led = 13
 
# SETUP:
A.pinMode(led, A.OUTPUT)
 
# LOOP:
while True:
    A.digitalWrite(led, A.HIGH); # turn the LED on (HIGH is the voltage level)
    print "blink on"
    A.delay(200); # wait for a second
    A.digitalWrite(led, A.LOW); # turn the LED off by making the voltage LOW
    print "blink off"
    A.delay(200);

