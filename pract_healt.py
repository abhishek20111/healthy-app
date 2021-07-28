from gtts import gTTS
def convert_to_audio(str):
    audio=gTTS(str)
    audio.save('water.mp3')

convert_to_audio("Please Drink water")

def convet_to_sound(str):
    sudio=gTTS(str)
    sudio.save('eyes.mp3')

convet_to_sound("Please do eyes Exercise")

def convet_to_lisen(str):
    nudio=gTTS(str)
    nudio.save('physical.mp3')

convet_to_lisen("Please do Exercise")






#                             play sond

# from pygame import mixer
#
# mixer.init()
#
# mixer.music.load("song.mp3")
#
# mixer.music.set_volume(0.7)
#
# mixer.music.play()
#
# while True:
#
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input("  ")
#
#     if query == 'p':
#
#         # Pausing the music
#         mixer.music.pause()
#     elif query == 'r':
#
#         # Resuming the music
#         mixer.music.unpause()
#     elif query == 'e':
#
#         # Stop the mixer
#         mixer.music.stop()
#         break









# from pygame import mixer
# from datetime import datetime
# from time import time
#
# def musicsound(file,stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#
#     while True:
#         input_from_user=input()
#         if input_from_user==stopper:
#             mixer.music.stop()
#             break
#
# def log_now(msg):
#     with open("mylogs.txt","a") as f:
#         f.write(f"{msg} {datetime.now()}\n")
#
# if __name__ == '__main__':
#     init_water=time()
#     init_eyes=time()
#     init_exercise=time()
#
#     water=5
#     eyes=10
#     exercise=15
#
#     while True:
#         if time()-init_water > water:
#             print("water drinking time , Enter 'done' to stop")
#             musicsound('water.mp3','done')
#             init_water=time()
#             log_now("Drank water at")
#
#         if time()-init_exercise > exercise:
#             print("Do exercise .Press 'done' to stop")
#             musicsound('physical.mp3','done')
#             init_exercise=time()
#             log_now("Exercise done at")
#
#         if time()-init_eyes > eyes:
#             print("Do eyes ,Type 'done' to stop it")
#             musicsound('eyes.mp3','done')
#             init_eyes=time()
#             log_now("Exercise done at")













#                                        i am pratice again the above programm

from pygame import mixer
from datetime import datetime
from time import time

def playmusic(file,pause,play,stop):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        print("'p' to pause, 'r' to resume")
        print("'e' to exit the program")

        inpu_user = input()

        if inpu_user=='p':
            mixer.music.pause()
            print("type 'done' for futher")
            continue

        elif inpu_user=='e':
            mixer.music.unpause()
            print("type 'done' for futher")
            continue

        elif inpu_user == stop:
            mixer.music.stop()

        break

def log_now(msg):
    with open(f"mylog.txt","a") as f:
        f.write(f"{msg},{datetime.now()}\n")

if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()

    water_drink=5
    eyes_exercise=10
    physical_exercise=20

    while True:
        if time()-init_water>water_drink:
            print("Please drink water ,Press 'done' when you done")
            playmusic('water.mp3','p','e','done')
            init_water=time()
            log_now("Drank water at")

        if time() - init_eyes > eyes_exercise:
            print("Please do eyes exercise ,Press 'done' when you done")
            playmusic('eyes.mp3', 'p', 'e', 'done')
            init_eyes = time()
            log_now("Eyes exercise at")

        if time() - init_exercise > physical_exercise:
            print("Please do physical exercise ,Press 'done' when you done")
            playmusic('physical.mp3', 'p', 'e', 'done')
            init_exercise = time()
            log_now("Exercise of body done  at")
