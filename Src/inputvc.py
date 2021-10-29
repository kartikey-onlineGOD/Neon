import speech_recognition as sr
import simpleaudio as sa 

s=""


def s2t( ):
    # Initialize recognizer class (for recognizing the speech)

    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable

    with sr.Microphone() as source:
        audio_text = r.listen(source)
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
        try:
            # using google speech recognition
            s=" "
            s = r.recognize_google(audio_text)
            return s
        except:
            wave_obj = sa.WaveObject.from_wave_file("Sorry.wav")
            play_obj = wave_obj.play()
            s2t( )
