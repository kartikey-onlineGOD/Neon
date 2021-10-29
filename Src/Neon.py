# New Voice Based Assistant
# Neon

#This the latest bot know as Neon

import time
import random
import tkinter 
import os
import numpy 
import simpleaudio as sa
import pafy
import inputvc as ivc
import Inputvc2 as ivct
import Songs as so
import GoogleSearch
import GoogleSearchSong
from PIL import Image
import Text2Speech as ts

def Intro( ):
    ts.T2S("I am listening please continue")
    gg =" "
    gg = ivc.s2t()
    if(gg != None):
        gg = gg.lower( )
    else :
        gg = "play"
    if(gg.find("play") >= 0 or gg.find("song") >= 0):
        wave_obj = sa.WaveObject.from_wave_file("SongChoice.wav")
        play_obj = wave_obj.play()
        gmk = ivc.s2t( )
        GoogleSearchSong.Search(gmk)
        Start( )
    elif(gg.find("what can ") >= 0 ):
        wave_obj = sa.WaveObject.from_wave_file("tas.wav")
        play_obj = wave_obj.play()
        Intro( )
    elif(gg.find("search") >= 0):
        wave_obj = sa.WaveObject.from_wave_file("IML.wav")
        play_obj = wave_obj.play()
        ts.T2S("What do i have to search for on Google " )
        mk = ivc.s2t( )
        GoogleSearch.Search(mk)
        Start( )
    elif(gg.find("timer") >= 0):
        ts.T2S("How long do you want the timer to be in seconds ")
        mk = ivc.s2t( )
        if(mk.find("second") >= 0):
            for i in range(1, int(mk)+1):
                time.sleep(14.9)
                ts.T2S(15*i , " seconds")
            ts.T2S("Time up ")
        
    else:
        Start( )
def Start( ):
    
    ch =" "
    ch = ivct.s2t( )
    if(ch != None):
        ch = ch.lower( )
    else:
        Start( )
    if(ch.find("neon") >= 0 ):
        Intro( )
    else :
        Start( )

      
Intro( )
    
    
