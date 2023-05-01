import numpy as np
import cv2
import pymysql
import CNN

# db dictionary
dic = {
    '0':'yet',
    '1':'yet',
    '2':'20181234',
    # george w bush
    '3':'20194311',
    '4':'20201376',
    '5':'20222133',
    # colin powell
    6:'20180233'
}

# load face_detection xml
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# object
cap = cv2.VideoCapture(0)

# width, height
cap.set(3,640)
cap.set(4,480)

while True:
    # detect face
    ret, img = cap.read()
    
    img = cv2.flip(img, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20,20))

    for(x, y, w, h) in faces:
        cv2.rectangle (img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
    cv2.imshow('video', img)

    # capture and cropping
    if cv2.waitKey(10)& 0xff == ord('q'):
        for (x, y, w, h) in faces:
            cropped = img[y:y+h, x:x+w]
            path = '/home/yu/Raspberry/temp/save_img.jpeg'
            # cv2.imwrite(path, cropped)
        predict = CNN.cnn_predict(path)
        print(predict)
            
        sql = "select name from student_info where id = {}" .format(dic[predict])
       
        # connect db
        db_list = []
        conn = pymysql.connect(host='localhost', user='root', password='', db='info')
            
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                result = cur.fetchall()
                for data in result:
                    db_list.append(data)
                    
            for i in db_list:
                print(i)
            
    # stop process
    if cv2.waitKey(10) & 0xff == ord('x'):
        cap.release()
        cv2.destroyAllWindows()
        
#cap.release()
#cv2.destroyAllWindows()
