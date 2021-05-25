#!/usr/bin/env python3
from tkinter import*
import pymysql
from PIL import ImageTk
from tkinter import messagebox
from tkinter import ttk
import tkinter
class Login():

    def __init__(self):
        self.root = root
        self.root.title("Get Started..")
        self.root.geometry("1200x600+40+20")
        self.root.resizable(False, False)
        #self.path = 'D:/pythonProject/Project_01/GUI_Image_Capture.py'

        #self.bg1 = PhotoImage(file="Logo_Image.png")
        #self.bg1_image = Label(self.root, image=self.bg1).place(x=0, y=0, width=1000, height=500)

        self.bg = ImageTk.PhotoImage(file="login_bg.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame_login1 = Frame(self.root, bg="white")
        frame_login1.place(x=100, y=20, height=560, width=400)

        #title1 = Label(frame_login1, text="SignUp", font=("Impact", 30, "bold"), fg="#d77337", bg="white")
        #title1.place(x=90, y=30)
        desc0 = Label(frame_login1, text="Don't worry if you don't have an account",font=("Calibri", 10, "bold"), fg="#d25d17",
                      bg="white")
        desc0.place(x=30, y=60)
        desc1 = Label(frame_login1, text="Create a new account", font=("Goudy old style", 15, "bold"), fg="#d25d17",
                      bg="white")
        desc1.place(x=30, y=80)
        desc2 = Label(frame_login1, text="It's quick and easy.", font=("Calibri", 10,), fg="#d25d17", bg="white")
        desc2.place(x=30, y=110)
        desc3 = Label(frame_login1, text="By clicking Sign Up, you agree to our Terms, Data Policy \n and Cookie Policy.", font=("Calibri", 10,), fg="#d25d17", bg="white")
        desc3.place(x=30, y=440)
        lbl_fname = Label(frame_login1, text="First Name*", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_fname.place(x=30, y=140)
        self.txt_fname = Entry(frame_login1, font=("calibri", 10), bg="lightgray")
        self.txt_fname.place(x=30, y=160, width=150, height=25)

        lbl_lname = Label(frame_login1, text="Last Name*", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_lname.place(x=200, y=140)
        self.txt_lname = Entry(frame_login1, font=("calibri", 10), bg="lightgray")
        self.txt_lname.place(x=200, y=160, width=150, height=25)

        lbl_contact = Label(frame_login1, text="Contact#*", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_contact.place(x=30, y=200)
        self.txt_contact = Entry(frame_login1, font=("calibri", 10), bg="lightgray")
        self.txt_contact.place(x=30, y=220, width=150, height=25)

        lbl_email = Label(frame_login1, text="Email Address*", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_email.place(x=200, y=200)
        self.txt_email = Entry(frame_login1, font=("calibri", 10), bg="lightgray")
        self.txt_email.place(x=200, y=220, width=150, height=25)

        lbl_secq = Label(frame_login1, text="Security Question*", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_secq.place(x=30, y=260)
        #self.txt_secq = Entry(frame_login1, font=("calibri", 10), bg="lightgray")
        #self.txt_secq.place(x=30, y=280, width=320, height=25)
        self.cmb_txt_secq = ttk.Combobox(frame_login1, font=("calibri", 10, "bold"), state="readonly")
        self.cmb_txt_secq['values'] = ("Select", "Your First Pet", "Your Birth Place", "Your Best Friend's Name")
        self.cmb_txt_secq.place(x=30, y=280, width=320, height=25)
        self.cmb_txt_secq.current(0)
        #self.Cmb_Value = cmb_txt_secq.get()

        lbl_seca = Label(frame_login1, text="Answer*", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_seca.place(x=30, y=320)
        self.txt_seca = Entry(frame_login1, font=("calibri", 10), bg="lightgray")
        self.txt_seca.place(x=30, y=340, width=320, height=25)

        lbl_password = Label(frame_login1, text="Password*", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_password.place(x=30, y=380)
        self.txt_password = Entry(frame_login1, font=("calibri", 10), bg="lightgray")
        self.txt_password.place(x=30, y=400, width=150, height=25)

        lbl_cpassword = Label(frame_login1, text="Confirm Password*", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_cpassword.place(x=200, y=380)
        self.txt_cpassword = Entry(frame_login1, font=("calibri", 10), bg="lightgray")
        self.txt_cpassword.place(x=200, y=400, width=150, height=25)

        signup_btn = Button(self.root, command=self.signup_function, cursor="hand2", text="Sign Up", fg="White",
                            bg="#d77337", bd=0, font=("calibri", 15))
        signup_btn.place(x=90, y=520, width=180, height=40)

        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=700, y=150, height=280, width=420)

        #title = Label(frame_login, text="Login", font=("Impact", 30, "bold"), fg="#d77337", bg="white")
        #title.place(x=90, y=30)
        desc00 = Label(frame_login, text="Existing Account", font=("Goudy old style", 15, "bold"), fg="#d25d17",
                      bg="white")
        desc00.place(x=30, y=40)
        desc11 = Label(frame_login, text="If you already have an account with us, please proceed logging in", font=("Calibri", 10, "bold"), fg="#d25d17", bg="white")
        desc11.place(x=30, y=80)

        lbl_user = Label(frame_login, text="Username", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_user.place(x=30, y=120)
        self.txt_user = Entry(frame_login, font=("calibri", 10),  bg="lightgray")
        self.txt_user.place(x=30, y=140, width=150, height=25)

        lbl_pass = Label(frame_login, text="Password", font=("calibri", 10, "bold"), fg="gray", bg="white")
        lbl_pass.place(x=200, y=120)
        self.txt_pass = Entry(frame_login, font=("calibri", 10), bg="lightgray")
        self.txt_pass.place(x=200, y=140, width=150, height=25)

       # forgot_btn = Button(frame_login, text="Forgot Password?", cursor="hand2", bg="White", fg="#d77337", bd=0, font=("calibri", 10))
       # forgot_btn.place(x=30, y=180)

        login_btn = Button(self.root, command=self.login_function, cursor="hand2", text="Login", fg="White", bg="#d77337", bd=0, font=("calibri", 15))
        login_btn.place(x=690, y=370, width=180, height=40)

    def signup_function(self):
        print(self.txt_fname.get(),
              self.txt_lname.get(),
              self.txt_contact.get(),
              self.txt_email.get(),
              self.cmb_txt_secq.get(),
              self.txt_seca.get(),
              self.txt_password.get(),
              self.txt_cpassword.get()
              )

        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_txt_secq.get() == "" or self.txt_seca.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error", "Please fill in the mandate fields(marked as *)", parent=self.root)
        elif self.cmb_txt_secq.get() == "Select":
            messagebox.showerror("Error", "Choose one of the options for Security Question from the dropdown", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password String Mismatch Found!", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="administrator", database="db_project_01")
                cur = con.cursor()
                cur.execute("select * from db_project_01.user where Email_Address = %s", self.txt_email.get())
                row_signup = cur.fetchone()
                #print(row_signup)
                if row_signup != None:
                    messagebox.showerror("Error", "Registration Failed as the email address is already occupied. \n Please use a different email id.", parent=self.root)
                    con.commit()
                    con.close()
                else:
                    cur.execute("insert into db_project_01.user(First_Name,Last_Name,Contact,Email_Address,Security_Question,Security_Answer,Password) values (%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.txt_fname.get(), self.txt_lname.get(), self.txt_contact.get(), self.txt_email.get(), self.cmb_txt_secq.get(), self.txt_seca.get(), self.txt_password.get()
                            ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Registration Status",
                                    f"Welcome aboard! \n Hey {self.txt_fname.get()} {self.txt_lname.get()}, you are successfully registered.",
                                    parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_txt_secq.delete(0, END)
        self.txt_seca.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_txt_secq.current(0)

    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error", "Please fill in the mandate fields", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="administrator", database="db_project_01")
                cur = con.cursor()
                print(self.txt_user.get())
                print(self.txt_pass.get())
                try:
                    cur.execute(f"select * from db_project_01.user where Email_Address = %s and Password = %s", (self.txt_user.get(), self.txt_pass.get()))
                except Exception as e:
                    print(e)
                #and Password = `{self.txt_pass.get()}`")
                row_login = cur.fetchone()
                #print(row_login)
                if row_login==None:
                    messagebox.showerror("Error", "You are not a valid user. Please signup and register yourself.", parent=self.root)
                    con.commit()
                    con.close()
                else:
                    con.commit()
                    con.close()
                    messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}",
                    #\n Your Password: {self.txt_pass.get()}",
                                parent=self.root)
                    print("Check-1")
                    #PLACE THE CODE FOR UI IMAGE SCANNER
                    import GUI_Image_Capture
                    #GUI_Image_Capture.tehseencode()
                    #----------------------------------#
                    print("Check-2")

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root);
root=Tk()
obj=Login()
root.mainloop()
