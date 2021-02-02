import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
directory = 'C:\\Users\\Sasidhar Mankala\\Desktop\\pythonproject\\Images'
cam = cv2.VideoCapture(1)
cv2.namedWindow("test")
img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if k%256 == 32 :
        # SPACE pressed
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
        # img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h+8, x:x+w+8]
            crop = frame[y-8: y+h+8 , x-8: x+w+8]
        img_name = "{}.png".format(img_counter)
        image_path2 = os.path.join(directory,img_name)
        cv2.imwrite(image_path2, crop)
        print("{} written!".format(img_name))
        img_counter += 1
    elif k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
cam.release()

cv2.destroyAllWindows()