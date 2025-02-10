from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np





class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")



        # Title Label
        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION",
            font=("times new roman", 25, "bold"),
            bg="white",
            fg="blue"
        )
        title_lbl.place(x=0, y=5, width=1530, height=45)


        #1st images in  top image
        img_face1 = Image.open(r"college_images\face8.jpg")
        img_face1 = img_face1.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_face1 = ImageTk.PhotoImage(img_face1)
        
        f_lbl3 = Label(self.root, image=self.photoimg_face1)
        f_lbl3.place(x=0, y=55, width=950, height=700)
        



        #images in 2nd image
        img_face2 = Image.open(r"college_images\face7.jpg")
        img_face2 = img_face2.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_face2 = ImageTk.PhotoImage(img_face2)
        
        f_lbl3 = Label(self.root, image=self.photoimg_face2)
        f_lbl3.place(x=950, y=55, width=650, height=700)

        # button
        train_btn = Button(self.root, text="Face Recognition",command=self.face_recog,cursor="hand2",
            font=("times new roman", 25, "bold"),
            bg="green",
            fg="blue",
            width=18
            )
        train_btn.place(x=1050,y=680,width=300,height=40)

    # ======= Attendance =======
    def mark_attendance(self, Student_id, rollno, name, department):
        try:
            with open("Ravi.csv", "r+", newline="\n") as f:
                myDataList = f.readlines()
                name_list = []

                for line in myDataList:
                    entry = line.split(",")  # Correct splitting by comma
                    name_list.append(entry[0])  # Add only Student_id for checking uniqueness

                # Check if the attendance for the student already exists
                if Student_id not in name_list:
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:%S")
                    f.writelines(f"{Student_id},{rollno},{name},{department},{dtString},{d1},Present\n")
                    print("Attendance marked successfully!")
                else:
                    print("Attendance already marked for this student.")
        except Exception as e:
            print(f"Error while marking attendance: {str(e)}")



    # ======== Face Recognition ========
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))  # Calculate confidence level

                try:
                    # Database connection
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="RRR@ravi$123",  # Use your MySQL password
                        database="face_recognizer"
                    )
                    mycursor = conn.cursor()

                    # Fetch student details based on `id`
                    mycursor.execute("SELECT std_id FROM student WHERE std_id = %s", (id,))
                    Student_id = mycursor.fetchone()
                    Student_id = "+".join(Student_id) if Student_id else "Unknown"


                    mycursor.execute("SELECT rollno FROM student WHERE std_id = %s", (id,))
                    rollno = mycursor.fetchone()
                    rollno = "+".join(rollno) if rollno else "Unknown"

                    mycursor.execute("SELECT std_name FROM student WHERE std_id = %s", (id,))
                    name = mycursor.fetchone()
                    name = "+".join(name) if name else "Unknown"

                    
                    mycursor.execute("SELECT dep FROM student WHERE std_id = %s", (id,))
                    department = mycursor.fetchone()
                    department = "+".join(department) if department  else "Unknown"

                    conn.close()

                    if confidence > 77:
                        # Display the details on the frame
                        cv2.putText(img, f"Student_Id: {Student_id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                        cv2.putText(img, f"Roll No: {rollno}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                        cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                        cv2.putText(img, f"Dept: {department}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)

                        # Call the attendance function
                        self.mark_attendance(Student_id, rollno, name, department)

                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                except Exception as e:
                    print(f"Database Error: {e}")
                    cv2.putText(img, "Database Error", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 0, 0), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
            return img

        # Load Haar Cascade and trained classifier
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()

        try:
            clf.read("classifier.xml")  # Load the trained model
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load classifier: {str(e)}")
            return

        video_cap = cv2.VideoCapture(0)  # Open the webcam

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to open webcam.")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()