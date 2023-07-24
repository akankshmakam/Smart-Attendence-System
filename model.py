import face_recognition
import cv2
import numpy as np
import os
from datetime import date,datetime,timedelta
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='6768', port='3306', database='attendence')
mycursor = mydb.cursor()

today = datetime.now()
formatted_date = today.strftime('%Y-%m-%d %H:%M:%S')

path = 'faces'
images = []
classNames = []

mylist = os.listdir(path)
print(mylist)
for cl in mylist:
    curimg = cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def encodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

encodelistKnown = encodings(images)
print("Encoding Complete...")

#webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations((imgS))
    encodeCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceloc in zip(encodeCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodelistKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodelistKnown,encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceloc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            add_people = "INSERT INTO khacks (Register_Number, Name, Entry) VALUES (%s, %s, %s)"
            students = ('URK21CS1181', name, formatted_date)
            mycursor.execute(add_people, students)
            student_details = mycursor.lastrowid
            mydb.commit()

        else:
            print('error')


    cv2.imshow('Image',img)
    cv2.waitKey(1)



