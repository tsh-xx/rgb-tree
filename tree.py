from microbit import *
import neopixel
import music

np = neopixel.NeoPixel(pin2, 8)
music.play(music.NYAN,wait=False)

while True:
    for i in range(5):
        np[i] = (155, 0, 0)
        np.show()
        sleep(500)
    for i in range(5):
        np[i] = (0, 155, 0)
        np.show()
        sleep(500)
    for i in range(5):
        np[i] = (0, 0, 155)
        np.show()
        sleep(500)
    music.play(music.ODE,wait=False)
