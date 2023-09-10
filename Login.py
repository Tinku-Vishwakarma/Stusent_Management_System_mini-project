from cProfile import label
from email.mime import image
from msilib.schema import ComboBox
from operator import le
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

def main():
    win=Tk()
    obj=Login(win)
    win.mainloop()
    
class Login():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System Login Form")
        self.root.geometry("1530x790+-7+0")

        # Background image
        img_1=Image.open(r"College_photo\university.jpg")
        img_1=img_1.resize((1530,790),Image.Resampling.HAMMING)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        bg_lbl=Label(self.root,image=self.photoimg_1,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=160,width=340,height=450)

        # Login image
        img_2=Image.open(r"College_photo\user1.png")
        img_2=img_2.resize((100,100),Image.Resampling.HAMMING)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        bg_lbl=Label(self.root,image=self.photoimg_2,bg="black",borderwidth=0)
        bg_lbl.place(x=635,y=165,width=100,height=100)

        get_str=Label(frame,text=" USER LOGIN",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=80,y=100)

        # label
        u_name=lbl=Label(frame,text="User Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        u_name.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        u_pass=lbl=Label(frame,text="User Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        u_pass.place(x=70,y=215)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=245,width=270)

        img_3=Image.open(r"College_photo\user1.png")
        img_3=img_3.resize((25,25),Image.Resampling.HAMMING)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        bg_lbl=Label(self.root,image=self.photoimg_3,bg="black",borderwidth=0)
        bg_lbl.place(x=550,y=312,width=25,height=25)

        img_4=Image.open(r"College_photo\password.png")
        img_4=img_4.resize((25,25),Image.Resampling.HAMMING)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root,image=self.photoimg_4,bg="black",borderwidth=0)
        bg_lbl.place(x=550,y=376,width=25,height=25)

        # Login Button
        btn_login=Button(frame,command=self.login_process,text="Login",font=("arial",10,"bold"),width=15,bg="blue",fg="white",activeforeground="white",activebackground="blue",cursor="hand2")
        btn_login.place(x=40,y=300,width=270,height=35)

        # New Register Button
        btn_reg=Button(frame,text="New Register User",command=self.register_window,font=("arial",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black",cursor="hand2")
        btn_reg.place(x=15,y=350,width=160)

        # Forgot Password Button
        btn_forgot=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("arial",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black",cursor="hand2")
        btn_forgot.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login_process(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="tinku" and self.txtpass.get()=="kum":
            messagebox.showinfo("Success","Welcom to Student Management System")       
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
            my_cursur=conn.cursor()
            my_cursur.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),self.txtpass.get()
            ))
            row=my_cursur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid User & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Student(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ================================Reset passrord====================================
    def reset_pass(self):
        if self.com_security.get()=="Select Option":
            messagebox.showerror("Error","select Security Question",parent=self.root2)
        elif self.security_ans.get()=="":
            messagebox.showerror("Error","Plese Enter the Answer",parent=self.root2)
        elif self.new_password.get()=="":
            messagebox.showerror("Error","Plese Enter The New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
            my_cursur=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.com_security.get(),self.security_ans.get())
            my_cursur.execute(query,value)
            row=my_cursur.fetchone()
            if row==None:
                messagebox.showerror("Error","Plese Enter Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_password.get(),self.txtuser.get())
                my_cursur.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("info","Password Successfully changed Login Again",parent=self.root2)
                self.root2.destroy()

    # ==============================forgot_password_window==============================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Plese Enter The Email To Forgot Password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
            my_cursur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursur.execute(query,value)
            row=my_cursur.fetchone()

            if row==None:
                messagebox.showerror("Error","Plese Enter The Vaild User Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+502+170")

                img=Image.open(r"College_photo\blck.jpg")
                img=img.resize((1530,790),Image.Resampling.HAMMING)
                self.photoimg=ImageTk.PhotoImage(img)

                bg_lbl=Label(self.root2,image=self.photoimg,bd=2,relief=RIDGE)
                bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

                leb=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),bd=2,fg="green",bg="black")
                leb.place(x=50,y=10,width=250)

                security=lbl=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),fg="white",bg="black")
                security.place(x=50,y=80)

                self.com_security=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.com_security["value"]=("Select Option","Your School First Name","Your Birth Place","Your Pet Name")
                self.com_security.current(0)
                self.com_security.place(x=50,y=110,width=250)

                security_ans=lbl=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="white",bg="black")
                security_ans.place(x=50,y=150)

                self.security_ans=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.security_ans.place(x=50,y=180,width=250)

                new_password=lbl=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="white",bg="black")
                new_password.place(x=50,y=220)

                self.new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.new_password.place(x=50,y=250,width=250)

                btn_reset=Button(self.root2,text="Reset",command=self.reset_pass,font=("arial",10,"bold"),width=15,bg="blue",fg="white",activeforeground="white",activebackground="blue",cursor="hand2")
                btn_reset.place(x=50,y=290,width=250,height=35)

class Register():
    def __init__(self,root1):
        self.root1=root1
        self.root1.title("Student Management System New Register Form")
        self.root1.geometry("1530x790+-7+0")

        # =========Variables===================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()

        # Background image
        img_1=Image.open(r"College_photo\university1.jpg")
        img_1=img_1.resize((1530,790),Image.Resampling.HAMMING)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        bg_lbl=Label(self.root1,image=self.photoimg_1,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # left image
        img_2=Image.open(r"College_photo\university.jpg")
        img_2=img_2.resize((1530,790),Image.Resampling.HAMMING)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        bg_lbl=Label(self.root1,image=self.photoimg_2,bd=1,relief=RIDGE)
        bg_lbl.place(x=50,y=100,width=470,height=500)

        reg_frame=Frame(self.root1,bg="white")
        reg_frame.place(x=520,y=100,width=720,height=500)

        get_str=Label(reg_frame,text="REGISTERATION FORM",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        get_str.place(x=200,y=20)

        # Frist name
        f_name=lbl=Label(reg_frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        f_name.place(x=50,y=100)

        self.f_name=ttk.Entry(reg_frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.f_name.place(x=50,y=130,width=250)

        # Last name
        l_name=lbl=Label(reg_frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        l_name.place(x=370,y=100)

        self.l_name=ttk.Entry(reg_frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.l_name.place(x=370,y=130,width=250)

        # contact
        contact=lbl=Label(reg_frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)

        self.contact=ttk.Entry(reg_frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact.place(x=50,y=200,width=250)

        # Email
        email=lbl=Label(reg_frame,text="Email ",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)

        self.email=ttk.Entry(reg_frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email.place(x=370,y=200,width=250)

        # security
        security=lbl=Label(reg_frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        security.place(x=50,y=240)

        self.com_security=ttk.Combobox(reg_frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.com_security["value"]=("Select Option","Your School First Name","Your Birth Place","Your Pet Name")
        self.com_security.current(0)
        self.com_security.place(x=50,y=270,width=250)

        security_ans=lbl=Label(reg_frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_ans.place(x=370,y=240)

        self.security_ans=ttk.Entry(reg_frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.security_ans.place(x=370,y=270,width=250)

        # password
        paswd=lbl=Label(reg_frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        paswd.place(x=50,y=310)

        self.paswd=ttk.Entry(reg_frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.paswd.place(x=50,y=340,width=250)

        cnf_paswd=lbl=Label(reg_frame,text=" Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        cnf_paswd.place(x=370,y=310)

        self.cnf_paswd=ttk.Entry(reg_frame,textvariable=self.var_conpass,font=("times new roman",15,"bold"))
        self.cnf_paswd.place(x=370,y=340,width=250)

        # checkbutton
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(reg_frame,variable=self.var_check,text="I Agree The Term & Condition",font=("times new roman",13,"bold"),bg="white",onvalue=1,offvalue=0,activebackground="white")
        self.checkbtn.place(x=45,y=380)

        # New Register Button
        btn_reg=Button(reg_frame,text="Register Now",command=self.register_data,font=("arial",13,"bold"),borderwidth=0,bg="blue",fg="white",activeforeground="white",activebackground="blue",cursor="hand2")
        btn_reg.place(x=50,y=420,width=180)

        # Login Now Button
        btn_log=Button(reg_frame,text="Login Now",command=self.return_login,font=("arial",13,"bold"),borderwidth=0,bg="blue",fg="white",activeforeground="white",activebackground="blue",cursor="hand2")
        btn_log.place(x=370,y=420,width=180)
    
    # function declare
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select Option":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root1)
        elif self.var_pass.get()!=self.var_conpass.get():
            messagebox.showerror("Error","Password Does Not Matched",parent=self.root1)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Plese agree term and condition",parent=self.root1)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
            my_cursur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursur.execute(query,value)
            row=my_cursur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist, Try Anothor Email",parent=self.root1)
            else:
                my_cursur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),
                    self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","User Successfully Register",parent=self.root1)

    def return_login(self):
        self.root1.destroy()

class Student():
    def __init__(self,root3):
        self.root3=root3
        self.root3.title("Student Management System")
        self.root3.geometry("1530x790+-7+0")

        # Variable
        self.var_dep=StringVar()
        self.var_Course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_Attendance=StringVar()

        # 1img
        img=Image.open(r"College_photo\7th.jpg")
        img=img.resize((540,160),Image.Resampling.HAMMING) #for converting the low size image
        self.photoimg=ImageTk.PhotoImage(img)

        self.lbl_1=Label(self.root3,image=self.photoimg)
        self.lbl_1.place(x=0,y=0,width=540,height=150)

        # 2img
        img_2=Image.open(r"College_photo\6th.jpg")
        img_2=img_2.resize((540,160),Image.Resampling.HAMMING)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.lbl_2=Label(self.root3,image=self.photoimg_2)
        self.lbl_2.place(x=450,y=0,width=540,height=150)

        # 3img
        img_3=Image.open(r"College_photo\5th.jpg")
        img_3=img_3.resize((540,160),Image.Resampling.HAMMING)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.lbl_1=Label(self.root3,image=self.photoimg_3)
        self.lbl_1.place(x=900,y=0,width=540,height=150)

        # Background image
        img_4=Image.open(r"College_photo\university.jpg")
        img_4=img_4.resize((1530,710),Image.Resampling.HAMMING)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root3,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=150,width=1530,height=700)

        lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="green",bg="white")
        lbl_title.place(x=0,y=0,width=1460,height=50)

        # Manage_frame
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=5,y=52,width=1355,height=495)

        # left Frame
        Dataleftframe=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",
        font=("times new roman",12,"bold"),fg="red",bg="white")
        Dataleftframe.place(x=0,y=0,width=605,height=490)

        # 3img
        img_5=Image.open(r"College_photo\3rd.jpg")
        img_5=img_5.resize((600,120),Image.Resampling.HAMMING)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img=Label(Dataleftframe,image=self.photoimg_5,relief=RIDGE)
        my_img.place(x=0,y=0,width=595,height=120)

        # Current corse LableFrame Information
        std_lbl=LabelFrame(Dataleftframe,bd=4,relief=RIDGE,padx=2,text="Current Course Information",
        font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl.place(x=0,y=120,width=595,height=115)

        # Labels
        # Department
        lbl_dep=Label(std_lbl,text="Department",font=("arial",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky='w')

        combo_dep=ttk.Combobox(std_lbl,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer Science","BS","LAW")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky='w')

        # Course
        lbl_dep=Label(std_lbl,text="Course",font=("arial",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=2,padx=2,sticky='w')

        com_txtCourse=ttk.Combobox(std_lbl,textvariable=self.var_Course,font=("arial",12,"bold"),width=17,state="readonly")
        com_txtCourse["value"]=("Select Course","MCA","BCA","B.SC","LLM","B.Tech")
        com_txtCourse.current(0)
        com_txtCourse.grid(row=0,column=3,padx=2,pady=10,sticky='w')

        # Year
        Year_std=Label(std_lbl,text="Year",font=("arial",12,"bold"),bg="white")
        Year_std.grid(row=1,column=0,padx=2,sticky='w')

        com_txtYear=ttk.Combobox(std_lbl,textvariable=self.var_year,font=("arial",12,"bold"),width=17,state="readonly")
        com_txtYear["value"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        com_txtYear.current(0)
        com_txtYear.grid(row=1,column=1,padx=2,pady=10,sticky='w')

        # Semester
        Semester_std=Label(std_lbl,text="Semester",font=("arial",12,"bold"),bg="white")
        Semester_std.grid(row=1,column=2,padx=2,sticky='w')

        com_txtSemester=ttk.Combobox(std_lbl,textvariable=self.var_semester,font=("arial",12,"bold"),width=17,state="readonly")
        com_txtSemester["value"]=("Select Semester","1","2","3","4")
        com_txtSemester.current(0)
        com_txtSemester.grid(row=1,column=3,padx=2,pady=10,sticky='w')

        # Student class LableFrame Information
        std_lbl_class=LabelFrame(Dataleftframe,bd=4,relief=RIDGE,padx=2,text="Class Course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_class.place(x=0,y=235,width=595,height=200)

        # Labels entry
        # ID
        lbl_id=Label(std_lbl_class,text="Student ID",font=("arial",11,"bold"),bg="white")
        lbl_id.grid(row=0,column=0,padx=2,pady=5,sticky='w')

        id_entry=ttk.Entry(std_lbl_class,textvariable=self.var_std_id,font=("arial",11,"bold"))
        id_entry.grid(row=0,column=1,padx=2,pady=5,sticky='w')

        # Name
        lbl_name=Label(std_lbl_class,text="Name",font=("arial",11,"bold"),bg="white")
        lbl_name.grid(row=0,column=2,padx=2,pady=5,sticky='w')

        name_entry=ttk.Entry(std_lbl_class,textvariable=self.var_std_name,font=("arial",11,"bold"))
        name_entry.grid(row=0,column=3,padx=2,pady=5,sticky='w')

        # Division
        div_std=Label(std_lbl_class,text="Division",font=("arial",11,"bold"),bg="white")
        div_std.grid(row=1,column=0,padx=2,sticky='w')

        com_txtdiv=ttk.Combobox(std_lbl_class,textvariable=self.var_div,font=("arial",11,"bold"),width=17,state="readonly")
        com_txtdiv["value"]=("Select Division","First","2nd","3rd","Fail")
        com_txtdiv.current(0)
        com_txtdiv.grid(row=1,column=1,padx=2,pady=7,sticky='w')

        # Roll
        lbl_roll=Label(std_lbl_class,text="Roll No",font=("arial",11,"bold"),bg="white")
        lbl_roll.grid(row=1,column=2,padx=2,pady=5,sticky='w')

        roll_entry=ttk.Entry(std_lbl_class,textvariable=self.var_roll,font=("arial",11,"bold"))
        roll_entry.grid(row=1,column=3,padx=2,pady=5,sticky='w')

        # Gender
        gender_std=Label(std_lbl_class,text="Gender",font=("arial",11,"bold"),bg="white")
        gender_std.grid(row=2,column=0,padx=2,sticky='w')

        com_txtgender=ttk.Combobox(std_lbl_class,textvariable=self.var_gender,font=("arial",11,"bold"),width=17,state="readonly")
        com_txtgender["value"]=("Select Gender","Male","Female","Other")
        com_txtgender.current(0)
        com_txtgender.grid(row=2,column=1,padx=2,pady=7,sticky='w')

        # DOB
        lbl_dob=Label(std_lbl_class,text="DOB",font=("arial",11,"bold"),bg="white")
        lbl_dob.grid(row=2,column=2,padx=2,pady=5,sticky='w')

        dob_entry=ttk.Entry(std_lbl_class,textvariable=self.var_dob,font=("arial",11,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,pady=5,sticky='w')

        # Email
        lbl_email=Label(std_lbl_class,text="Email",font=("arial",11,"bold"),bg="white")
        lbl_email.grid(row=3,column=0,padx=2,pady=5,sticky='w')

        email_entry=ttk.Entry(std_lbl_class,textvariable=self.var_email,font=("arial",11,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=5,sticky='w')

        # Phone
        lbl_phone=Label(std_lbl_class,text="Mob. No",font=("arial",11,"bold"),bg="white")
        lbl_phone.grid(row=3,column=2,padx=2,pady=5,sticky='w')

        phone_entry=ttk.Entry(std_lbl_class,textvariable=self.var_mob,font=("arial",11,"bold"))
        phone_entry.grid(row=3,column=3,padx=2,pady=5,sticky='w')

        # Address
        lbl_add=Label(std_lbl_class,text="Address",font=("arial",11,"bold"),bg="white")
        lbl_add.grid(row=4,column=0,padx=2,pady=5,sticky='w')

        add_entry=ttk.Entry(std_lbl_class,textvariable=self.var_address,font=("arial",11,"bold"))
        add_entry.grid(row=4,column=1,padx=2,pady=5,sticky='w')

        # Attendance
        tech_std=Label(std_lbl_class,text="Attendance",font=("arial",11,"bold"),bg="white")
        tech_std.grid(row=4,column=2,padx=2,pady=5,sticky='w')

        com_txt_tech=ttk.Combobox(std_lbl_class,textvariable=self.var_Attendance,font=("arial",11,"bold"),width=17,state="readonly")
        com_txt_tech["value"]=("Present","Absent")
        com_txt_tech.current(0)
        com_txt_tech.grid(row=4,column=3,padx=2,pady=7,sticky='w')
        # Botton_frame
        btn_frame=Frame(Dataleftframe,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=435,width=595,height=32)

        btn_Add=Button(btn_frame,text="Save",command=self.add_data,font=("arial",10,"bold"),width=17,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Updade",command=self.update_data,font=("arial",10,"bold"),width=17,bg="blue",fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_Delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",10,"bold"),width=17,bg="blue",fg="white")
        btn_Delete.grid(row=0,column=2,padx=1)

        btn_Reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",10,"bold"),width=17,bg="blue",fg="white")
        btn_Reset.grid(row=0,column=3,padx=1)

        # Right Frame
        Datarightframe=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",
        font=("times new roman",12,"bold"),fg="red",bg="white")
        Datarightframe.place(x=608,y=0,width=738,height=490)

        # Logout Button
        btn_logout=Button(root3,text="Logout",command=self.return_logout,font=("arial",10,"bold"),width=20,bg="white",bd=0,fg="red",activeforeground="red",activebackground="white",cursor="hand2")
        btn_logout.place(x=1200,y=160,width=120,height=35)

        # 6img
        img_6=Image.open(r"College_photo\9th.jpg")
        img_6=img_6.resize((780,200),Image.Resampling.HAMMING)
        self.photoimg_6=ImageTk.PhotoImage(img_6)
       
        img_6=Label(Datarightframe,image=self.photoimg_6,bd=2,relief=RIDGE)
        img_6.place(x=0,y=0,width=725,height=150)

        Searchframe=LabelFrame(Datarightframe,bd=4,relief=RIDGE,padx=2,text="Search Student Information",
        font=("times new roman",12,"bold"),fg="red",bg="white")
        Searchframe.place(x=0,y=140,width=725,height=60)

        search_by=Label(Searchframe,text="Search By:",font=("arial",11,"bold"),fg="red",bg="white")
        search_by.grid(row=0,column=0,padx=2,pady=5,sticky='w')
        
        # Search
        self.var_com_search=StringVar()
        com_txtSearch=ttk.Combobox(Searchframe,textvariable=self.var_com_search,font=("arial",11,"bold"),width=17,state="readonly")
        com_txtSearch["value"]=("Select Option","Roll","Name","Mob_No","student_id")
        com_txtSearch.current(0)
        com_txtSearch.grid(row=0,column=1,padx=5,sticky='w')

        self.var_search=StringVar()
        txt_search=ttk.Entry(Searchframe,textvariable=self.var_search,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=2,sticky='w')

        btn_search=Button(Searchframe,command=self.search_data,text="Search",font=("arial",10,"bold"),width=15,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_All=Button(Searchframe,command=self.fetch_data,text="Show All",font=("arial",10,"bold"),width=15,bg="blue",fg="white")
        btn_All.grid(row=0,column=4,padx=5)

        #========================= Student Table Scrol Bar======================
        table_frame=Frame(Datarightframe,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=200,width=725,height=265)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview (table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","mob. no","address","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Genger")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("mob. no",text="Mob_No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("Attendance",text="Attendance")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("mob. no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("Attendance",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # Datbeses
    def add_data(self):
        if(self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","All Fields Are Required",parent=self.root3)
        elif ():
            messagebox.showerror
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into sms values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),self.var_Course.get(),self.var_year.get(),self.var_semester.get(),
                    self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),
                    self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_mob.get(),
                    self.var_address.get(),self.var_Attendance.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully Added",parent=self.root3)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root3)

    # fatch function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from sms")
        data=my_cursur.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # Get cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]
        self.var_dep.set(data[0]), self.var_Course.set(data[1]), self.var_year.set(data[2]),
        self.var_semester.set(data[3]), self.var_std_id.set(data[4]), self.var_std_name.set(data[5]),
        self.var_div.set(data[6]), self.var_roll.set(data[7]), self.var_gender.set(data[8]),
        self.var_dob.set(data[9]), self.var_email.set(data[10]), self.var_mob.set(data[11]),
        self.var_address.set(data[12]), self.var_Attendance.set(data[13])

    # Update Section
    def update_data(self):
        if(self.var_dep.get()=="" or self.var_email.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","All Fields Are Required",parent=self.root3)
        else:
            try:
                update=messagebox.askyesno("update","Are you sure update data",parent=self.root3)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
                    my_cursur=conn.cursor()
                    my_cursur.execute("update sms set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Mob_No=%s,Address=%s,Attendance=%s where student_id=%s",(
                    self.var_dep.get(),self.var_Course.get(),self.var_year.get(),self.var_semester.get(),
                    self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),
                    self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_mob.get(),
                    self.var_address.get(),self.var_Attendance.get(),self.var_std_id.get()))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("Success","Update Successfully",parent=self.root3)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root3)

    # Delete Section
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root3)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are You Sure Delete This Data",parent=self.root3)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
                    my_cursur=conn.cursor()
                    sql="delete from sms where student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursur.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Delete Successfully",parent=self.root3)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root3)

    # Reset Section
    def reset_data(self):
        self.var_dep.set("Select Department"), self.var_Course.set("Select Course"), self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"), self.var_std_id.set(""), self.var_std_name.set(""),
        self.var_div.set("Select Division"), self.var_roll.set(""), self.var_gender.set("Select Gender"),
        self.var_dob.set(""), self.var_email.set(""), self.var_mob.set(""),
        self.var_address.set(""), self.var_Attendance.set("Select Attendance")
    
    # Search section
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Plese Select Option",parent=self.root3)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
                my_cursur=conn.cursor()
                my_cursur.execute("select * from sms where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursur.fetchall()

                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)

                    conn.commit()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root3)

    def return_logout(self):
        self.root3.destroy()

if __name__ == "__main__":
   main()  