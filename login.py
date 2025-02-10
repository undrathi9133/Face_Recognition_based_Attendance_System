from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from PIL import ImageDraw
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\bg3.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Get the screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Open and resize the background image
        bg_image = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\bg2.jpg")
        bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)

        # Set the resized image as the background
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)


        # Frame for Login
        frame = Frame(self.root, bg="light blue")
        frame.place(x=600, y=120, width=340, height=500)

        # Round User Icon
        img1 = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\14.jpeg")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)

        # Create a circular mask
        mask = Image.new("L", img1.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img1.size[0], img1.size[1]), fill=255)

        # Apply the mask to make the image round
        img1.putalpha(mask)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        # User Icon Placement
        lblimg1 = Label(image=self.photoimage1, bg="light blue", borderwidth=0)
        lblimg1.place(x=720, y=140, width=100, height=100)

        # Title
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="light blue")
        get_str.place(x=95, y=110)

        # Username Label and Entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="light blue")
        username.place(x=50, y=150)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password Label and Entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="light blue")
        password.place(x=50, y=230)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=260, width=270)

        # Buttons Placement
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                        bd=3, relief=RIDGE, fg="white", bg="red", activebackground="red", activeforeground="white")
        loginbtn.place(x=40, y=310, width=270, height=35)

        registerbtn = Button(frame, text="Register", command=self.register_window, font=("times new roman", 10, "bold"),
                            borderwidth=0, fg="white", bg="black", activebackground="black", activeforeground="white")
        registerbtn.place(x=40, y=360, width=270, height=30)

        f_passbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"),
                        borderwidth=0, fg="white", bg="black", activebackground="black", activeforeground="white")
        f_passbtn.place(x=40, y=400, width=270, height=30)

        
    def login(self):
        # Handle Login Functionality
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="RRR@ravi$123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "SELECT * FROM users WHERE username=%s AND password=%s",
                    (self.txtuser.get(), self.txtpass.get())
                )
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    open_main=messagebox.showinfo("Success", "Welcome!", parent=self.root)
                    if open_main:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                
                #conn.close()
           
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)




    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("400x400+400+200")

        # Title
        title = Label(self.root, text="Register Here", font=("times new roman", 20, "bold"), fg="green", bg="white")
        title.pack(side=TOP, fill=X)

        # Fields
        lbl_username = Label(self.root, text="Username", font=("times new roman", 15, "bold"))
        lbl_username.place(x=50, y=80)
        self.entry_username = ttk.Entry(self.root, font=("times new roman", 15, "bold"))
        self.entry_username.place(x=50, y=110, width=250)

        lbl_password = Label(self.root, text="Password", font=("times new roman", 15, "bold"))
        lbl_password.place(x=50, y=150)
        self.entry_password = ttk.Entry(self.root, font=("times new roman", 15, "bold"), show="*")
        self.entry_password.place(x=50, y=180, width=250)

        lbl_confirm_password = Label(self.root, text="Confirm Password", font=("times new roman", 15, "bold"))
        lbl_confirm_password.place(x=50, y=220)
        self.entry_confirm_password = ttk.Entry(self.root, font=("times new roman", 15, "bold"), show="*")
        self.entry_confirm_password.place(x=50, y=250, width=250)

        # Register Button
        register_btn = Button(self.root, text="Register", command=self.register_data, font=("times new roman", 15, "bold"),
                              bg="green", fg="white")
        register_btn.place(x=50, y=300, width=250)

    def register_data(self):
        if self.entry_username.get() == "" or self.entry_password.get() == "" or self.entry_confirm_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.entry_password.get() != self.entry_confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="RRR@ravi$123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO users (username, password) VALUES (%s, %s)",
                    (self.entry_username.get(), self.entry_password.get())
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                self.root.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
