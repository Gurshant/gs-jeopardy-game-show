import serial, time, wave, threading, pygame, sys

def play_sound(fileName):
    pygame.mixer.init()
    pygame.mixer.music.load(fileName)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy() == True:
        continue

def play_right_answer():
   threading.Thread( target=play_sound, args=('right_answer.wav',) ).start()
#     playSound('right_answer.wav')

def play_buzzer_pressed():
    t1 = threading.Thread( target=play_sound, args=('buzzer_pressed.wav',) )
    t1.start()
    t1.join()
#     playSound('buzzer_pressed.wav')

