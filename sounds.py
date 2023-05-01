import threading, pygame, sys

def play_sound(fileName):
    pygame.mixer.init()
    pygame.mixer.music.load(fileName)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy() == True:
        continue

def correct():
    threading.Thread( target=play_sound, args=('./sounds/right_answer.wav',) ).start()

def incorrect():
    threading.Thread( target=play_sound, args=('./sounds/wrong.mp3',) ).start()

def buzzer():
    threading.Thread( target=play_sound, args=('./sounds/buzzer_pressed.wav',) ).start()
    # t1.join()



