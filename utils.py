from gtts import gTTS
import random
import signal
from pygame import mixer

def timeout_handler(signum, frame):
    raise Exception("Input timeout")  # raises an exception to break the input prompt

def create_audio(name, path):
    # The text that you want to convert to audio
    mytext = f'{name} hai firmato?'

    # Language in which you want to convert
    random_language = random.choice(["de", "it", "fr"])

    audio = gTTS(text=mytext, lang=random_language, slow=False)
    audio.save(path)

def play_audio():
    mixer.init()
    mixer.music.load('audio.mp3')
    mixer.music.play()

def have_clocked_in():
    try:
        signal.signal(signal.SIGALRM, timeout_handler)  # register the timeout handler for SIGALRM
        signal.alarm(10)  # set the alarm to trigger after 10 seconds
        print("Input something if you have clocked in: ")
        input_data = input()
    except:
        input_data = False
    signal.alarm(0)  # cancel the alarm
    if input_data:
        return True
    else:
        print("You didn't clock in, I'll ask you in 15 minutes")
        return False