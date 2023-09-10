from atexit import register
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector


class Register():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System New Register Form")
        self.root.geometry("1530x790+0+0")

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

        bg_lbl=Label(self.root,image=self.photoimg_1,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # left image
        img_2=Image.open(r"College_photo\university.jpg")
        img_2=img_2.resize((1530,790),Image.Resampling.HAMMING)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        bg_lbl=Label(self.root,image=self.photoimg_2,bd=1,relief=RIDGE)
        bg_lbl.place(x=50,y=100,width=470,height=500)

        reg_frame=Frame(self.root,bg="white")
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
        self.checkbtn=Checkbutton(reg_frame,variable=self.var_check,text="I Agree The Rerm & Condition",font=("times new roman",13,"bold"),bg="white",onvalue=1,offvalue=0,activebackground="white")
        self.checkbtn.place(x=45,y=380)

        # New Register Button
        btn_reg=Button(reg_frame,text="Register Now",command=self.register_data,font=("arial",13,"bold"),borderwidth=0,bg="blue",fg="white",activeforeground="white",activebackground="blue",cursor="hand2")
        btn_reg.place(x=50,y=420,width=180)

        # Forgot Password Button
        btn_forgot=Button(reg_frame,text="Login Now",font=("arial",13,"bold"),borderwidth=0,bg="blue",fg="white",activeforeground="white",activebackground="blue",cursor="hand2")
        btn_forgot.place(x=370,y=420,width=180)
    
    # function declare
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select Option":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get()!=self.var_conpass.get():
            messagebox.showerror("Error","Password Does Not Matched")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Plese agree term and condition")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Tinku@123",database="cuk")
            my_cursur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursur.execute(query,value)
            row=my_cursur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist, Try Anothor Email")
            else:
                my_cursur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),
                    self.var_securityQ.get(),self.var_securityA.get(),self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","User Successfully Register")





        








if __name__ == "__main__":
    root = Tk()
    obj=Register(root)
    root.mainloop()