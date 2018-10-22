from microbit import *
#sleep(10000)
#display.scroll(str(button_a.get_presses()))

while running_time() < 10000:
    display.show(Image.ASLEEP)

display.show(Image.SURPRISED)

#while True:
#    if button_a.is_pressed():
#        display.show("1")
#    else:
#        display.show("0")
