import cv2
import HandTrackingModule as htm
import Gestures

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.HandDetector(max_hands=1, detectionCon=0.5, trackCon=0.5)

fingerId = [4, 8, 12, 16, 20]
prevlist = list()
fingerCounter = 0


def gestureName(counter):
    switcher = {
        0: "Do a Gesture",
        1: "Play/Pause",
        2: "Volume Up",
        3: "Volume Down",
        4: "Mute",
        5: "Fast Forward",
        6: "Rewind",
        7: "FullScreen",
    }
    return switcher.get(counter, "Do a Gesture")


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)

    ges = Gestures.Gestures()
    img, prevlist, fingerCounter = ges.getGesture(img, lmlist, prevlist, fingerCounter)

    cv2.putText(img, gestureName(fingerCounter), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
