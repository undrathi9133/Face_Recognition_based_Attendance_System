from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        # Title Label
        title_lbl = Label(
            self.root,
            text="TRAIN DATA SET",
            font=("times new roman", 25, "bold"),
            bg="white",
            fg="green"
        )
        title_lbl.place(x=0, y=5, width=1530, height=45)

        
        #images in train data top image
        img_top = Image.open(r"college_images\train1.jpg")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl3 = Label(self.root, image=self.photoimg_top)
        f_lbl3.place(x=0, y=55, width=1530, height=325)

        # button
        train_btn = Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2",
            font=("times new roman", 25, "bold"),
            bg="light blue",
            fg="red",
            width=18
            )
        train_btn.place(x=0,y=380,width=1530,height=60)



        #images in train data buttom image
        img_buttom = Image.open(r"college_images\train2.png")
        img_buttom = img_buttom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_buttom = ImageTk.PhotoImage(img_buttom)
        
        f_lbl3 = Label(self.root, image=self.photoimg_buttom)
        f_lbl3.place(x=0, y=440, width=1530, height=325)

    # Function train classifier
    def train_classifier(self):
        try:
            data_dir = "Data"
            if not os.path.exists(data_dir):
                messagebox.showerror("Error", f"Data directory '{data_dir}' not found.")
                return

            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
            if not path:
                messagebox.showerror("Error", "No images found in the Data directory.")
                return

            faces = []
            ids = []

            for image in path:
                try:
                    img = Image.open(image).convert('L')  # Convert to grayscale
                    imageNp = np.array(img, 'uint8')
                    id = int(os.path.split(image)[1].split('.')[1])  # Extract user ID from file name

                    faces.append(imageNp)
                    ids.append(id)
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1)
                except Exception as e:
                    print(f"Skipping invalid image file: {image} ({str(e)})")

            ids = np.array(ids)

            # ===== Train the classifier and save =====
            if len(faces) == 0:
                messagebox.showerror("Error", "No valid images found for training.")
                return

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training datasets completed successfully!")
        except Exception as e:
            cv2.destroyAllWindows()
            messagebox.showerror("Error", f"An error occurred: {str(e)}")





if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()