from microbit import *

hour = 21
minute = 23
prev_time = 0

def displayTime():
    display.scroll(str(int(hour/10))+str(hour%10)+":"+str(int(minute/10))+str(minute%10))

while True:
    current_time = running_time()
    if (current_time - prev_time) > 60000:
        prev_time += 60000
        minute += 1
        if minute > 59:
            minute = 0
            hour += 1
            if hour > 23:
                hour = 0
        displayTime()

    if button_a.was_pressed():
        hour += 1
        if hour > 23:
            hour = 0
        #displayTime()
        
    if button_b.was_pressed():
        minute += 1
        if minute > 59:
            minute = 0
        prev_time = current_time # Clear second to zero
        #displayTime()
        
    if accelerometer.was_gesture("shake") or pin0.is_touched():
        displayTime()
