#import library

import speech_recognition as sr
s=""
def s2t( s ):
    # Initialize recognizer class (for recognizing the speech)

    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable

    with sr.Microphone() as source:
        audio_text = r.listen(source)
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
        try:
            # using google speech recognition
            s = r.recognize_google(audio_text)
            return s
        except:
             s = "   "
             s2t( s )
