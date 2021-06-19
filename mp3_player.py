from microbit import *

# Const of IMAGES
PLAY_IMAGE = Image("09000:09900:09990:09900:09000")
PAUSE_IMAGE = Image("09090:09090:09090:09090:09090")
MAX_INDEX = 9
# Variables
is_playing = 1
is_change = False
index_song = 0
# Some useful functions
def decrease_index():
    global index_song
    if index_song - 1 >= 0:
        index_song -= 1
    else:
        index_song = MAX_INDEX
    
def increase_index():
    global index_song
    if index_song + 1 <= MAX_INDEX:
        index_song += 1
    else:
        index_song = 0

while True:
    # Important initials
    is_change = False
    level = display.read_light_level()
    acc_x =  accelerometer.get_x()  
    # Logic of behaviour
    if level == 0:
        is_playing = 1 - is_playing
        is_change = True
        
    if acc_x <= -500:
        decrease_index()
    elif acc_x >= 500:
        increase_index()
        
    # Decide what to show at Dispay
    if is_change:
        display.show(PLAY_IMAGE if is_playing else PAUSE_IMAGE)
    else:
        display.show(index_song)
        
    # I need relax, I need sleep!
    sleep(1000)
