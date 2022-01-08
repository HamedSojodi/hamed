import cv2
capture= cv2.VideoCapture(0)
if not capture.isOpened():
    raise IOError('can not open webcam')
while(True):
    ret,frame =capture.read()
    cv2.imshow('input', frame)
    c=cv2.waitKey(1)
    if c==27:
        break
capture.relaese()
cv2.destroyAllWindows()
