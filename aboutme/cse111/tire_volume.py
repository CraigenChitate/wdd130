import math

import datetime

#this line imports the current datetime
now = datetime.datetime.now()
print(now.strftime("%y-%m-%d "))


width = float(input('Enter the width of the tire in mm (ex 205): '))
ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

radical_1 = (2540 * diameter + width * ratio)
radical_1_2 = (math.pi * width**2 * ratio)

volume = ((radical_1 * radical_1_2) / 10000000000)

volume = round(volume, 2)
print()
print(f'The approximate volume is {volume} liters.')


#this line writes data to volume.txt file
with open('volume.txt', 'at') as volumes_file:
    print(f'{now}, {width}, {ratio}, {diameter}, {volume}', file=volumes_file)
