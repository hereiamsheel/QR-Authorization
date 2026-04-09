#-----------------------------------
# This is the test file for QR Code 
#-----------------------------------
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time

#img = cv2.imread('image.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:

    success, img = cap.read()
    img = cv2.flip(img,1)
    start = time.time()

    for barcode in decode(img):
        #print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img, [pts], True, (255,255,255), 5)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)

    end = time.time()
    fps = 1 / (end - start)
    start = end
    cv2.putText(img, "FPS: " + str(int(fps)), 
                (30, 50), 
                cv2.FONT_HERSHEY_PLAIN, 
                1, (25, 255, 25), 2)
    
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  
cv2.destroyAllWindows() 

