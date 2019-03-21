from Tkinter import*
from tkMessageBox import *
import sqlite3
import time;

def Student_info():
    root=Tk()
    root.geometry("1600x800+0+0")
    root.title("Student Record Keeping Systems")
    #root.configure(background='light blue')

    first=Frame(root,width=1600,height=50,bg="dark grey",relief="raised")
    first.pack(side=TOP)
    first.configure(background='light blue')

    f1=Frame(root,width=1200,height=800,relief="raised")
    f1.pack(side=LEFT)

    f2=Frame(root,width=400,height=40,relief="raised")
    f2.pack(side=RIGHT)

    localtime=time.asctime(time.localtime(time.time()))

    Label(first,font="times 50 bold",text="Student record keeping system",fg="black",bd=10,anchor='w').grid(row=0,column=0)
    Label(first,font="times 20 bold",text=localtime,fg="blue",bd=10,anchor='w').grid(row=1,column=0)

    #------------------------------------------------------------------------------------------------------------------------
    Label(f1,text=" Enrollment No. :",fg='dark blue',font='Arial 16 bold',bd=16,anchor='w').grid(row=0,column=0)
    e1=Entry(f1,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey',insertwidth=4)
    e1.grid(row=0,column=1)

    Label(f1,text=" First Name :",fg='dark blue',font='Arial 16 bold',bd=16,anchor='w').grid(row=1,column=0)
    e2=Entry(f1,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey',insertwidth=4)
    e2.grid(row=1,column=1)

    Label(f1,text="Last Name :",fg='dark blue',font='Arial 16 bold',bd=16,anchor='w').grid(row=2,column=0)
    e3=Entry(f1,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey')
    e3.grid(row=2,column=1)

    Label(f1,text="Mobile No. :  ",fg='dark blue',font='Arial 16 bold',bd=16,anchor='w').grid(row=0,column=2)
    e8=Entry(f1,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey')
    e8.grid(row=0,column=3)

    Label(f1,text="CGPA: ",fg='dark blue',font='Arial 16 bold',bd=16,anchor='w').grid(row=1,column=2)
    e10=Entry(f1,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey')
    e10.grid(row=1,column=3)

    Label(f1,text=" Hobbies: ",fg='dark blue',font='Arial 16 bold',bd=16,anchor='w').grid(row=2,column=2)
    e11=Entry(f1,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey')
    e11.grid(row=2,column=3)

    #-------------------------------------------------------------------------------------------------------------------------

    Label(f1,text="Current Course:",fg='dark blue',font='Arial 16 bold',bd=16,anchor='w').grid(row=3,column=0)
    date31=("CSE","ECE","ME","CE","CHE")
    v1=StringVar()
    v1.set(date31[0])
    sb=Spinbox(f1,values=date31,textvariable=v1,width=10).grid(row=3,column=1)
    sa=v1.get()

    Label(f1,text="Department:",fg='dark blue',font='Arial 16 bold',bd=16,anchor='w').grid(row=3,column=2)
    date3=("B.Tech","M.Tech")
    v=StringVar()
    v.set(date3[0])
    sb=Spinbox(f1,values=date3,textvariable=v,width=10).grid(row=3,column=3)
    ss=v.get()

    #------------------------------------- Date of Birth-------------------------------------------------------------------------------------
    Label(f1,text=" Date of Birth of Student :",fg='dark blue',font='Arial 16 bold',anchor='w').grid(row=4,column=0)

    spinbox1=Spinbox(f1,from_=1,to=31,state=NORMAL,width=8)
    spinbox1.grid(row=4,column=1)

    dateList=["Jan","Feb","Mar","Apr","May","jun","July","Aug","Sep","Oct","Nov","Dec"]
    s=StringVar()
    s.set(dateList[0])
    dMenu=OptionMenu(f1,s,*dateList)
    dMenu.grid(row=4,column=2)

    spinbox2=Spinbox(f1,from_=1990,to=2017,state=NORMAL,width=8)
    spinbox2.grid(row=4,column=3)


    t1=spinbox1.get()
    t3=spinbox2.get()
    t2=s.get()
       
    e4=t1+"/"+t2+"/"+t3
    #---------------------------------------Registration date------------------------------------------------------------------------------------------
    Label(f1,text="Registration Date :",fg='dark blue',font='Arial 16 bold',anchor='w').grid(row=5,column=0)

    spinbox3=Spinbox(f1,from_=1,to=31,state=NORMAL,width=8)
    spinbox3.grid(row=5,column=1)

    dateList=["Jan","Feb","Mar","Apr","May","jun","July","Aug","Sep","Oct","Nov","Dec"]
    ss1=StringVar()
    ss1.set(dateList[0])
    dMenu=OptionMenu(f1,ss1,*dateList)
    dMenu.grid(row=5,column=2)

    spinbox4=Spinbox(f1,from_=1990,to=2017,state=NORMAL,width=8)
    spinbox4.grid(row=5,column=3)


    w1=spinbox3.get()
    w3=spinbox4.get()
    w2=ss1.get()
       
    e6=w1+"/"+w2+"/"+w3



    #-----------------------++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-----------------------------------+

    Label(f2,text="    Enrollment no. OF STUDENT     \n   to retrieve data :",fg='dark blue',font='Arial 16 bold').grid(row=0,column=0)
    e12=Entry(f2,font='Arial 12 bold', bd=4, relief='sunken', bg='light grey')
    e12.grid(row=1,column=0)
    e12.insert(END,0)

    #----------------------------------------------------------------------------------------------------------------------------------------
    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e8.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
    #------------------------------------+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---------------------------------------+    

    def insert():
        con=sqlite3.Connection('students1')
        cur=con.cursor() 
        try:
            cur.execute("create table if not exists student1(erno number(10) primary key,fname char(15),lname char(15),dob date,regdate date,mobileno number(15),cgpa number(8),course char(15),department char(15),hobbies char(15))")
            b=(int(e1.get()),e2.get(),e3.get(),e4,e6,e8.get(),e10.get(),sa,ss,e11.get())
            cur.execute("insert into student1 values(?,?,?,?,?,?,?,?,?,?)",b) 
        except:
            showerror("Duplicate Entry","incorrect data")
        con.commit()
        #cur.fetchall()
        clear()

    #----------------------------============================------------------------------------=========================================--------

    def checkcgpa():
        w=int(e10.get())
        if w>=0:
            insert()
        else:
            showerror("error","You have entered invalid cgpa")
            clear()
        

    def checkmobno():
        a=int(e8.get())
        m=a
        l,r=0,0
        while a!=0:
            r=a%10
            l=l+1
            a=a/10
        print l
        if(l!=10):
            showerror("oops","Incorrect mobileno.")
            clear()
        elif(l==10):
            a=m
            k=[]
            i,r=0,0
            while i<10:
                r=a%10
                k.append(r)
                a=a/10
                i=i+1
            if (k[9]<7 and k[8]<7):
                showerror("oops","Incorrect mobileno.")
                clear() 
            else:
               checkcgpa()

    #--------------------------------------------------------------------------------------------------------------------------------------------------
    def showall():
        root1=Tk()
        root1.geometry("1170x500+0+0")
        root1.configure(background='darkOlivegreen')
        con=sqlite3.Connection('students1')
        cur=con.cursor()
        cur.execute("Select erno from student1",)
        a=[]
        a=cur.fetchall()
        b=[]
        cur.execute("Select fname from student1",)
        b=cur.fetchall()
        c=[]
        cur.execute("Select lname from student1",)
        c=cur.fetchall()
        d=[]
        cur.execute("Select dob from student1",)
        d=cur.fetchall()
        e=[]
        cur.execute("Select regdate from student1",)
        e=cur.fetchall()
        f=[]
        cur.execute("Select mobileno from student1",)
        f=cur.fetchall()
        g=[]
        cur.execute("Select cgpa from student1",)
        g=cur.fetchall()
        w=[]
        cur.execute("Select course from student1",)
        w=cur.fetchall()
        r=[]
        cur.execute("Select department from student1",)
        r=cur.fetchall()
        qq=[]
        cur.execute("Select hobbies from student1",)
        qq=cur.fetchall()
        Label(root1,text="Enrollmentno.",fg='black',font='Arial 10 bold',relief="raised",bg='light blue',borderwidth=4,width=15,height=2).grid(row=0,column=0)
        Label(root1,text="Student Name",fg='black',font='Arial 10 bold',relief="raised",bg='light blue',borderwidth=4,width=15,height=2).grid(row=0,column=1)
        Label(root1,text="DateOfBirth",fg='black',font='Arial 10 bold',relief="raised",bg='light blue',borderwidth=4,width=15,height=2).grid(row=0,column=2)
        Label(root1,text="RegistrationDate",fg='black',font='Arial 10 bold',relief="raised",bg='light blue',borderwidth=4,width=15,height=2).grid(row=0,column=3)
        Label(root1,text="Mobileno.",fg='black',font='Arial 10 bold',relief="raised",bg='light blue',borderwidth=4,width=15,height=2).grid(row=0,column=4)
        Label(root1,text="CGPA",fg='black',font='Arial 10 bold',relief="raised",bg='light blue',borderwidth=4,width=15,height=2).grid(row=0,column=5)
        Label(root1,text="Course",fg='black',font='Arial 10 bold',relief="raised",bg='light blue',borderwidth=4,width=15,height=2).grid(row=0,column=6)
        Label(root1,text="Department",fg='black',font='Arial 10 bold',relief="raised",bg='light blue',borderwidth=4,width=15,height=2).grid(row=0,column=7)
        Label(root1,text="Hobbies",fg='black',font='Arial 10 bold',relief="raised",bg='light blue',borderwidth=4,width=15,height=2).grid(row=0,column=8) 
        i,l,k=0,1,0
        for value in a:
            Label(root1,text=a[i],fg='black',font='Arial 10 bold',relief="sunken", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k)
            i=i+1
            l=l+1
        i,l,k=0,1,0
        for value in b and c:
            Label(root1,text=b[i]+c[i],fg='black',font='Arial 10 bold',relief="sunken", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,1
        for value in d:
            Label(root1,text=d[i],fg='black',font='Arial 10 bold',relief="sunken", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,2
        for value in e:
            Label(root1,text=e[i],fg='black',font='Arial 10 bold',relief="sunken", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,3
        for value in f:
            Label(root1,text=f[i],fg='black',font='Arial 10 bold',relief="sunken", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,4
        for value in g:
            Label(root1,text=g[i],fg='black',font='Arial 10 bold',relief="sunken", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,5
        for value in w:
            Label(root1,text=w[i],fg='black',font='Arial 10 bold',relief="sunken", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,6
        for value in r:
            Label(root1,text=r[i],fg='black',font='Arial 10 bold',relief="sunken", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,7
        for value in qq:
            Label(root1,text=qq[i],fg='black',font='Arial 10 bold',relief="sunken", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        
        Button(root1,text="Click to go back",bg='green',fg='black',font='Arial 8 bold',width=15,height=2,command=root1.destroy).grid(row=l+1,column=3)
        root1.mainloop()
                
    #-------------------------++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=---------------------------------------------------++

    def show():
        con=sqlite3.Connection('students1')
        cur=con.cursor()
        cur.execute("select * from student1 where erno=?",(int(e12.get()),))
        if(int(e12.get())!=0):
            showinfo("retrieved data",cur.fetchall())
            showinfo("Successful","Retrieved Successfuly")
        else:
            showerror("error","incorrect data")
        e12.delete(0,END)
        e12.insert(END,0)

        
    def quitx():
        q=askyesno("Exit system","Do you want to really quit")
        if q>0:
            root.destroy()
            return
        
    Button(f1,text="Insert",fg='dark red',font='Arial 19 bold',justify="left",width=18,bd=10,bg='dark grey',command=checkmobno).grid(row=8,column=0,columnspan=3)
    Button(f1,text="Reset",fg='dark red',font='Arial 19 bold',justify="left",width=16,bd=10,bg='dark grey',command=clear).grid(row=8,column=2)
    Button(f1,text="Show All",fg='dark red',font='Arial 19 bold',justify="right",bd=10,bg='dark grey',width=15,command=showall).grid(row=8,column=3)
    Button(f2,text="Retrieve data ",fg='dark red',font='Arial 19 bold',bd=10,bg='dark grey',command=show).grid(row=3,column=0,columnspan=2)
    Button(f2,text="quit ",fg='dark red',font='Arial 19 bold',bd=10,bg='dark grey',command=quitx).grid(row=4,column=0)



    root.mainloop()



        
