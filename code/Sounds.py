import threading
import pygame

def play_sound(fileName):
    pygame.mixer.init()
    pygame.mixer.music.load(fileName)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy() == True:
        continue

def correct():
    threading.Thread( target=play_sound, args=('./sounds/right_answer.wav',)).start()

def incorrect():
    threading.Thread( target=play_sound, args=('./sounds/buzzer_pressed.wav',)).start()

def buzzer():
    if(sound_running()):
        threading.Thread( target=play_sound, args=('./sounds/wrong.mp3',), name='buzzer').start()
    # t1.join()
    
def sound_running():
    for th in threading.enumerate():
        if th.name == 'buzzer':
            print('buzzer running')
            return False
    return True



