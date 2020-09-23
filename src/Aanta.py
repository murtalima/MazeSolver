import cv2
def Aanta (p1s,p2s,p3s,p4s,map,map_bin):
    caminho = []
    #print(p1s, p2s)
    p1 = (p3s[1] +1 , p3s[0])
    #print(p1)
    posR = 1
    posS = 1
    posL = 1
    posN = 1
    caminho = []
    while (posR != 3 and posS != 3 and posL != 3 and posN != 3):
        #cv2.imshow("result", map)

        dis = (p2s[0] - p1[0], p2s[1] - p1[1])
        posR = map_bin[p1[0], p1[1] + 1]
        posS = map_bin[p1[0] + 1, p1[1]]
        posL = map_bin[p1[0], p1[1] - 1]
        posN = map_bin[p1[0] - 1, p1[1]]
        print(dis, posR, posS, posL, posS)
        if (posR == 0):
            p1 = (p1[0] , p1[1]+ 1)
            map[p1] = [255, 0, 0]
            map_bin[p1] = 4
            caminho.append(p1)
        else:
            if (posN == 0):
                p1 = (p1[0] - 1, p1[1])
                map[p1] = [255, 0, 0]
                map_bin[p1] = 4
                caminho.append(p1)
            else:
                if (posL == 0):
                    p1 = (p1[0] , p1[1]- 1)
                    map[p1] = [255, 0, 0]
                    map_bin[p1] = 4
                    caminho.append(p1)
                else:
                    if (posS == 0):
                        p1 = (p1[0] + 1, p1[1])
                        map[p1] = [255, 0, 0]
                        map_bin[p1] = 4
                        caminho.append(p1)
                    else:
                        map[p1] = [255, 255, 0]
                        map_bin[p1] = 6
                        p1 = caminho.pop()
        #if cv2.waitKey(25) & 0xFF == ord('q'):
        #    cv2.destroyAllWindows()
        #    break
    return map,map_bin,caminho