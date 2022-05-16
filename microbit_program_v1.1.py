from microbit import *

seconds = 0
continueTiming = True

# weclome screen
display.show(Image.ASLEEP)
sleep(1000)

while True:
    
    # start UI
    display.show(Image( '00000:'
                        '09300:'
                        '09990:'
                        '09300:'
                        '00000'))
    
    # press A to start timing
    if button_a.is_pressed():
        while continueTiming:
            
            # display current time
            display.scroll(seconds, wait = False) # scroll text, wait false let's to code continue while the animation is playing
            
            # count
            sleep(5000)
            seconds += 5