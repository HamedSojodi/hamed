
#
# import cv2
# from cvzone.HandTrackingModule import HandDetector
#
# cap = cv2.VideoCapture(1)
# detector = HandDetector(detectionCon=0.8, maxHands=2)
# while (True):
#     success, img = cap.read()
#     hands, ima = detector.findHands(img)
#
#     if hands:
#         hand1 = hands[0]
#         lmList1 = hand1["lmList"]
#         bbox1 = hand1["bbox"]
#         centerpoint1 = hand1["center"]
#
#         fingers1 = detector.fingersUp(hand1)
#         # length, info, img = detector.findDistance(lmList1[4], lmList1[8], ima)
#
#     if len(hands) == 2:
#         hand2 = hands[1]
#         lmList2 = hand2["lmList"]
#         bbox2 = hand2["bbox"]
#         centerpoint2 = hand2["center"]
#
#         fingers2 = detector.fingersUp(hand2)
#         length, info, img = detector.findDistance(lmList1[8], lmList2[8], ima)
#
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)
#
#
#















import numpy as np
import cv2

cascPath = "haarcascade_frontalface_default.xml"
cma = cv2.VideoCapture(1)

faceCascade = cv2.CascadeClassifier(cascPath)
while (True):
    ret, img = cma.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = faceCascade.detectMultiScale(gray, 1.8, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Faces found", img)
    if cv2.waitKey(1) == ord('q'):
        break
cma.release()
cv2.destroyAllWindows()




# imagePath = 'h.jpg'
# cascPath = "haarcascade_frontalface_default.xml"
#
# faceCascade = cv2.CascadeClassifier(cascPath)
#
# image = cv2.imread(imagePath)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
# faces = faceCascade.detectMultiScale(
#     gray,
#     scaleFactor=1.1,
#     minNeighbors =5,
#     minSize=(30, 30)
# )
# print("Found {0} faces!".format(len(faces)))
# # Draw a rectangle around the faces
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
# cv2.imshow("Faces found", image)
# cv2.waitKey(0)
