import pyautogui as p


class Gestures:
    def __init__(self):
        self.fingerId = [4, 8, 12, 16, 20]
        self.tipValues = list()

    def getGesture(self, img, lmlist, prevlist, counter):

        if len(lmlist) != 0:
            if lmlist[self.fingerId[0]][1] > lmlist[self.fingerId[0] - 2][1]:
                self.tipValues.append(True)
            else:
                self.tipValues.append(False)
            for index in range(1, 5):
                print(self.fingerId[index], self.fingerId[index] - 2)
                print(lmlist[self.fingerId[index]][2], lmlist[self.fingerId[index] - 2][2])
                if lmlist[self.fingerId[index]][2] < lmlist[self.fingerId[index] - 2][2]:
                    self.tipValues.append(True)
                else:
                    self.tipValues.append(False)

            # print(self.tipValues)

        if len(self.tipValues) != 0 and prevlist != self.tipValues:
            # PLAY/PAUSE
            if self.tipValues[0] and self.tipValues[1] and self.tipValues[2] and self.tipValues[3] and \
                    self.tipValues[4]:
                p.press("space")
                counter = 1
            # VOLUME UP
            if self.tipValues[1] and not self.tipValues[2] and not self.tipValues[3] and not self.tipValues[4]:
                p.hotkey("ctrl", "up")
                counter = 2
            # VOLUME DOWN
            if not self.tipValues[1] and not self.tipValues[2] and not self.tipValues[3] and self.tipValues[4]:
                p.hotkey("ctrl", "down")
                counter = 3
            # MUTE
            if self.tipValues[1] and not self.tipValues[2] and not self.tipValues[3] and self.tipValues[4]:
                p.press("m")
                counter = 4
            # FAST FORWARD
            if self.tipValues[0] and self.tipValues[1] and self.tipValues[2] and not self.tipValues[3] and \
                    not self.tipValues[4]:
                p.hotkey("alt", "right")
                counter = 5
            # REWIND
            if not self.tipValues[1] and self.tipValues[2] and self.tipValues[3] and self.tipValues[4]:
                p.hotkey("alt", "left")
                counter = 6
            # FullScreen
            if not self.tipValues[0] and self.tipValues[1] and self.tipValues[2] and self.tipValues[3] and \
                    self.tipValues[4]:
                p.press("f")
                counter = 7

        return img, self.tipValues, counter

        # if lmlist[4][2] < lmlist[2][2]:
        #     thumbFinger = True
        # else:
        #     thumbFinger = False
        # if lmlist[8][2] < lmlist[6][2]:
        #     indexFinger = True
        # else:
        #     indexFinger = False
        # if lmlist[12][2] < lmlist[10][2]:
        #     middleFinger = True
        # else:
        #     middleFinger = False
        # if lmlist[16][2] < lmlist[14][2]:
        #     ringFinger = True
        # else:
        #     ringFinger = False
        # if lmlist[20][2] < lmlist[18][2]:
        #     pinkyFinger = True
        # else:
        #     pinkyFinger = False
