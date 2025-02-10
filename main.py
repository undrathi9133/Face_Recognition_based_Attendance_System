from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter
import os
from tkinter import Label
from time import strftime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")

        # Load and resize the 1st image
        img = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\1.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Load and resize the 2nd image
        img1 = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\2.jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg2)
        f_lbl1.place(x=500, y=0, width=530, height=130)

        # Load and resize the 3rd image
        img2 = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\3.webp")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg3)
        f_lbl2.place(x=1000, y=0, width=550, height=130)

        # Load and resize the background image
        img3 = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\background.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.bg_photoimg = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.bg_photoimg)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title Label
        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION BASED ATTENDANCE SYSTEM ",
            font=("times new roman", 25, "bold"),
            bg="white",
            fg="red"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)



        lbl = Label(self.root, font=("times new roman", 20, "bold"), bg="white", fg="blue")
        lbl.place(x=0, y=145, width=330, height=30)


        def time():
            string = strftime('%H:%M:%S %p')  # Get the current time
            lbl.config(text=string)           # Update the label's text
            lbl.after(1000, time)             # Schedule the function to run again after 1 second

            # Call the time function to start the clock
        time()






        # Student Button
        img4 = Image.open(r"college_images\6.jpeg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=320,width=220,height=40)


        # Face Detector Button
        img5 = Image.open(r"college_images\22.jpeg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, command=self.face_data, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)

        b2_1 = Button(
            bg_img,
            text="Face Detector",command=self.face_data,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white"
        )
        b2_1.place(x=500, y=320, width=220, height=40)


        # Attendance Button
        img6 = Image.open(r"college_images\5.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, command=self.attendance_data, cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        b3_1 = Button(
            bg_img,
            text="Attendance",command=self.attendance_data,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white"
        )
        b3_1.place(x=800, y=320, width=220, height=40)


        # Help Desk Button
        img7 = Image.open(r"college_images\4.jpeg")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b2 = Button(bg_img, image=self.photoimg7, command=self.help_data, cursor="hand2")
        b2.place(x=1100, y=100, width=220, height=220)

        b2_1 = Button(
            bg_img,
            text="Help Desk",command=self.help_data,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white"
        )
        b2_1.place(x=1100, y=320, width=220, height=40)


        # Train face Button
        img8 = Image.open(r"college_images\9.jpeg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, command=self.train_data, cursor="hand2",)
        b5.place(x=200, y=380, width=220, height=220)

        b5_1 = Button(
            bg_img,
            text="Train Data",command=self.train_data,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white"
        )
        b5_1.place(x=200, y=580, width=220, height=40)

         
        # Photos Button
        img9 = Image.open(r"college_images\13.jpeg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, command=self.open_img, cursor="hand2")
        b6.place(x=500, y=380, width=220, height=220)

        b6_1 = Button(
            bg_img,
            text="Photos",command=self.open_img,          #command=self.Photos,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white"
        )
        b6_1.place(x=500, y=580, width=220, height=40)


        #Developer Button
        img11 = Image.open(r"college_images\14.jpeg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b11 = Button(bg_img, image=self.photoimg11, command=self.developer_data, cursor="hand2")
        b11.place(x=800, y=380, width=220, height=220)

        b11_1 = Button(
            bg_img,
            text="Developer",command=self.developer_data,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white"
        )
        b11_1.place(x=800, y=580, width=220, height=40)


        #Exit face Button
        img12 = Image.open(r"college_images\15.jpeg")
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b12 = Button(bg_img, image=self.photoimg12, command=self.iExit, cursor="hand2")
        b12.place(x=1100, y=380, width=220, height=220)

        b12_1 = Button(
            bg_img,
            text="Exit",command=self.iExit,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="blue",
            fg="white"
        )
        b12_1.place(x=1100, y=580, width=220, height=40)



        #========function buttons ======
    
    def student_button_clicked(self):
        print("Student button clicked!")

    def Face_Detector(self):
        print("Face Detector clicked!")

    def Attendance(self):
        print("Attendance clicked!")

    def Help_Desk(self):
        print("Help Desk clicked!")

    def Train_Data(self):
        print("Train Data button clicked!")

    def Photos(self):
        print("photos button clicked!")

    def Developer(self):
        print("Developer button clicked!")

    def Exit(self):
        print("Exit button clicked!")


    def open_img(self):
        os.startfile("Data")


    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project?", parent=self.root)
        if iExit:
            self.root.destroy()  # Corrected method to properly close the window
        else:
            return





    #========function buttons ======
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)














    



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
