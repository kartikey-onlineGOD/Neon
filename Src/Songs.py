import numpy
import Inputvc2 as ivct
import simpleaudio as sa


try :
    def Play( k ) :
        if(k.find("attention") >= 0 ):
            wave_obj = sa.WaveObject.from_wave_file("Attention.wav")
            play_obj = wave_obj.play()
            ggg = ivct.s2t()
            if(ggg.find("stop") >= 0 ):
                play_obj.stop()
            else:
                play_obj.wait_done()
                
        elif(k.find("talk anymore") >= 0 ):
            wave_obj = sa.WaveObject.from_wave_file("We Don't Talk Anymore.wav")
            play_obj = wave_obj.play()
            ggg = ivct.s2t()
            if(ggg.find("stop") >= 0 ):
                play_obj.stop()
            else:
                play_obj.wait_done()
                
        elif(k.find("memories") >= 0 ):
            wave_obj = sa.WaveObject.from_wave_file("Memories.wav")
            play_obj = wave_obj.play()
            ggg = ivct.s2t()
            if(ggg.find("stop") >= 0 ):
                play_obj.stop()
            else:
                play_obj.wait_done()
                
        elif(k.find("bad boy") >= 0 ):
            wave_obj = sa.WaveObject.from_wave_file("BadBoy.wav")
            play_obj = wave_obj.play()
            ggg = ivct.s2t()
            if(ggg.find("stop") >= 0 ):
                play_obj.stop()
            else:
                play_obj.wait_done()
                
        elif(k.find("stack") >= 0 ):
            wave_obj = sa.WaveObject.from_wave_file("StackItUp.wav")
            play_obj = wave_obj.play()
            ggg = ivct.s2t()
            if(ggg.find("stop") >= 0 ):
                play_obj.stop()
            else:
                play_obj.wait_done()
                
        elif(k.find("good thing") >= 0 ):
            wave_obj = sa.WaveObject.from_wave_file("GoodThing.wav")
            play_obj = wave_obj.play()
            ggg = ivct.s2t()
            if(ggg.find("stop") >= 0 ):
                play_obj.stop()
            else:
                play_obj.wait_done()
        else:
            print("wrong choice")
            import Songs
except :
    Song("attention")
    

        
