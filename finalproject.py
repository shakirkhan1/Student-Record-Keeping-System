from Tkinter import *
from tkMessageBox import *
import sqlite3
import time;



root11=Tk()#main root window for details
root11.geometry("1380x800+0+0")
root11.configure(background='DarkGoldenrod4')
root11.resizable(0,0)


def quitx2(Motion):
    root11.destroy()
#__________________________+++++++++++++++++++++++++++_____________________________________+++++++++++++++++++++++++++++++_______________________________
    root=Tk()
    root.geometry("1600x800+0+0")
    root.title("Student Record keeping System")
    root.configure(background='goldenrod')
    #root.resizable(0,0)

    first=Frame(root,width=1600,height=35,bg="dark grey",relief="sunken",bd=10)            #bottom frame 1
    first.pack(side=TOP)
    first.configure(background='DodgerBlue')

    fir2=Frame(first,width=1600,height=30,bg="dark grey",relief="sunken",bd=10)       #fram 1 on top of bottom fram
    fir2.pack(side=TOP)
    fir2.configure(background='darkkhaki')

    
    a=PhotoImage(file='images/logojuet3.gif')
    l=Label(fir2,image=a)
    l.grid(row=0)

    ##first1=Frame(root,width=50,height=50,bg="dark grey",relief="raised")
    ##first1.pack(side=BOTTOM)
    ##first1.configure(background='DarkSlateblue')


    f1=Frame(root,width=1200,height=750,relief="raised",bg='honeydew3',bd=10)    #left bottom frame fields 
    f1.pack(side=LEFT)
    f1.configure(background='DodgerBlue')

    f1a=Frame(f1,width=1200,height=750,relief="raised",bg='honeydew3',bd=10)#subframe on left frame 
    f1a.pack(side=LEFT)


    f2=Frame(root,width=500,height=750,relief="raised",bg='honeydew3',bd=10)#right frame for field to retrieve data
    f2.pack(side=RIGHT)
    f2.configure(background='DodgerBlue')

    f22=Frame(f2,width=500,height=750,relief="raised",bg='honeydew3',bd=10)#subfame on right frame
    f22.pack(side=RIGHT)

    localtime=time.asctime(time.localtime(time.time()))   #code to get system time
    
   #-----------------------------------+++++++++++++++++++labels on top frame +++++++++++++++++_____-----------------------------------------------------

    Label(fir2,font="times 50 bold underline",text="Student record keeping system",fg="black",bg='red',bd=10,anchor=W).grid(row=0,column=1)
    Label(fir2,font="times 15 bold",text="\n  JUET\n WELCOMES \n YOU  \n",fg="deepskyblue",bg='red',bd=10,anchor=W).grid(row=0,column=2)
    #Label(fir2,font="times 15 bold",text="\n BY \nSHAKIR KHAN\n  161B207   \n",fg="deepskyblue",bg='red',bd=10,anchor=W).grid(row=0)
    Label(fir2,font="times 20 bold underline",text=localtime,fg="DodgerBlue",bd=10,anchor='w').grid(row=1,column=1)

    #---------------------------------------------------labels on left top frame--------------------------------------------------------------
    Label(f1a,text=" Enrollment No. :",fg='dark blue',font='Arial 16 bold',bg='honeydew3',bd=16,anchor=W).grid(row=0,column=0)
    e1=Entry(f1a,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey',insertwidth=4)
    e1.grid(row=0,column=1)

    Label(f1a,text=" First Name :",fg='dark blue',font='Arial 16 bold',bg='honeydew3',bd=16,anchor=W).grid(row=1,column=0)
    e2=Entry(f1a,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey',insertwidth=4)
    e2.grid(row=1,column=1)

    Label(f1a,text="Last Name :",fg='dark blue',font='Arial 16 bold',bg='honeydew3',bd=16,anchor=W).grid(row=2,column=0)
    e3=Entry(f1a,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey')
    e3.grid(row=2,column=1)

    Label(f1a,text="Mobile No. :  ",fg='dark blue',font='Arial 16 bold',bg='honeydew3',bd=16,anchor=W).grid(row=0,column=2)
    e8=Entry(f1a,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey')
    e8.insert(END,0)
    e8.grid(row=0,column=3)

    Label(f1a,text="CGPA: ",fg='dark blue',font='Arial 16 bold',bg='honeydew3',bd=16,anchor=W).grid(row=1,column=2)
    e10=Entry(f1a,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey')
    e10.grid(row=1,column=3)

    Label(f1a,text=" Hobbies: ",fg='dark blue',font='Arial 16 bold',bg='honeydew3',bd=16,anchor=W).grid(row=2,column=2)
    e11=Entry(f1a,font='Arial 15 bold', bd=10, relief='sunken', bg='light grey')
    e11.grid(row=2,column=3)

   #---------------------------------------------------------------------------------------------------------------------------------------

    Label(f1a,text="Current Course:",fg='dark blue',font='Arial 16 bold',bg='honeydew3',bd=16,anchor=W).grid(row=3,column=0)
    date31=("CSE","ECE","ME","CE","CHE")
    v1=StringVar()
    v1.set(date31[0])
    sb=Spinbox(f1a,values=date31,textvariable=v1,width=10,font='Arisl 17 bold',bg='honeydew3',fg='black').grid(row=3,column=1)
    #sa=v1.get()

    Label(f1a,text="Department:",fg='dark blue',font='Arial 16 bold',bg='honeydew3',bd=16,anchor=W).grid(row=3,column=2)
    date3=("B.Tech","M.Tech")
    v=StringVar()
    v.set(date3[0])
    sb=Spinbox(f1a,values=date3,textvariable=v,width=10,bg='honeydew3',font='Arisl 17 bold',fg='black').grid(row=3,column=3)
    #ss=v.get()

    #------------------------------------- Date of Birth-------------------------------------------------------------------------------------
    Label(f1a,text=" Date of Birth  :",fg='dark blue',font='Arial 16 bold',bg='honeydew3',anchor=W).grid(row=4,column=0)

    spinbox1=Spinbox(f1a,from_=1,to=31,state=NORMAL,width=8,bg='honeydew3',font='Arisl 17 bold')
    spinbox1.grid(row=4,column=1)

    dateList=["Jan","Feb","Mar","Apr","May","jun","July","Aug","Sep","Oct","Nov","Dec"]
    s=StringVar(root)
    s.set(dateList[0])
    dMenu=OptionMenu(f1a,s,*dateList)
    dMenu.grid(row=4,column=2)

    spinbox2=Spinbox(f1a,from_=1990,to=2017,state=NORMAL,width=8,bg='honeydew3',font='Arisl 17 bold')
    spinbox2.grid(row=4,column=3)


##    t1=spinbox1.get()
##    t3=spinbox2.get()
##    t2=s.get()
##       
##    e4=t1+"/"+t2+"/"+t3
##    #---------------------------------------Registration date------------------------------------------------------------------------------------------
    Label(f1a,text="Registration Date :",fg='dark blue',font='Arial 16 bold',bg='honeydew3',anchor=W).grid(row=5,column=0)

    spinbox3=Spinbox(f1a,from_=1,to=31,state=NORMAL,width=8,bg='honeydew3',font='Arisl 17 bold')
    spinbox3.grid(row=5,column=1)

    dateList=["Jan","Feb","Mar","Apr","May","jun","July","Aug","Sep","Oct","Nov","Dec"]
    ss1=StringVar(root)
    ss1.set(dateList[0])
    dMenu=OptionMenu(f1a,ss1,*dateList)
    dMenu.grid(row=5,column=2)

    spinbox4=Spinbox(f1a,from_=1990,to=2017,state=NORMAL,width=8,bg='honeydew3',font='Arisl 17 bold')
    spinbox4.grid(row=5,column=3)


##    w1=spinbox3.get()
##    w3=spinbox4.get()
##    w2=ss1.get()
##       
##    e6=w1+"/"+w2+"/"+w3



    #-----------------------+++++++++++++++++++++++++++++label on right frame++++++++++++++++++++++++++++++++++++-----------------------------------+

    Label(f22,text="    Enrollment no. OF STUDENT     \n   to retrieve data :",fg='dark blue',bg='honeydew3',font='Arial 16 bold').grid(row=0,column=0)
    e12=Entry(f22,font='Arial 12 bold', bd=4, relief='sunken', bg='light grey')
    #e12.insert(END,0)
    e12.grid(row=1,column=0)

    #--------------------------------------------code to clear the fields on inserting the data-----------------------------------------------------------------------------
    def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e8.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        e8.insert(END,0)
        w1=spinbox3.get()
        w3=spinbox4.get()
        w2=ss1.get()
        e6=w1+"/"+w2+"/"+w3
        t1=spinbox1.get()
        t3=spinbox2.get()
        t2=s.get()
       
        e4=t1+"/"+t2+"/"+t3
    #------------------------------------+++++++++++++++++++++++code to insert the data+++++++++++++++++++++++++++++++---------------------------------------+    

    def insert():
        con=sqlite3.Connection('students1')
        cur=con.cursor() 
        try:
            cur.execute("create table if not exists student1(erno varchar(10) primary key,fname char(15) not null,lname char(15) not null,dob date,regdate date,mobileno number(15) unique,cgpa number(8,9),course char(15),department char(15),hobbies char(15) not null)")
            t1=spinbox1.get()
            t3=spinbox2.get()
            t2=s.get()
       
            e4=t1+"/"+t2+"/"+t3
            w1=spinbox3.get()
            w3=spinbox4.get()
            w2=ss1.get()
       
            e6=w1+"/"+w2+"/"+w3
            sa=v1.get()
            ss=v.get()
            b=(e1.get(),e2.get(),e3.get(),e4,e6,int(e8.get()),float(e10.get()),sa,ss,e11.get())
            cur.execute("insert into student1 values(?,?,?,?,?,?,?,?,?,?)",b)
            showinfo("GREAT","Insertion Successful")
        except:
            showerror("enter again","incorrect data")
        con.commit()
        clear()

    #----------------------------============================-----code to check authenticity of mobileno and cgpa-------------=========================================--------

    def checkcgpa():
        w=float(e10.get())
        if w>=0 and w<=10:
            insert()
        else:
            showerror("error","You have entered invalid cgpa")
            clear()
        

    def checkmobno():
        if int(e8.get())!=0:
            a=int(e8.get())
            m=a
            l,r=0,0
            while a!=0:
                r=a%10
                l=l+1
                a=a/10
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
                if (k[9]<7 and k[8]<=7):
                    showerror("oops","Incorrect mobileno.")
                    clear() 
                else:
                   checkcgpa()
        else:
            showerror("oops","ENTER correct DATA")
            clear()



            
    #----------------------------------------------code to print all data on second window-------------------------------------------------------------
    def showall():
        root1=Tk()
        root1.geometry("1380x800+0+0")
        root1.configure(background='DarkGoldenrod4')
        #root1.resizable(0,0)
        first=Frame(root1,width=1200,height=55,bg="black",relief="sunken",bd=10)
        first.pack(side=TOP)
        first.configure(background='DodgerBlue')

        first1=Frame(first,width=1200,height=49,bg="black",relief="sunken",bd=10)
        first1.pack(side=TOP)
        first1.configure(background='darkkhaki')

        f11=Frame(root1,width=1250,height=760,relief="raised",bg='honeydew3',bd=10)
        f11.pack()
        f11.configure(background='black')

        f112=Frame(f11,width=1250,height=760,relief="raised",bg='honeydew3',bd=10)
        f112.pack()
        f112.configure(background='DodgerBlue')
    ##
    ##    f12=Frame(root1,width=1150,height=50,relief="raised",bg='honeydew3',bd=10)
    ##    f12.pack(side=BOTTOM)

        Label(first1,font="times 45 bold underline",text="Student Records",fg="black",bg='red',bd=10,anchor=W).grid(row=0,column=1)
        con=sqlite3.Connection('students1')
        cur=con.cursor()
        
        # +++++++++++++++++++++++++++++++++++++++++++++code to get separate data in form of list++++++++++++++++++++++++++++++++++++
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
        Label(f112,text="Enrollmentno.",fg='black',font='Arial 11 bold',relief="raised",anchor=W,bg='light blue',borderwidth=4,width=14,height=2).grid(row=0,column=0)
        Label(f112,text="Student Name",fg='black',font='Arial 11 bold',relief="raised",anchor=W,bg='light blue',borderwidth=4,width=14,height=2).grid(row=0,column=1)
        Label(f112,text="DateOfBirth",fg='black',font='Arial 11 bold',relief="raised",anchor=W,bg='light blue',borderwidth=4,width=14,height=2).grid(row=0,column=2)
        Label(f112,text="RegistrationDate",fg='black',font='Arial 11 bold',relief="raised",anchor=W,bg='light blue',borderwidth=4,width=14,height=2).grid(row=0,column=3)
        Label(f112,text="Mobileno.",fg='black',font='Arial 11 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=14,height=2).grid(row=0,column=4)
        Label(f112,text="CGPA",fg='black',font='Arial 11 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=14,height=2).grid(row=0,column=5)
        Label(f112,text="Course",fg='black',font='Arial 11 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=14,height=2).grid(row=0,column=6)
        Label(f112,text="Department",fg='black',font='Arial 11 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=14,height=2).grid(row=0,column=7)
        Label(f112,text="Hobbies",fg='black',font='Arial 11 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=14,height=2).grid(row=0,column=8) 
        i,l,k=0,1,0
        for value in a:
            Label(f112,text=a[i],fg='black',font='Arial 10 bold',relief="raised", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k)
            i=i+1
            l=l+1
        i,l,k=0,1,0
        for value in b and c:
            Label(f112,text=b[i]+c[i],fg='black',font='Arial 10 bold',relief="raised", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,1
        for value in d:
            Label(f112,text=d[i],fg='black',font='Arial 10 bold',relief="raised", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,2
        for value in e:
            Label(f112,text=e[i],fg='black',font='Arial 10 bold',relief="raised", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,3
        for value in f:
            Label(f112,text=f[i],fg='black',font='Arial 10 bold',relief="raised", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,4
        for value in g:
            Label(f112,text=g[i],fg='black',font='Arial 10 bold',relief="raised", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,5
        for value in w:
            Label(f112,text=w[i],fg='black',font='Arial 10 bold',relief="raised", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,6
        for value in r:
            Label(f112,text=r[i],fg='black',font='Arial 10 bold',relief="raised", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        i,l,k=0,1,7
        for value in qq:
            Label(f112,text=qq[i],fg='black',font='Arial 10 bold',relief="raised", bd=4,bg='dark grey',width=15,height=2).grid(row=l,column=k+1)
            i=i+1
            l=l+1
        
        Button(f112,text="Click to go back",bg='green',fg='black',font='Arial 8 bold',relief="groove",width=15,height=2,command=root1.destroy).grid(row=l+1,column=6)
        root1.mainloop()
                
    #-------------------------++++++++++++++++++++++++++++++++code to see any particular data++++++++++++++++++=---------------------------------------------------++

    def show():
        con=sqlite3.Connection('students1')
        cur=con.cursor()
        cur.execute("select * from student1 where erno=?",(e12.get(),))
        a=[]
        a=cur.fetchall()
        if(e12.get()!=""):
            if a:
                showinfo("      DATA    ",a)
                showinfo("Successful","Retrieved Successfuly")
            else:
                showerror("error","data not found")
        else:
            showerror("error","incorrect data")
        e12.delete(0,END)
        #e12.insert(END,0)

 
    #---------------------------------------------code to destroy root window-------------------------------------------------------------------------------------
    def quitx():
        q=askyesno("Exit system","Do you want to really quit")
        if q>0:
            root.destroy()
            return


    Button(f1a,text="Insert",fg='dark red',font='Arial 17 bold',justify="left",width=15,bd=9,bg='darkkhaki',command=checkmobno).grid(row=8,column=1)
    Button(f1a,text="Reset",fg='dark red',font='Arial 17 bold',justify="left",width=15,bd=9,bg='honeydew3',command=clear).grid(row=8,column=2)
    Button(f1a,text="Show All",fg='dark red',font='Arial 17 bold',justify="right",bd=9,bg='darkkhaki',width=15,command=showall).grid(row=8,column=3)
    Button(f22,text="Retrieve data ",fg='dark red',font='Arial 15 bold',bd=8,bg='darkkhaki',command=show).grid(row=2,column=0,columnspan=2)
    Button(f22,text="Quit ",fg='dark red',font='Arial 12 bold',bd=8,bg='darkkhaki',command=quitx).grid(row=3,column=0)
    #Button(f22,text="About Developer ",fg='dark red',font='Arial 10 bold',bd=7,bg='darkkhaki',command=developer).grid(row=4,column=0)


    root.mainloop()





#______________________++++++++++++++++++++++___________code for first page (for developers details)___________________________+++++++++++++++++++++++++
    
f=Frame(root11,width=1200,height=150,bg="black",relief="sunken",bd=10)#bottom frame on first page for image
f.pack(side=TOP)
f.configure(background='black')


ff=Frame(root11,width=1200,height=750,bg="black",relief="sunken",bd=10)#top frame on bottom frame for image
ff.pack()
ff.configure(background='DodgerBlue')

f2=Frame(root11,width=1200,height=100,bg="black",relief="sunken",bd=10) #bottom frame for details  
f2.pack()
f2.configure(background='DodgerBlue')


ff1=Frame(ff,width=1200,height=500,bg="black",relief="sunken",bd=10)#top frame for details
ff1.pack()
ff1.configure(background='DodgerBlue')

Label(ff1,text="NAME     ",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=1,column=0)
Label(ff1,text="SHAKIR KHAN",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=1,column=3)
Label(ff1,text="Enrollmentno.",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=2,column=0)
Label(ff1,text="161B207",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=2,column=3)
Label(ff1,text="COURSE",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=3,column=0)
Label(ff1,text="B.TECH.",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=3,column=3)
Label(ff1,text="BRANCH ",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=4,column=0)
Label(ff1,text="CSE  ",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=4,column=3)
Label(ff1,text="BATCH  ",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=5,column=0)
Label(ff1,text="B7 (BZ) ",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=5,column=3)
Label(ff1,text="email-id ",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=6,column=0)
Label(ff1,text="me.shakir1996@gmail.com",fg='black',font='Arial 20 bold',relief="raised",bg='light blue',anchor=W,borderwidth=4,width=21,height=2).grid(row=6,column=3)

Label(f2,text="         Move cursor over top image to proceed to mainpage",fg='black',font='Arial 20 bold',relief="raised",bg='darkkhaki',anchor=W,borderwidth=4,width=50,height=2).grid(row=0)



a=PhotoImage(file='images/Header2.gif')#to get header image on first page
l=Label(f,image=a)
l.bind('<Motion>',quitx2)# splash screen to distroy the first page when mouse is moved over the image
l.grid()
root11.mainloop()
