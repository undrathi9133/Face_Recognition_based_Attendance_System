from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2





class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")


        # Title Label
        title_lbl = Label(
            self.root,
            text="DEVELOPER ",
            font=("times new roman", 30, "bold"),
            bg="white",
            fg="blue"
        )
        title_lbl.place(x=0, y=0, width=1530, height=50)





        #bg image
        DEV = Image.open(r"college_images\atten4.png")
        DEV = DEV.resize((1530, 710), Image.Resampling.LANCZOS)
        self.bg_dev = ImageTk.PhotoImage(DEV)
        bg_dev = Label(self.root, image=self.bg_dev)
        bg_dev.place(x=0, y=55, width=1530, height=710)

        # Main Frame
        main_frame = Frame(bg_dev, bd=2, relief=RIDGE)
        main_frame.place(x=50, y=0, width=550, height=700)


        # left label image
        dev = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\mine.jpg")
        dev = dev.resize((540, 350), Image.Resampling.LANCZOS)
        self.photodev = ImageTk.PhotoImage(dev)
        
        f_lbl3 = Label(bg_dev, image=self.photodev)
        f_lbl3.place(x=55, y=20, width=540, height=350)


        #left  Label
        title_lbl = Label(bg_dev,
            text="PROJECT DEVELOPER ",
            font=("times new roman", 30, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=55, y=370, width=540, height=50)

        #left  Label
        title_lbl = Label(bg_dev,
            text="I am Ravi Teja From KMEC 4th Year Student",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=55, y=420, width=540, height=50)

        #left  Label
        title_lbl = Label(bg_dev,
            text="This is my major project",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=55, y=470, width=540, height=50)
        #left  Label
        title_lbl = Label(bg_dev,
            text="my team members are omkali and varun",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=55, y=520, width=540, height=50)

        #left  Label
        title_lbl = Label(bg_dev,
            text="It is Python project",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=55, y=570, width=540, height=50)

        #left  Label
        title_lbl = Label(bg_dev,
            text="thank you",
            font=("times new roman", 18, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=55, y=620, width=540, height=50)

        










if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
