#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sandesh
#
# Created:     17/03/2022
# Copyright:   (c) Sandesh 2022
# Licence:     <your licence>
#---------------------------------------------------------------------------

import sounddevice
from scipy.io.wavfile import write
fs=44100
second =  int(input("Enter time duration in seconds: "))
print("Recording.....n")
record_voice = sounddevice.rec( int( second * fs ) , samplerate = fs , channels = 2 )
sounddevice.wait()
sounddevice.query_devices()
write("out.wav", fs , record_voice )
print("Recording is done Pleaase open the folder to listen the music.")