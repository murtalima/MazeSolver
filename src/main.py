import numpy as np
from PIL import ImageGrab
import cv2
import time
from src import mapGenerator
from src import Aanta
import pyautogui
from pynput import keyboard

size = 200
cc = True
def run_Aanta (screen):
    # ---------------------------------------#
    # criar mapa
    # ---------------------------------------#
    map = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    cMap = mapGenerator.MapGen(map)
    map = cMap.map
    map_bin = cMap.map_bin
    p1s = cMap.p1s
    p2s = cMap.p2s
    p3s = cMap.p3s
    p4s = cMap.p4s
    # ---------------------------------------#
    # rodar Aanta
    # ---------------------------------------#
    map, map_bin, caminho = Aanta.Aanta(p1s, p2s, p3s, p4s, map, map_bin)
    for x in caminho:
        screen[x] = [0, 255, 0]
    # ---------------------------------------#
    cv2.imshow("caminho", screen)
    cv2.imshow("map", map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cMap.save_map()
    del cMap




current = set()


def on_press(key):
    global size
    try:
        print(key.char)
        if (key.char == ('e')):
            global cc
            cc = False
            cv2.destroyAllWindows()
            run_Aanta(screen)
            return False

        if (key.char == ('s')):
            if (size > 0):
                size = size - 1
        if (key.char == ('w')):
            if (size > 0):
                size = size + 1
    except AttributeError:
        print('error')

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    else:
        return True
def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:



        while(cc):
            if (cc == False):
                print("a")
                listener.stop()
            x, y = pyautogui.position()
            global screen
            screen = np.array(ImageGrab.grab(bbox=(x - size, y - size, x + size, y + size)))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            map = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

            # print('Loop took {} seconds'.format(time.time() - last_time))
            last_time = time.time()
            cv2.imshow("main", map)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    listener.join()

while(True):
    cc = True
    main()









