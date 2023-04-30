import serial, time, pyaudio, wave, threading, pygame, thread, sys

# ser = serial.Serial(sys.argv[1], 9600)

# class AudioThread(threading.Thread):
#     def __init__(self,fileName):
#         super(AudioThread, self).__init__()
#         self.fileName=fileName

#     def run(self):
#         #define stream chunk   
#         chunk = 1024  

#         #open a wav format music  
#         f = wave.open(self.fileName,"rb")  

#         #instantiate PyAudio  
#         p = pyaudio.PyAudio()  

#       #open stream  
#         stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
#             channels = f.getnchannels(),  
#             rate = f.getframerate(),  
#             output = True)  

#         #read data  
#         data = f.readframes(chunk)  

#         #play stream  
#         while data != '':  
#             stream.write(data)  
#             data = f.readframes(chunk) 
        
#         #stop stream  
#         stream.stop_stream()  
#         stream.close()  

#         #close PyAudio  
#         p.terminate()  

# class AudioThread2(threading.Thread):
#     def __init__(self,fileName):
#         super(AudioThread2, self).__init__()
#         self.fileName=fileName

#     def run(self):
#         pygame.mixer.init()
#         pygame.mixer.music.load(self.fileName)
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy() == True:
#             continue

def playSound(fileName):
    pygame.mixer.init()
    pygame.mixer.music.load(fileName)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def playRightAnswer():
    # thread = AudioThread2("right_answer.wav")
    # thread.start()
    thread.start_new_thread ( playSound, ('right_answer.wav',) )

def playBuzzerPressed():
    # thread = AudioThread2("buzzer_pressed.wav")
    # thread.start()
    thread.start_new_thread ( playSound, ('buzzer_pressed.wav',) )




