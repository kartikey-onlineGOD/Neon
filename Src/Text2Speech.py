import gtts
from playsound import playsound
def T2S( k ):
    tts = gtts.gTTS(k)
    # save the audio file
    tts.save("hello.mp3")
    # play the audio file
    playsound("hello.mp3")

T2S("Hello")
