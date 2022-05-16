from microbit import *

################################################################################

def readableTime(sec):
    
    # hours
    hours = int(sec / 3600) # int to round the bool down
    
    # minutes
    sec = sec % 3600
    minutes = int(sec / 60) # int to round the bool down
    
    # seconds
    # sec = sec % 60
    
    # return readable text
    return str(hours) + ':' + str(minutes) #+ 'm' + str(sec) + 's' 

################################################################################

timeToSeconds = 1000
seconds = 0
continueTiming = True

while True:
    
    # start UI
    display.show(Image( '00000:'
                        '09400:'
                        '09990:'
                        '09400:'
                        '00000'))
    
    # press A to start timing
    if button_a.is_pressed():

        while continueTiming:
            
            # display current time
            display.scroll(readableTime(seconds), wait = False) # scroll text, wait false let's to code continue while the animation is playing
            
            # icon
            sleep(3 * timeToSeconds)
            seconds += 3
            display.show(Image( '04940:'
                                '40904:'
                                '90999:'
                                '40004:'
                                '04940'), wait = False)
                                
            # count
            sleep(7 * timeToSeconds)
            seconds += 7