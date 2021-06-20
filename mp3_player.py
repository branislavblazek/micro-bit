from microbit import *
import music

# Consts
PLAY_IMAGE = Image("09000:09900:09990:09900:09000")
PAUSE_IMAGE = Image("09090:09090:09090:09090:09090")
SPEAKER_ON = Image("09009:99090:99900:99090:09009")
SPEAKER_OFF = Image("09000:99000:99900:99000:09000")
PLAYLIST = [music.ENTERTAINER, music.ODE, music.BLUES, music.WEDDING,
music.FUNERAL, music.PYTHON, music.CHASE, music.WAWAWAWAA, music.FUNK, music.NYAN]
MAX_INDEX = 9
# Variables
is_player_playing = 1
is_song_playing = 0
is_speaker_playing = 1
is_player_change = False
is_speaker_change = False
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
        
def stop_song():
    global is_song_playing
    is_song_playing = 0
    music.stop()

while True:
    # Important initials
    is_player_change = False
    is_speaker_change = False
    # Logic of behaviour
    # Is playing player?
    level = display.read_light_level() 
    if level == 0:
        is_player_playing = 1 - is_player_playing
        is_player_change = True
        
    # Decrease or increase counter?
    acc_x = accelerometer.get_x() 
    if acc_x <= -500:
        decrease_index()
        stop_song()
    elif acc_x >= 500:
        increase_index()
        stop_song()
        
    # Is speaker playing?
    if button_b.was_pressed():
        is_speaker_playing = 1 - is_speaker_playing
        is_speaker_change = True
    
    # Turn or of off speaker
    if is_speaker_playing == 1:
        speaker.on()
    elif is_speaker_playing == 0:
        speaker.off()
        
    # Decide what to show at Dispay
    if is_player_change:
        display.show(PLAY_IMAGE if is_player_playing else PAUSE_IMAGE)
    elif is_speaker_change:
        display.show(SPEAKER_ON if is_speaker_playing else SPEAKER_OFF)
    else:
        display.show(index_song)
    
     # Decide what to play and play
    if is_player_playing == 1 and is_song_playing == 0:
        is_song_playing = 1
        music.play(PLAYLIST[index_song], wait=False, loop=True)
        
    if is_player_playing == 0:
        is_song_playing = 0
        music.stop()
        
    # I need relax, I need sleep!
    sleep(1000)