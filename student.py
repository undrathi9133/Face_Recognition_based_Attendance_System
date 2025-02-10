from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2





class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")

        #========= variables ========
        self.var_dep=StringVar()
        #self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_section=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       


        # Load and resize the 1st image
        img = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\student1.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Load and resize the 2nd image
        img1 = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\student2.jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg2)
        f_lbl1.place(x=500, y=0, width=530, height=130)

        # Load and resize the 3rd image
        img2 = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\student3.jpeg")
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg3)
        f_lbl2.place(x=1000, y=0, width=550, height=130)

        # Load and resize the background image
        img3 = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\studentbg.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.bg_photoimg = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.bg_photoimg)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title Label
        title_lbl = Label(
            bg_img,
            text="STUDENT MANAGEMENT SYSTEM",
            font=("times new roman", 25, "bold"),
            bg="white",
            fg="blue"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)
 
 
 
 
 
 
 
        # Main Frame
        main_frame = Frame(bg_img, bd=2, relief=RIDGE)
        main_frame.place(x=10, y=50, width=1505, height=650)

        # Left Label Frame
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold")
        )
        Left_frame.place(x=10, y=10, width=740, height=580)

        # left label image
        img4 = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\23.jpg")
        img4 = img4.resize((740, 130), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        f_lbl3 = Label(self.root, image=self.photoimg4)
        f_lbl3.place(x=40, y=230, width=700, height=130)

        # current course
        current_course_frame = LabelFrame(Left_frame,
            bd=2,
            relief=RIDGE,
            text="Current Course Information",
            font=("times  new roman", 12, "bold")
        )
        current_course_frame.place(x=5, y=150, width=720, height=150)

        #department
        dep_label = Label(current_course_frame,
           text="Department",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        dep_label.grid(row=0,column=0 ,padx=10)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times  new roman", 12, "bold"),state="readonly",width=17)
        dep_combo["values"]=("select department","CSE","CSM","IT","CS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        #course
        '''course_label = Label(current_course_frame,
           text="Course",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        course_label.grid(row=1,column=2 ,padx=10)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times  new roman", 12, "bold"),state="readonly",width=17)
        course_combo["values"]=("select course","BE","BSC","BCOM")
        course_combo.current(0)
        course_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)'''


        

        #YEAR
        year_label = Label(current_course_frame,
           text="Year",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        year_label.grid(row=0,column=2 ,padx=10)
        div_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times  new roman", 12, "bold"),state="readonly",width=17)
        div_combo["values"]=("select year","I","II","III","IV  ")
        div_combo.current(0)
        div_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #semester
        sem_label = Label(current_course_frame,
           text="Semester",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        sem_label.grid(row=1,column=0,padx=10)
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times  new roman", 12, "bold"),state="readonly",width=17)
        sem_combo["values"]=("select semister","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #section
        section_label = Label(current_course_frame,
           text="Section",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        section_label.grid(row=1,column=2,padx=10)
        section_combo=ttk.Combobox(current_course_frame,textvariable=self.var_section, font=("times  new roman", 12, "bold"),state="readonly",width=17)
        section_combo["values"]=("select section","A","B","C")
        section_combo.current(0)
        section_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        


        # Student information
        class_student_frame = LabelFrame(Left_frame,
            bd=2,
            relief=RIDGE,
            text="Class Student Information",
            font=("times  new roman", 12, "bold")
        )
        class_student_frame.place(x=5, y=250, width=720, height=300)
         
        #studentID
        studentID = Label(class_student_frame,
           text="StudentId:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        studentID.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #studentName
        studentname = Label(class_student_frame,
           text="Student Name:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        studentname.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #studentDivision
        studentdivision = Label(class_student_frame,
           text="Student Division:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        studentdivision.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        '''studentdivision_entry = ttk.Entry(class_student_frame,textvariable=self.var_div,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentdivision_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)'''

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("times  new roman", 12, "bold"),state="readonly",width=15)
        div_combo["values"]=("select division","A","B","C","D ")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll no
        student_rollno = Label(class_student_frame,
           text="Roll no:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        student_rollno.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentrollno_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentrollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #GENDER
        studentgender = Label(class_student_frame,
           text="Gender:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        studentgender.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        '''studentgender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentgender_entry.grid(row=2,column=1,padx=10,sticky=W)'''

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times  new roman", 12, "bold"),state="readonly",width=15)
        gender_combo["values"]=("select gender","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date of birth
        studentDOB = Label(class_student_frame,
           text="DOB:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        studentDOB.grid(row=2,column=2,padx=10,sticky=W)

        studentDOB_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentDOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email..
        studentemail = Label(class_student_frame,
           text="Student Email:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        studentemail.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentemail_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentemail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone number
        studentcellno = Label(class_student_frame,
           text="Student phone no:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        studentcellno.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentcellno_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentcellno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #student address
        studentaddress = Label(class_student_frame,
           text="Student Address:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        studentaddress.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentaddress_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentaddress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #Teacher name
        studentmadam = Label(class_student_frame,
           text="Teacher:",
           bg="white",
           font=("times  new roman", 12, "bold")
        )
        studentmadam.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studentmadam_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,
            width=20,
            font=("times  new roman", 12, "bold")
            )
        studentmadam_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1 =ttk.Radiobutton(class_student_frame,variable=self.var_radio1,
            text="Take Photo Sample",
            value="Yes"
            )
        radiobtn1.grid(row=5,column=0)
        
        #self.var_radio2=StringVar()
        radiobtn2 =ttk.Radiobutton(class_student_frame,variable=self.var_radio1,
            text="No Photo Sample",
            value="No"
            )
        radiobtn2.grid(row=5,column=1)

        #buttons frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=205,width=750,height=35)

        #save button
        save_btn = Button(btn_frame, text="Save",command=self.add_data,
            font=("times  new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=18
            )

        save_btn.grid(row=0,column=0)

        #update 
        update_btn= Button(btn_frame,
            text="Update",
            font=("times  new roman", 13, "bold"),command=self.update_data,
            bg="blue",
            fg="white",
            width=18
            )
        update_btn.grid(row=0,column=1)

        #delete button
        delete_btn= Button(btn_frame,
            text="Delete",
            font=("times  new roman", 13, "bold"),command=self.delete_data,
            bg="blue",
            fg="white",
            width=18
            )
        delete_btn.grid(row=0,column=2)

        #reset button
        reset_btn= Button(btn_frame,
            text="Reset",
            font=("times  new roman", 13, "bold"),command=self.reset_data,
            bg="blue",
            fg="white",
            width=18
            )
        reset_btn.grid(row=0,column=3)


        #buttons frame
        btn2_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn2_frame.place(x=0,y=240,width=750,height=35)

        #save photo button
        save_photo_btn= Button(btn2_frame,command=self.generate_data,
            text="Save photo",
            font=("times  new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=36
            )
        save_photo_btn.grid(row=0,column=0)


        #Update photo button
        update_photo_btn= Button(btn2_frame,
            text="Update photo",
            font=("times  new roman", 13, "bold"),
            bg="blue",
            fg="white",
            width=36
            )
        update_photo_btn.grid(row=0,column=1)


        



        




        # Right Label Frame
        Right_frame = LabelFrame(main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold")
        )
        Right_frame.place(x=755, y=10, width=740, height=580)

        # left label image
        img_right = Image.open(r"C:\Users\RAVITEJA\OneDrive\Documents\Desktop\Face_Recognition_System\college_images\right1.jpeg")
        img_right = img_right.resize((740, 130), Image.Resampling.LANCZOS)
        self.photoimgright = ImageTk.PhotoImage(img_right)
        f_lblright = Label(Right_frame , image=self.photoimgright)
        f_lblright.place(x=10, y=10, width=720, height=140)


        #=========Search System ==========#
        # Student information
        search_frame = LabelFrame(Right_frame,
            bd=2,
            relief=RIDGE,
            text="Search System ",
            font=("times  new roman", 12, "bold")
        )
        search_frame.place(x=5, y=150, width=720, height=70)

         #phone number
        search_label = Label(search_frame,
           text="Search By:",
           bg="red",
           fg="white",
           font=("times  new roman", 12, "bold")
        )
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame, font=("times  new roman", 13, "bold"),state="readonly",width=15)
        search_combo["values"]=("select ","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(search_frame,
            text="Show All",
            width=12,
            font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",width=12,
            font=("times new roman",13,"bold"),
            bg="blue",
            relief=RIDGE
            )
        search_btn.grid(row=0,column=3,padx=4)

        '''showall_btn = Button(search_frame,text="Search",width=12,
            font=("times new roman",13,"bold"),
            bg="blue",
            relief=RIDGE
            )
        showall_btn.grid(row=0,column=4,padx=4)'''

        # table frame 
        table_frame = Frame(Right_frame,
            bd=2,
            relief=RIDGE,
            bg="white"
        )
        table_frame.place(x=5, y=215, width=720, height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column = ("dep","course","year","sem",
            "id","name","div","roll","gender","dob","email","phone","address",
            "teacher","photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #====== function declaration  =========

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get() =="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are requiered",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="RRR@ravi$123",  # Use your MySQL password
                    database="face_recognizer"
                                                )

                mycursor=conn.cursor()
                mycursor.execute("INSERT into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                              self.var_dep.get(),
                                                                                                              #self.var_course.get(),
                                                                                                              self.var_year.get(),
                                                                                                              self.var_semester.get(),
                                                                                                              self.var_section.get(),
                                                                                                              self.var_std_id.get(),
                                                                                                              self.var_std_name.get(),
                                                                                                              self.var_div.get(),
                                                                                                              self.var_roll.get(),
                                                                                                              self.var_gender.get(),
                                                                                                              self.var_dob.get(),
                                                                                                              self.var_email.get(),
                                                                                                              self.var_phone.get(),
                                                                                                              self.var_address.get(),
                                                                                                              self.var_teacher.get(),
                                                                                                              self.var_radio1.get(),
                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




    #===========fetch data============
    def fetch_data(self):
        conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="RRR@ravi$123",  # Use your MySQL password
                    database="face_recognizer"
                                                )

        mycursor=conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
        


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #==============get cursor==========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_section.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    #update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                 # Confirmation prompt
                 Update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                 if Update:
                    # Establish database connection
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="RRR@ravi$123",
                        database="face_recognizer"
                           )
                    mycursor = conn.cursor()

                    #  Correct SQL query with backticks for `div`
                    query = """
                    UPDATE student 
                    SET dep=%s, year=%s, semester=%s, section=%s, std_name=%s, `div`=%s, 
                    rollno=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, 
                    teacher=%s, photosample=%s 
                    WHERE std_id=%s
                    """
                    values = (
                       self.var_dep.get(),
                       self.var_year.get(),
                       self.var_semester.get(),
                       self.var_section.get(),
                       self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()  # `std_id` is used in the WHERE condition
                        )

                        # Execute query
                    mycursor.execute(query, values)

                    # Commit changes
                    conn.commit()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)

                    # Refresh table data
                    self.fetch_data()

                    # Close connection
                    conn.close()
                 else:
                     return
            except Exception as es:
                    messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    # Delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be provided", parent=self.root)
        else:
            try:
                # Confirm delete operation
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
                if delete:
                    # Connect to the database
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="RRR@ravi$123",  # Replace with your MySQL password
                        database="face_recognizer"
                    )
                    mycursor = conn.cursor()

                    # SQL query to delete the student record
                    sql = "DELETE FROM student WHERE std_id = %s"
                    val = (self.var_std_id.get(),)  # Ensure `self.var_std_id.get()` is called correctly
                    mycursor.execute(sql, val)

                    conn.commit()  # Commit changes to the database
                    conn.close()   # Close the connection
                    
                    # Refresh the table data
                    self.fetch_data()

                    # Inform the user about successful deletion
                    messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    # reset function
    def reset_data(self):
        self.var_dep.set("select department")
        self.var_year.set("select year")
        self.var_semester.set("select semester")
        self.var_section.set("select section")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("select division")
        self.var_roll.set("")
        self.var_gender.set("select gender ")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ======= Generate data set or Take photo Samples ==========
    def generate_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Establish database connection
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="RRR@ravi$123",  # Use your MySQL password
                    database="face_recognizer"
                )
                mycursor = conn.cursor()

                # Update or insert student details in the database
                query = """
                            UPDATE student 
                            SET dep=%s, year=%s, semester=%s, section=%s, std_name=%s, `div`=%s, 
                            rollno=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, 
                            teacher=%s, photosample=%s 
                            WHERE std_id=%s
                            """

                values = (
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_section.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    "Yes",  # Indicating photo samples are available
                    self.var_std_id.get()
                )

                mycursor.execute(query, values)
                conn.commit()
                conn.close()

                # ====== Load pre-defined data on face frontals from OpenCV ======
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                # Define face_cropped function
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    # If no face detected, return None
                    if len(faces) == 0:
                        return None

                    for (x, y, w, h) in faces:
                        cropped_face = img[y:y + h, x:x + w]
                        return cropped_face

                # Start capturing images from the webcam
                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, myframe = cap.read()
                    if not ret:
                        messagebox.showerror("Error", "Failed to access the camera", parent=self.root)
                        break

                    cropped_face = face_cropped(myframe)

                    if cropped_face is not None:  # Check if a face is detected
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{self.var_std_id.get()}.{img_id}.jpg"

                        # Save the image to the directory
                        cv2.imwrite(file_name_path, face)

                        # Display feedback on the window
                        cv2.putText(
                            face, f"Image {img_id}", (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2
                        )
                        cv2.imshow("Cropped Face", face)

                    

                    # Exit condition: Press 'Enter' or save 100 images
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo(
                    "Result", 
                    f"Dataset generation completed successfully! {img_id} images captured."
                )
            
            except Exception as es:
                        messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()


    
