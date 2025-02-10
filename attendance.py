from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog







mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")

        #=====variables ========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        # Load and resize the 1st image
        img = Image.open(r"college_images\atten1.jpg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Load and resize the 2nd image
        img1 = Image.open(r"college_images\atten3.png")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg2)
        f_lbl1.place(x=800, y=0, width=800, height=200)

        #bg image
        img3 = Image.open(r"college_images\atten4.png")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.bg_photoimg = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.bg_photoimg)
        bg_img.place(x=0, y=200, width=1530, height=710)

        

        # Title Label
        title_lbl = Label(
            bg_img,
            text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",
            font=("times new roman", 25, "bold"),
            bg="white",
            fg="blue"
        )
        title_lbl.place(x=0, y=0, width=1530, height=50)


        # Main Frame
        main_frame = Frame(bg_img, bd=2, relief=RIDGE)
        main_frame.place(x=10, y=50, width=1505, height=650)

        # Left Label Frame
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 12, "bold")
        )
        Left_frame.place(x=10, y=10, width=740, height=580)


        img4 = Image.open(r"college_images\atten4.png")
        img4 = img4.resize((740, 130), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        f_lbl3 = Label(self.root, image=self.photoimg4)
        f_lbl3.place(x=35, y=300, width=720, height=130)

        # LEFT inside Frame
        left_inside_frame = Frame(bg_img, bd=2, relief=RIDGE)
        left_inside_frame.place(x=25, y=230, width=730, height=300)




        #Attendance label
        Attendance_ID = Label(left_inside_frame,text="Attendance_ID:",bg="white",font=("times new roman", 12, "bold"))
        Attendance_ID.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Attendance_ID_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman", 12, "bold"))
        Attendance_ID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        roll_no = Label(left_inside_frame,text="Roll NO:",bg="white",font=("comicsansns 11 bold"))
        roll_no.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("comicsansns 11 bold"))
        roll_no_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Name
        Name = Label(left_inside_frame,text="Name:",bg="white",font=("comicsansns 11 bold"))
        Name.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Name_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("comicsansns 11 bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        '''div_combo=ttk.Combobox(left_inside_frame, state="readonly",width=15)
        div_combo["values"]=("select division","A","B","C","D ")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)'''

        #department
        sdep = Label(left_inside_frame,text="Department:", bg="white",font=("comicsansns 11 bold"))
        sdep.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        sdep_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep,font=("comicsansns 11 bold"))
        sdep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Time
        time = Label(left_inside_frame,text="Time:",bg="white",font=("comicsansns 11 bold"))
        time.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("comicsansns 11 bold"))
        time_entry.grid(row=2,column=1,padx=10,sticky=W)

        '''gender_combo=ttk.Combobox(left_inside_frame, state="readonly",width=15)
        gender_combo["values"]=("select gender","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)'''

        #Date
        date = Label(left_inside_frame, text="Date:",bg="white",font=("comicsansns 11 bold"))
        date.grid(row=2,column=2,padx=10,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("comicsansns 11 bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attenace
        attend1 = Label(left_inside_frame,text="Attendance Status:",bg="white",font=("comicsansns 11 bold"))
        attend1.grid(row=3,column=0,padx=10,pady=5,sticky=W)


        attend1=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance, state="readonly",width=15)
        attend1["values"]=("select", "Present",  "Absent")
        attend1.current(0)
        attend1.grid(row=3,column=1,padx=10,pady=5,sticky=W)



        #buttons frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=205,width=750,height=35)

        #import button
        save_btn = Button(btn_frame,command=self.importCsv, text="Import csv",
            font=("times  new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=17
            )

        save_btn.grid(row=0,column=0)

        #export  
        update_btn= Button(btn_frame,command=self.exportCsv,
            text="Export csv",
            font=("times  new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=17
            )
        update_btn.grid(row=0,column=1)

        #Update button
        delete_btn= Button(btn_frame,
            text="Update",
            font=("times  new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=17
            )
        delete_btn.grid(row=0,column=2)

        #reset button
        reset_btn= Button(btn_frame,command=self.reset_data,
            text="Reset",
            font=("times  new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=18
            )
        reset_btn.grid(row=0,column=3)





        # Right Label Frame
        Right_frame = LabelFrame(main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 12, "bold")
        )
        Right_frame.place(x=755, y=10, width=740, height=580)


        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=10,width=730,height=455)


        #=== scroll bar table ==========================
        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")


        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)



        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)






    # ============ fetch data ============

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #====import csv ============
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")) ,parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    #=======export csv ========
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data ","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")) ,parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully")

        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



    def get_cursor(self, event=""):
        # Get the currently selected row
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']  # Corrected typo from 'vales' to 'values'

        if rows:  # Ensure rows is not empty
            self.var_atten_id.set(rows[0])          # Attendance ID
            self.var_atten_roll.set(rows[1])        # Roll number
            self.var_atten_name.set(rows[2])        # Name (fixed typo)
            self.var_atten_dep.set(rows[3])         # Department
            self.var_atten_time.set(rows[4])        # Time
            self.var_atten_date.set(rows[5])        # Date
            self.var_atten_attendance.set(rows[6])  # Attendance status



    def reset_data(self):
        # Ensure rows is not empty
        self.var_atten_id.set("")         # Attendance ID
        self.var_atten_roll.set("")        # Roll number
        self.var_atten_name.set("")        # Name (fixed typo)
        self.var_atten_dep.set("")         # Department
        self.var_atten_time.set("")        # Time
        self.var_atten_date.set("")        # Date
        self.var_atten_attendance.set("")  # Attendance status














 
 






if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()