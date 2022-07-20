#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sandesh
#
# Created:     18/03/2022
# Copyright:   (c) Sandesh 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#lets create a smart light switch that swiches the lights off if it's daytime
#on if nighttime.


time_period= input("Is it Day or Night? ")
is_day = True
lights_on = False

print("Day time?")
print(is_day)

print("Lights on?")
print(lights_on)

is_day = False
lights_on = not is_day

print("Day time?")
print(is_day)

print('lights_on?')
print(lights_on)