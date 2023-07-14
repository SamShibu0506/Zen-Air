from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from tkmacosx import Button
import mysql.connector
from tkcalendar import DateEntry
from tkmacosx import Button as macosx_Button
import random
import string
from ttkthemes import ThemedStyle
import datetime

class Login:
    def on_enter(self,e):
        self.username_entry.delete(0,'end')
    def on_leave(self,e):
        name = self.username_entry.get()
        if(name==''):
            self.username_entry.insert(0,'Username')
    def on_enterp(self,e):
        self.psswd_entry.delete(0,'end')
        self.psswd_entry.configure(show="•")
    def on_leavep(self,e):
        name = self.psswd_entry.get()
        if(name==''):
            self.psswd_entry.configure(show="")
            self.psswd_entry.insert(0,'Password')


    def on_enterfgt(self,e):
        self.answer_entry.delete(0,'end')
    def on_leavefgt(self,e):
        name = self.answer_entry.get()
        if(name==''):
            self.answer_entry.insert(0,'Answer')
    def on_enternw(self,e):
        self.newpass_entry.delete(0,'end')
        self.newpass_entry.configure(show="•")
    def on_leavenw(self,e):
        name = self.newpass_entry.get()
        if(name==''):
            self.newpass_entry.configure(show="")
            self.newpass_entry.insert(0,'New Password')
            
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#fff")
        self.root.geometry("462x500+550+200")
        self.root.resizable(False,False)
        self.root.title("ZEN Airlines")

        login_frame = Frame(root,bg="#11172b")
        self.root.configure(background="white")
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        login_frame.place(x=0, y=0, height=self.screen_height, width=self.screen_width / 3+10)
        bg_lbl = Label(login_frame, bg="#11172b")
        bg_lbl.place(x=0, y=0, height=self.screen_height, width=self.screen_width / 3+10)



        self.username = StringVar()
        self.password = StringVar()
        self.answer = StringVar()
        self.newpass = StringVar()
        
        # username = Label(login_frame,text = "USERNAME",font=("charter",15,"bold"),fg="white",bg="#11172b")
        # username.grid(column=0,row=0)
        self.username_entry = ttk.Entry(login_frame,font=("Charter",15,"bold"),textvariable=self.username)
        self.username_entry.place(x=80,y=150,width=300,height=50)
        self.username_entry.insert(0,'Username')
        self.username_entry.bind('<FocusIn>',self.on_enter)
        self.username_entry.bind('<FocusOut>',self.on_leave)
        # self.psswd = Label(login_frame,text = "PASSWORD",font=("charter",15,"bold"),fg="white",bg="#11172b")
        # self.psswd.grid(column=0,row=1)
        self.psswd_entry = ttk.Entry(login_frame,font=("Charter",15,"bold"),textvariable=self.password,)
        self.psswd_entry.place(x=80,y=210,width=300,height=50)

        self.psswd_entry.insert(0,'Password')
        self.psswd_entry.bind('<FocusIn>',self.on_enterp)
        self.psswd_entry.bind('<FocusOut>',self.on_leavep)
        b1 = Button(login_frame, text="Log In", font=("charter", 15,"bold"), fg="white", bg="red",borderless=1,command=self.log,borderwidth=0)
        b1.place(x=80,y=300,width=300,height=50)
        b2 = Button(login_frame, text="Forgot Password", font=("charter", 12,"bold"), fg="white", bg="#11172b",borderless=1,command=self.open_child_window)
        b2.place(x=270,y=265,width=110,height=30)
        # self.btn_book_add.grid(row=0,column=1,padx=1,pady=13)

    def open_child_window(self):
        if self.username.get()=="":
            messagebox.showerror("Error","Please enter username")
        conn = mysql.connector.connect(host='localhost',user="root",password="sam19113",database="Project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from login where username=%s",(self.username.get(),))
        row = my_cursor.fetchone()
        if row== None:
             messagebox.showerror("Error","Please enter valid username")
        else:
            self.root2 = Toplevel()
            self.root2.title("Forgot Password")
            self.root2.geometry("400x430+580+250")
            self.root2.resizable(False,False)

            self.screen_width = root.winfo_screenwidth()
            self.screen_height = root.winfo_screenheight()
            fgtframe = Frame(self.root2)
            fgtframe.place(x=0,y=0,width=self.screen_height,height=self.screen_height)
            bgfgt = Label(fgtframe,bg="#11172b")
            bgfgt.place(x=0,y=0,width=self.screen_height,height=self.screen_height)
            l = Label(self.root2,text="Choose The Security Question",font=("charter", 13,"bold"), fg="white", bg="#11172b")
            l.place(x=110,y=80)
            self.combo_sec = ttk.Combobox(self.root2,state="readonly",font=("Charter",13,"bold")) 
            self.combo_sec["values"] = ("Select","Pet Name","Birth Place","First Teacher's Name")
            self.combo_sec.current(0)
            self.combo_sec.place(x=110,y=110,width=200,height=40)

            self.answer_entry = ttk.Entry(fgtframe,font=("Charter",12,"bold"),textvariable=self.answer)
            self.answer_entry.place(x=110,y=170,width=200,height=40)
            if not self.answer_entry.get() == 'Answer':
                self.answer_entry.delete(0,'end')
                self.answer_entry.insert(0,'Answer')
            
            self.answer_entry.bind('<FocusIn>',self.on_enterfgt)
            self.answer_entry.bind('<FocusOut>',self.on_leavefgt)

            self.newpass_entry = ttk.Entry(fgtframe,font=("Charter",12,"bold"),textvariable=self.newpass)
            self.newpass_entry.place(x=110,y=220,width=200,height=40)
            if not self.newpass_entry.get() == "New Password":
                self.newpass_entry.delete(0,'end')
                self.newpass_entry.insert(0, 'New Password')
            self.newpass_entry.bind('<FocusIn>',self.on_enternw)
            self.newpass_entry.bind('<FocusOut>',self.on_leavenw)

            b3 = Button(fgtframe, text="Reset", font=("charter", 13,"bold"), fg="white", bg="red",borderless=1,command=self.reset)
            b3.place(x=110,y=270,width=200,height=40)
    def reset(self):
        conn = mysql.connector.connect(host='localhost',user="root",password="sam19113",database="Project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from login where username=%s and security_answer=%s",(self.username.get(),self.answer.get()))
        row = my_cursor.fetchone()
        if row== None:
            messagebox.showerror("Error","Answer is Invalid")
        else:
            my_cursor.execute("update login set password =%s where username=%s",(self.newpass.get(),self.username.get()))
            messagebox.showinfo("Success","Password Reset Successfully")
            conn.commit()
            conn.close()  
            self.root2.destroy()

    def log(self):
            if self.username.get()=="" or self.password.get()=="" or self.password.get()=="Password" or self.username.get()=="Username":
                messagebox.showerror("Error","All Fields are Required")
            else:
                conn = mysql.connector.connect(host='localhost',user="root",password="sam19113",database="Project")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from login where username=%s and password=%s",(self.username.get(),self.password.get()))
                row = my_cursor.fetchone()
                if row== None:
                    messagebox.showerror("Error","Invalid User Id or Password")
                else:
                    messagebox.showinfo("Success","Logged in Successfully")
                    self.newhomewindow = Toplevel(self.root)
                    self.home = HomePage(self.newhomewindow)
                conn.commit()
                conn.close()  



class HomePage:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("ZEN Airlines")
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        Menu_frame = Frame(root)
        Menu_frame.place(x=0,y=0,height=80,width=self.screen_width)
        bg_lbl = Label(Menu_frame, bg="#11172b")
        bg_lbl.place(x=0,y=0,width=self.screen_width,height=80)
        #-----------------MENU BUTTON--------------------------------------------------------#
        indicatewidth = 7
        
        lbl_logo=Label(Menu_frame,text="ZEN AIR",font=("charter",30,"bold"),fg="white",bg="#11172b")
        lbl_logo.grid(row=0,column=0,padx=(100,10),pady=(20,5))

        option_frame = Frame(Menu_frame, bg="#11172b",)
        option_frame.place(x=250,y=20)

        btn_book_add = macosx_Button(option_frame, text="BOOK", font=("charter", 13,"bold"), fg="white", bg="#11172b",borderless=1,command=lambda:self.indicate(self.home_indicate,self.bookpage))
        btn_book_add.grid(row=0,column=1,padx=1,pady=13)
        self.home_indicate = Label(option_frame,text='',bg="#11172b",width=8)
        self.home_indicate.grid(row=1,column=1)
        
        btn_chk_add = macosx_Button(option_frame,text="CHECK-IN",font=("charter",13,"bold"),fg="white",bg="#11172b",borderless=1,command=lambda:self.indicate(self.chk_indicate,self.chkinpage))
        btn_chk_add.grid(row=0,column=2,padx=1)
        self.chk_indicate = Label(option_frame,text='',bg="#11172b",width=10)
        self.chk_indicate.grid(row=1,column=2)

        btn_mytrip_add = macosx_Button(option_frame,text="MY TRIPS",font=("charter",13,"bold"),fg="white",bg="#11172b",borderless=1,command=lambda:self.indicate(self.mytrip_indicate,self.trippage))
        btn_mytrip_add.grid(row=0,column=3,padx=1)
        self.mytrip_indicate = Label(option_frame,text='',bg="#11172b",width=10)
        self.mytrip_indicate.grid(row=1,column=3)

        btn_status_add = macosx_Button(option_frame,text="FLIGHT STATUS",font=("charter",13,"bold"),fg="white",bg="#11172b",borderless=1,command=lambda:self.indicate(self.status_indicate,self.statuspage))
        btn_status_add.grid(row=0,column=4,padx=1)
        self.status_indicate = Label(option_frame,text='',bg="#11172b",width=14)
        self.status_indicate.grid(row=1,column=4)

        btn_login_add = macosx_Button(option_frame,text="LOG OUT",font=("charter",13,"bold"),fg="white",bg="#11172b",borderless=1,command=lambda:self.indicate(self.login_indicate,self.loginpage))
        btn_login_add.grid(row=0,column=5,padx=(620,0),pady=(0,5))
        self.login_indicate = Label(option_frame,text='',bg="#11172b",width=9)
        self.login_indicate.grid(row=1,column=5,padx=(620,0),pady=(0,5))

        self.Main_frame = Frame(root)
        self.Main_frame.place(x=0,y=80,height=self.screen_height,width=self.screen_width)
        bg_lb2 = Label(self.Main_frame, bg="#11172b")
        bg_lb2.place(x=0,y=0.5,width=self.screen_width,height=self.screen_height)
        self.indicate(self.home_indicate,self.bookpage)
    #-----------------------INDICATOR FUNCTION------------------------------
    def hide(self):
        self.home_indicate.config(bg="#11172b")
        self.mytrip_indicate.config(bg="#11172b")
        self.status_indicate.config(bg="#11172b")
        self.chk_indicate.config(bg="#11172b")
        self.login_indicate.config(bg="#11172b")
    def indicate(self,lb,page):
        self.hide()
        lb.config(bg="red")
        self.deletepage()
        page()
    def deletepage(self):
        for frame in self.Main_frame.winfo_children():
            frame.destroy()

    #--------------------MAIN FRAME-------------------------------------
    def bookpage(self):
        self.homeframe = Frame(self.Main_frame,bg="#11172b")
        self.homeframe.place(x=0,y=0,height=self.screen_height,width=self.screen_width,)
        
        bg_lb2 = Label(self.homeframe, bg="#11172b")
        bg_lb2.place(x=0,y=0.5,width=self.screen_width,height=self.screen_height)
        lbl1 = Label(self.homeframe,text="BOOK",font=("charter",13,"bold"),fg="red",bg="orange")
        lbl1.place(x=5,y=10)
        box = Label(self.homeframe,bd=20,bg="#11172b",relief=RIDGE)
        box.place(x=0,y=3,width=self.screen_width,height=230)
        self.bookimg = Image.open("bookpge1.jpeg")
        self.resizebookimg = self.bookimg.resize((1450, 550))  # Resize the image to the desired dimensions
        self.bookimg = ImageTk.PhotoImage(self.resizebookimg)
        self.booklbl4 = Label(self.homeframe,image=self.bookimg,bg="#11172b")
        self.booklbl4.place(x=0,y=235,height=550,width=1450)
        self.tboxbg = Label(self.homeframe,bg="#11172b")
        self.tboxbg.place(x=80,y=430,height=170,width=380)
        self.booklbl5 = Label(self.homeframe,text="FLY AND EXPLORE",font=("Andale Mono",15,"bold"),fg="white",bg="#11172b")
        self.booklbl5.place(x=200,y=450,)
        self.booklbl6 = Label(self.homeframe,text="Earn thousands of Miles this summer",font=("Apple Chancery",20,"bold"),fg="white",bg="#11172b")
        self.booklbl6.place(x=110,y=480,)
        self.booklbl7 = Label(self.homeframe,text="We've made your travels more rewarding with thousands of\nMiles to earn with our partners.",font=("Times",15,),fg="white",bg="#11172b")
        self.booklbl7.place(x=80,y=530,)

        self.searchflight()
        
    def statuspage(self):
        self.statusframe = Frame(self.Main_frame)
        self.statusframe.place(x=0,y=0,height=self.screen_height,width=self.screen_width)
        self.statuslbl1 = Label(self.statusframe, bg="#11172b")
        self.statuslbl1.place(x=0,y=0.5,width=self.screen_width,height=self.screen_height)

        self.statuslbl3 = Label(self.statusframe,bd=20,bg="#11172b",relief=RIDGE)
        self.statuslbl3.place(x=0,y=3,width=self.screen_width,height=230)
        self.statuslbl2 = Label(self.statusframe,text="FLIGHT STATUS",font=("charter",20,"bold"),fg="#11172b",bg="red")
        self.statuslbl2.place(x=self.screen_width/2-100,y=75,width=200,height=100)
    def trippage(self):
        self.tripframe = Frame(self.Main_frame)
        self.tripframe.place(x=0,y=0,height=self.screen_height,width=self.screen_width)
        self.triplbl1 = Label(self.tripframe, bg="#11172b")
        self.triplbl1.place(x=0,y=0.5,width=self.screen_width,height=self.screen_height)
        self.triplbl3 = Label(self.tripframe,bd=20,bg="#11172b",relief=RIDGE)
        self.triplbl3.place(x=0,y=3,width=self.screen_width,height=230)
        self.triplbl2 = Label(self.tripframe,text="MY TRIPS",font=("charter",20,"bold"),fg="#11172b",bg="red")
        self.triplbl2.place(x=self.screen_width/2-100,y=75,width=200,height=100)
    def chkinpage(self):
        self.chkinframe = Frame(self.Main_frame)
        self.chkinframe.place(x=0,y=0,height=self.screen_height,width=self.screen_width)
        self.chkinlbl1 = Label(self.chkinframe, bg="#11172b")
        self.chkinlbl1.place(x=0,y=0.5,width=self.screen_width,height=self.screen_height)
        self.chkinlbl3 = Label(self.chkinframe,bd=20,bg="#11172b",relief=RIDGE)
        self.chkinlbl3.place(x=0,y=3,width=self.screen_width,height=230)
        self.chkinlbl2 = Label(self.chkinframe,text="CHECK-IN",font=("charter",20,"bold"),fg="#11172b",bg="red")
        self.chkinlbl2.place(x=self.screen_width/2-100,y=75,width=200,height=100)
    def loginpage(self):
        messagebox.askokcancel("Are you sure you want to log out","log out")
        messagebox.showinfo("Success","Logged Out Successfully")
        self.root.destroy()
    def on_enterfrom(self,e):
        self.Fromen.delete(0,'end')
    def on_leavefrom(self,e):
        name = self.Fromen.get()
        if(name==''):
            self.Fromen.insert(0,'From')
    def on_enterTo(self,e):
        self.To.delete(0,'end')
    def on_leaveTo(self,e):
        name = self.To.get()
        if(name==''):
            self.To.insert(0,'To')
    def swap(self):
        self.temp = self.Fromget.get()
        self.temp2 = self.Toget.get()
        if(self.temp == 'From' and self.temp2=='To'):
            return
        elif(self.temp != 'From' and self.temp2=='To'):
            self.To.delete(0,'end')
            self.From.delete(0,'end')
            self.From.insert(0,'From')
            self.To.insert(0,self.temp)
            return
        elif(self.temp == 'From' and self.temp2!='To'):
            self.To.delete(0,'end')
            self.From.delete(0,'end')
            self.To.insert(0,'To')
            self.From.insert(0,self.temp2)
            return
        self.To.delete(0,'end')
        self.From.delete(0,'end')
        self.From.insert(0,self.temp2)
        self.To.insert(0,self.temp)
    def option_selected(self):
        selected_option = self.triptype.get()
        if selected_option == "One Way":
            self.entry1.config(state="normal")
            self.entry2.config(state="disabled")
        elif selected_option == "Round Trip":
            self.entry1.config(state="normal")
            self.entry2.config(state="normal")
    def searchflight(self):
        self.Fromget = StringVar()
        self.Toget = StringVar()
        self.finddatefrom = StringVar()
        self.finddateto = StringVar()
        self.findtype = StringVar()
        self.Fromen = ttk.Entry(self.homeframe, font=("Charter", 15, "bold"), textvariable=self.Fromget)
        self.Fromen.place(x=100, y=100, width=200, height=50)
        self.Fromen.insert(0, 'From')
        self.Fromen.bind('<FocusIn>', self.on_enterfrom)
        self.Fromen.bind('<FocusOut>', self.on_leavefrom)

        self.swapimg = Image.open("swap.png")
        self.resizedswapimg = self.swapimg.resize((30, 40))  # Resize the image to the desired dimensions
        self.swapphoto = ImageTk.PhotoImage(self.resizedswapimg)
        self.swapbutton = Button(self.homeframe, image=self.swapphoto, bg="#11172b", borderless=1, command=self.swap)
        self.swapbutton.place(x=330, y=105, width=40, height=40)

        self.To = ttk.Entry(self.homeframe, font=("Charter", 15, "bold"), textvariable=self.Toget)
        self.To.place(x=400, y=100, width=200, height=50)
        self.To.insert(0, 'To')
        self.To.bind('<FocusIn>', self.on_enterTo)
        self.To.bind('<FocusOut>', self.on_leaveTo)

        self.triptype = ttk.Combobox(self.homeframe, values=["One Way", "Round Trip"],)
        self.triptype.current(0)  # Set "One Way" as the default value
        self.triptype.place(x=650, y=110, width=100, height=30)
        self.triptype.bind("<<ComboboxSelected>>", lambda event: self.option_selected())

        self.entry1 = DateEntry(self.homeframe, font=("Charter", 12, ), date_pattern="yyyy-mm-dd",)
        self.entry1.place(x=780, y=110, width=100, height=30)

        self.entry2 = DateEntry(self.homeframe, font=("Charter", 12, ), date_pattern="yyyy-mm-dd", state="disabled",)
        self.entry2.place(x=880, y=110, width=100, height=30)
        self.pax2 = ttk.Combobox(self.homeframe, font=("Charter", 15, ),values=["Travellers","1", "2","3","4"],)
        self.pax2.place(x=1000,y=110,width=100,height=30)
        self.pax2.current(0)
        self.bookbtn = Button(self.homeframe, text="BOOK", font=("charter", 12,"bold"), fg="white", bg="red",borderless=1,command=self.bookbtnfn)
        self.bookbtn.place(x=1150,y=100,width=100,height=50)
    def bookbtnfn(self):
        # self.s = ttk.Style()
        # self.s.configure('Treeview', rowheight=40)
        self.tree = ttk.Treeview(self.homeframe, columns=("","Flight No.", "Departure", "Departure Time", "Destination","Arrival Time","Cost", "Date", "Duration"))
        # self.tree.heading("#0", text="")
        self.tree.heading("#1", text="Flight No.")
        self.tree.heading("#2", text="Departure")
        self.tree.heading("#3", text="Departure Time")
        self.tree.heading("#4", text="Destination")
        self.tree.heading("#5", text="Arrival Time")
        self.tree.heading("#6", text="Cost")
        self.tree.heading("#7", text="Date")
        self.tree.heading("#8", text="Duration")

        self.tree.column("#1", width=100)
        self.tree.column("#2", width=100)
        self.tree.column("#3", width=100)
        self.tree.column("#4", width=100)
        self.tree.column("#5", width=100)
        self.tree.column("#6", width=100)
        self.tree.column("#7", width=100)
        self.tree.column("#8", width=100)
        # Populate TreeView with data
        self.populate_treeview(self.tree)
        self.tree.place(x=0,y=230,height=470,width=self.screen_width)
        if(self.triptype.get() == "One Way"):
            self.selectbtn = Button(self.homeframe, text="Book", font=("charter", 15,"bold"), fg="white", bg="red",borderless=1,command=self.selectflight,activebackground='red',activeforeground='black')
            self.selectbtn.place(x=0,y=700,width=self.screen_width,height=70)
        else:
            self.selectbtn = Button(self.homeframe, text="Select", font=("charter", 15,"bold"), fg="white", bg="red",borderless=1,command=self.selectflight,activebackground='red',activeforeground='black')
            self.selectbtn.place(x=0,y=700,width=self.screen_width,height=70)
 
    def selectflight(self):
        self.curItem = self.tree.focus()
        self.date1 = None
        self.date2 = None
        self.flight1 = None
        self.flight2 = None
        self.trip = None
        self.dep = self.tree.item(self.curItem,"values")
        self.pas = self.pax2.get()
        # print(self.dep)
        if self.triptype.get() == "One Way":
            # print("one way")
            self.date1 = self.entry1.get_date()
            self.flight1 = self.dep[0]
            self.trip = "One Way"
            # self.getdetails()
            self.bookwin = Toplevel(self.root)
            self.book = BookTicket(self.bookwin,self.date1,self.date2,self.flight1,self.flight2,self.trip,self.pas)
        else:
            self.selectbtn.destroy()
            self.mycursor.execute("select fd.flight_no,fd.departure,TIME_FORMAT(fd.departure_time, '%h:%i %p'),fd.destination,TIME_FORMAT(fd.arrival_time, '%h:%i %p'),f.cost,f.date,TIMEDIFF(fd.arrival_time, fd.departure_time) AS duration from flightdata as fd inner join flight as f on fd.flight_no = f.flight_no where f.date = %s and fd.departure = %s and fd.destination = %s",(self.entry2.get_date(),self.Toget.get(), self.Fromget.get()))
            # self.mycursor.execute("select * from flights where departure = %s and destination = %s and date = %s;", (self.Toget.get(), self.Fromget.get(),self.entry2.get_date()))
            flights = self.mycursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for flight in flights:
                self.tree.insert("", "end", values=flight)
            self.selectbtn = Button(self.homeframe, text="Book", font=("charter", 15,"bold"), fg="white", bg="red",borderless=1,command=self.twoway,activebackground='red',activeforeground='black')
            self.selectbtn.place(x=0,y=700,width=self.screen_width,height=70)
            
    def twoway(self):
            self.curItem = self.tree.focus()
            self.ret = self.tree.item(self.curItem,"values")
            # print(self.ret)
            self.date1 = self.entry1.get_date()
            self.date2 = self.entry2.get_date()
            self.flight1 = self.dep[0]
            self.flight2 = self.ret[0]
            self.trip = "Two Way"
            self.bookwin = Toplevel(self.root)
            self.book = BookTicket(self.bookwin,self.date1,self.date2,self.flight1,self.flight2,self.trip,self.pas)




    def generatepnr():
        pnr = "ZE" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return pnr 
    def populate_treeview(self,tree):
    # Connect to the MySQL database
        self.conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sam19113",
        database="project"
    )
        self.mycursor = self.conn.cursor()
        self.mycursor.execute("select fd.flight_no,fd.departure,TIME_FORMAT(fd.departure_time, '%h:%i %p'),fd.destination,TIME_FORMAT(fd.arrival_time, '%h:%i %p'),f.cost,f.date,TIMEDIFF(fd.arrival_time, fd.departure_time) AS duration from flightdata as fd inner join flight as f on fd.flight_no = f.flight_no where f.date = %s and fd.departure = %s and fd.destination = %s",(self.entry1.get_date(),self.Fromget.get(), self.Toget.get(),))        
        flights = self.mycursor.fetchall()

        # Populate the TreeView with data
        for flight in flights:
            tree.insert("", "end", values=flight)

    # Close the database connection
        # self.conn.close()

class BookTicket:
    def __init__(self,root,date1,date2,flight1,flight2,trip,pax) :
        self.root = root
        self.root.geometry("1100x780+150+70")
        self.root.title("ZEN Airlines")

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.date1 = date1
        self.date2 = date2
        self.flight1 = flight1
        self.flight2 = flight2
        self.trip = trip
        self.trunctemp() #TRuncating table temp
        self.bgcol = "#F8F8F8"
        self.conn = mysql.connector.connect(host='localhost',user="root",password="sam19113",database="Project")
        self.mycursor = self.conn.cursor()
        self.mycursor.execute("select fd.flight_no,fd.departure,TIME_FORMAT(fd.departure_time, '%l:%i%p'),fd.destination,TIME_FORMAT(fd.arrival_time, '%l:%i%p'),f.cost,DATE_FORMAT(f.date, '%Y-%m-%d'),TIMEDIFF(fd.arrival_time, fd.departure_time) AS duration from flightdata as fd inner join flight as f on fd.flight_no = f.flight_no where f.date = %s and f.flight_no = %s ",(self.date1,self.flight1))    

        a = self.mycursor.fetchone()
        # print(a)
        date = a[6]  # Fetch the date from the result
        deptime = a[2].lower()
        arrtime = a[4].lower()
        cost1 = int(a[5])
        print(cost1)

        formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%b %d")
        formatted_day = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%a")

        source = a[1]
        destination = a[3]
        self.mycursor.execute("select code from airports where name = %s",(source,))
        b = self.mycursor.fetchone()
        self.sourcecode = b[0]
        self.mycursor.execute("select code from airports where name = %s",(destination,))
        c = self.mycursor.fetchone()
        self.destinationcode = c[0]
        # print(self.destinationcode)
        # print(self.sourcecode)
        duration = a[7]  # Fetch the duration from the result
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        formatted_duration = f"{hours}h {minutes}m"
        # print(formatted_duration)
        self.Menu_frame = Frame(self.root)
        self.Menu_frame.place(x=0,y=0,height=80,width=self.screen_width)
        self.bg_lbl = Label(self.Menu_frame, bg="#11172b")
        self.bg_lbl.place(x=0,y=0,width=self.screen_width,height=80)
        #-----------------MENU BUTTON--------------------------------------------------------#
        indicatewidth = 7
        self.mainframe = Frame(self.root,bg=self.bgcol)
        self.mainframe.place(height=self.screen_height,width=self.screen_width,x=0,y=80)
        self.lbl_logo=Label(self.Menu_frame,text="ZEN AIR",font=("charter",30,"bold"),fg="white",bg="#11172b")
        self.lbl_logo.grid(row=0,column=0,padx=(100,10),pady=(20,5))


        self.b = 1
        self.pax = pax

        self.bar1bg = 'white'
        self.lbl2 = Label(self.mainframe,text="Trip Summary",bg=self.bgcol,fg="#0b1f66",font=("Whitney-Book",30,))
        self.lbl2.place(x=100,y=10)
        self.detailsframe = Frame(self.mainframe,bg="#f8f8f8")
        self.detailsframe.place(x=100,y=200,height=400,width=610)
        self.inndet = Frame(self.detailsframe,bg='white')
        self.inndet.place(x=0,y=50,height=380,width=580)
        self.bar1 = Frame(self.mainframe,bg=self.bar1bg)
        self.bar1.place(x=100,y=80,width=610,height=80)
        self.pointer1 = Label(self.bar1,bg="#0b1f66")
        self.pointer1.place(x=0,y=0,width=10,height=80)
        self.b11 = Label(self.bar1,text="Outbound",fg="#0b1f66",bg=self.bar1bg,font=("Whitney-Book",15,'bold'))
        self.b11.place(x=10,y=5)
        self.b12 = Label(self.bar1,text=(self.sourcecode + " - " + self.destinationcode),fg="#0b1f66",bg=self.bar1bg,font=("Charter",16,'bold'))
        self.b12.place(x=100,y=25)
        self.b13 = Label(self.bar1,text=(formatted_day + ", " + formatted_date),fg="#0b1f66",bg=self.bar1bg,font=("Charter",16,'bold'))
        self.b13.place(x=220,y=25)
        self.b14 = Label(self.bar1,text=(deptime + " - " + arrtime),fg="#0b1f66",bg=self.bar1bg,font=("Charter",16,'bold'))
        self.b14.place(x=340,y=25)
        self.b15 = Label(self.bar1,text=(formatted_duration),fg="#0b1f66",bg=self.bar1bg,font=("Charter",16,'bold'))
        self.b15.place(x=510,y=25)
        self.lbl1 = Label(self.detailsframe,text="Passenger Info",font=("charter", 22,"bold"),bg=self.bgcol,fg="#0b1f66")
        self.lbl1.place(x=0,y=15)
        
        canvas = Label(self.mainframe,bg='red')
        self.triptol = Frame(self.mainframe,width=300,height=300,bg='white',)
        self.triptol.place(x=780,y=50)
        self.lblt1 = Label(self.triptol,text='Trip Total',font=("Charter", 25,'bold'),fg="#0b1f66",bg='white')
        self.lblt1.place(x=10,y=10,)
        self.lblt2 = Label(self.triptol,text=(str(pax)+" Passenger"),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
        self.lblt2.place(x=10,y=50,)
        canvas.place(x=750,y=50,width=5, height=600)
        if(self.trip=='One Way'):
            print(self.pax)
        
            ttlcst = str(float(cost1)*float(self.pax))

            conv = str(0.01*float(ttlcst))
            ttltax = str(0.05*float(ttlcst))
            ttlamt = str(float(ttltax) + float(ttlcst) + float(conv))
            
            
            self.lblt2 = Label(self.triptol,text=("Flights"),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt2.place(x=10,y=80,)
            
            self.lblt3 = Label(self.triptol,text=("₹ " +ttlcst),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt3.place(x=200,y=80,)
            
            
            self.lblt4 = Label(self.triptol,text=("Taxes, Fees & Charges"),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt4.place(x=10,y=110,)
            self.lblt5 = Label(self.triptol,text=("₹ " +ttltax),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt5.place(x=200,y=110,)

            self.lblt6 = Label(self.triptol,text=("Convenience Fee"),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt6.place(x=10,y=140,)
            self.lblt7 = Label(self.triptol,text=("₹ " +conv),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt7.place(x=200,y=140,)
            self.line = Label(self.triptol,bg='red')
            self.line.place(x=20,y=179,width=245,height=3)
            self.lblt8 = Label(self.triptol,text=("Amount Due"),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt8.place(x=10,y=190,)
            self.lblt9 = Label(self.triptol,text=("₹ " +ttlamt),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt9.place(x=200,y=190,)

        
        # print(ttlamt)
        # print(0.05*cost1*self.pax)
        if(self.trip == "Two Way"):
            self.detailsframe.place_configure(y=260)
            self.mycursor.execute("select fd.flight_no,fd.departure,TIME_FORMAT(fd.departure_time, '%l:%i%p'),fd.destination,TIME_FORMAT(fd.arrival_time, '%l:%i%p'),f.cost,DATE_FORMAT(f.date, '%Y-%m-%d'),TIMEDIFF(fd.arrival_time, fd.departure_time) AS duration from flightdata as fd inner join flight as f on fd.flight_no = f.flight_no where f.date = %s and f.flight_no = %s ",(self.date2,self.flight2)) 
            d = self.mycursor.fetchone()
            date = d[6]  # Fetch the date from the result
            deptime = d[2].lower()
            arrtime = d[4].lower()
            cost2 = int(d[5])
            ttlcst = str((float(cost1)+float(cost2))*float(self.pax))
            print(cost1)
            print(cost2)
            conv = str(0.01*float(ttlcst))
            ttltax = str(0.05*float(ttlcst))
            ttlamt = str(float(ttltax) + float(ttlcst) + float(conv))
            # canvas.place(x=750,y=50)
            
            
            self.lblt2 = Label(self.triptol,text=("Flights"),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt2.place(x=10,y=80,)
            
            self.lblt3 = Label(self.triptol,text=("₹ " +ttlcst),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt3.place(x=200,y=80,)
            
            
            self.lblt4 = Label(self.triptol,text=("Taxes, Fees & Charges"),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt4.place(x=10,y=110,)
            self.lblt5 = Label(self.triptol,text=("₹ " +ttltax),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt5.place(x=200,y=110,)

            self.lblt6 = Label(self.triptol,text=("Convenience Fee"),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt6.place(x=10,y=140,)
            self.lblt7 = Label(self.triptol,text=("₹ " +conv),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt7.place(x=200,y=140,)
            self.line = Label(self.triptol,bg='red')
            self.line.place(x=20,y=179,width=245,height=3)
            self.lblt8 = Label(self.triptol,text=("Amount Due"),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt8.place(x=10,y=190,)
            self.lblt9 = Label(self.triptol,text=("₹ " +ttlamt),font=("Times",14,'bold'),fg="#0b1f66",bg='white')
            self.lblt9.place(x=200,y=190,)


            formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%b %d")
            formatted_day = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%a")
            duration = d[7]  # Fetch the duration from the result
            hours, remainder = divmod(duration.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            formatted_duration = f"{hours}h {minutes}m"
            self.bar2 = Frame(self.mainframe,bg=self.bar1bg)
            self.bar2.place(x=100,y=170,width=610,height=80)
            self.pointer2 = Label(self.bar2,bg="#0b1f66")
            self.pointer2.place(x=0,y=0,width=10,height=80)
            self.b21 = Label(self.bar2,text="Return",fg="#0b1f66",bg=self.bar1bg,font=("Whitney-Book",15,'bold'))
            self.b21.place(x=10,y=5)
            self.b22 = Label(self.bar2,text=(self.destinationcode + " - " + self.sourcecode),fg="#0b1f66",bg=self.bar1bg,font=("Charter",16,'bold'))
            self.b22.place(x=100,y=25)
            self.b23 = Label(self.bar2,text=(formatted_day + ", " + formatted_date),fg="#0b1f66",bg=self.bar1bg,font=("Charter",16,'bold'))
            self.b23.place(x=220,y=25)
            self.b24 = Label(self.bar2,text=(deptime + " - " + arrtime),fg="#0b1f66",bg=self.bar1bg,font=("Charter",16,'bold'))
            self.b24.place(x=340,y=25)
            self.b25 = Label(self.bar2,text=(formatted_duration),fg="#0b1f66",bg=self.bar1bg,font=("Charter",16,'bold'))
            self.b25.place(x=510,y=25)

        self.entdetails()


    def entdetails(self):
        style = ttk.Style()
        style.configure("TEntry", padding=(0, 5, 0, 5))

        self.a = "Passenger-" + str(self.b) 
        # print(self.pax2.get())
        self.pass1 = Label(self.inndet,text=self.a,font=("Charter",16,'bold'),bg='white',fg="#0b1f66")
        self.pass1.place(x=10,y=5)
        self.entnamelbl1 = Label(self.inndet,text="First Name",font=("Charter",13,'bold'),bg='white',fg="#697180",)
        self.entnamelbl1.grid(column=0,row=0,sticky="w",pady=(40,0),padx=(10,0))
        self.entname1 = ttk.Entry(self.inndet, font=("Charter", 13,),width=29)
        self.entname1.grid(column=0,row=1,padx=(10,50),pady=(0,10))
        self.entnamelbl2 = Label(self.inndet,text="Last Name",font=("Charter",13,'bold'),bg='white',fg="#697180")
        self.entnamelbl2.grid(column=1,row=0,sticky="w",pady=(40,0))


        self.entname2 = ttk.Entry(self.inndet, font=("Charter", 13,),width=29)
        self.entname2.grid(column=1,row=1,padx=0,pady=(0,10))

        self.entage1 = Label(self.inndet,text="Age",font=("Charter",13,'bold'),bg='white',fg="#697180")
        self.entage1.grid(column=0,row=2,sticky='w',padx=(10,0),)

        self.entage2 = ttk.Entry(self.inndet, font=("Charter", 13,),width=29)
        self.entage2.grid(column=0,row=3,padx=(10,50),pady=(0,10))

        self.gender1 = Label(self.inndet,text="Gender",font=("Charter", 13, "bold"),bg='white',fg="#697180")
        self.gender1.grid(column=1,row=2,sticky='w')
        style.configure("TCombobox", selectbackground="white",)

        self.gender2 = ttk.Combobox(self.inndet, font=("Charter", 16, "bold"),values=["Select","Male", "Female","Other"],width=22,state='readonly')
        self.gender2.grid(column=1,row=3,padx=0)
        self.gender2.current(0)

        self.nat1 = Label(self.inndet,text="Nationality",font=("Charter",13,'bold'),bg='white',fg="#697180")
        self.nat1.grid(column=0,row=4,sticky='w',padx=(10,0),)

        self.nat2 = ttk.Entry(self.inndet, font=("Charter", 13,),width=29)
        self.nat2.grid(column=0,row=5,padx=(10,50))

        if int(self.pax) == self.b:
            self.done = Button(self.inndet, text="Submit", font=("charter", 15,"bold"), fg="white", bg="red",borderless=1,command=lambda:(self.addpax(),self.addedpax()),activebackground='red',activeforeground='black')
            self.done.place(x=120,y=265,width=310,height=40)
        else:
            self.addpsnd = Button(self.inndet, text="Add Passenger", font=("charter", 15,"bold"), fg="white", bg="red",borderless=1,command=lambda:(self.addpax(),self.entdetails()),activebackground='red',activeforeground='black')
            self.addpsnd.place(x=120,y=265,width=310,height=40)
        self.b = self.b + 1
    def addedpax(self):
        messagebox.showinfo("Success","Successfully Added Travellers")
    def addpax(self):
        self.conn = mysql.connector.connect(host='localhost',user="root",password="sam19113",database="Project")
        self.mycursor = self.conn.cursor()
        first_name = self.entname1.get()
        last_name = self.entname2.get()
        age = int(self.entage2.get())
        gender = self.gender2.get()
        self.mycursor.execute("insert into temp values (%s,%s,%s,%s)", (first_name,last_name,age,gender))
        self.conn.commit()
        for widget in self.inndet.winfo_children():
            widget.destroy()
        self.trunctemp()
        
    def trunctemp(self):
        self.conn = mysql.connector.connect(host='localhost',user="root",password="sam19113",database="Project")
        self.mycursor = self.conn.cursor()
        self.mycursor.execute("truncate table temp",)
        self.conn.commit()
        self.conn.close()





if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
