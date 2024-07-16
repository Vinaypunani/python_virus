import rotatescreen as screen
import time as time

display = screen.get_primary_display()

list_of_angles = [90,180,270,0]

for i in range(3):
    for x in list_of_angles:
        display.rotate_to(x)
        time.sleep(1)