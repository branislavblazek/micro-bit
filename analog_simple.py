# Add your Python code here. E.g.
from microbit import *

clock = [Image.CLOCK1,Image.CLOCK2,Image.CLOCK3,Image.CLOCK4,Image.CLOCK5,Image.CLOCK6,Image.CLOCK7,Image.CLOCK8,Image.CLOCK9,Image.CLOCK10,Image.CLOCK11,Image.CLOCK12]

while True:
    for i in range(12):
        print(clock[i])
        display.show(clock[i])
        sleep(500)
        