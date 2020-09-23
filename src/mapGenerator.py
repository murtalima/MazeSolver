import numpy as np
from PIL import ImageGrab
import cv2
class MapGen:

    def draw_lines(self):
        ret, th = cv2.threshold(self.map, 254, 255, cv2.THRESH_BINARY_INV)
        self.map = np.zeros_like(self.map)

        l = -1
        for line in th:
            l += 1
            p = -1
            # print("")
            for point in line:
                p += 1
                if (point[0] < 100):
                    self.map[l, p] = [255, 255, 255]
                    self.map_bin[l, p] = 0
                    # print("0", end='')
                else:
                    self.map_bin[l, p] = 1
                    self.map[l, p] = [0, 0, 0]
                    # print("1", end='')
        return self.map_bin, map

    def find_objectives(self):
        # 1 = inicio
        # 0 = fim
        bin = 0
        l = -1
        for line in self.map_bin:
            is_up = False
            p1_done = False



            l += 1
            p = -1
            for point in line:
                p += 1
                if (point == 0):
                    if (p1_done == True):
                        is_up = True
                    else:
                        if (is_up == True):
                            p1_done = True
                            is_up = False
                            p1 = (p, l)
                else:
                    if (p1_done == True):
                        if (is_up == True and p1[1] == l):
                            p1_done = False
                            is_up = False
                            p2 = (p, l)
                            self.p1s = p1
                            self.p2s = p2

                            if(bin == 0):
                                self.p3s = p1
                                self.p4s = p2
                                bin =1

                        else:
                            p1_done = False
                            is_up = True



                    else:
                        is_up = True
                        p1_done = False

    def set_objectives(self):
        self.find_objectives()
        print(self.p1s,self.p2s,self.p3s,self.p4s)
        vp1 = (self.p2s[0] - self.p1s[0])
        vp2 = (self.p4s[0] - self.p3s[0])
        for x in range(vp1+1):
            self.map[self.p1s[1] ,self.p1s[0]+ x] = [0,255,0]
            self.map_bin[self.p1s[1], self.p1s[0]+ x] = 3
        for x in range(vp2+1):
            self.map[self.p3s[1],self.p3s[0] + x] = [0,0,255]
            self.map_bin[self.p3s[1] , self.p3s[0]+ x] = 2
    def __init__(self,screen):
        self.p1s = (0,0)
        self.p2s = (0, 0)
        self.p3s = (0, 0)
        self.p4s = (0, 0)
        self.screen = screen
        self.map = cv2.cvtColor(self.screen, cv2.COLOR_BGR2RGB)
        w, h, _ = self.map.shape
        self.map_bin = np.zeros(shape=(w, h), dtype="int")
        self.draw_lines()
        self.set_objectives()
    def save_map (self):
        file1 = open("lib/map_bin.txt", "w")
        for line in self.map_bin:
            file1.write("\n")
            for point in line:
                file1.write(str(point))
        file1.close()


