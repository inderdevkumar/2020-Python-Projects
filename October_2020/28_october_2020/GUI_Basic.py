from tkinter import *
from tkinter import messagebox  
import time
from tkcalendar import DateEntry

window= Tk()
  
# Creating frame
login_frame = LabelFrame(window, text="Work Productivity", padx=5, pady=5)
login_frame.pack(padx=15, pady=10)

#Creating Label in tkinter
l1=Label(login_frame,text="Date: ")
l1.grid(row=0,column=0,sticky=E, pady=3)

l2=Label(login_frame,text="Employee ID: ")
l2.grid(row=1,column=0,sticky=E, pady=3)

l3=Label(login_frame,text="Hours in VDI: ")
l3.grid(row=2,column=0,sticky=E, pady=3)

l4=Label(login_frame,text="Planned number of Automation Script Developed(Count): ")
l4.grid(row=3,column=0,sticky=E, pady=3)

l5=Label(login_frame,text="Actual number of Automation Script Developed(Count): ")
l5.grid(row=4,column=0,sticky=E, pady=3)

l6=Label(login_frame,text="Planned number of Automation Script Executed(Count): ")
l6.grid(row=5,column=0,sticky=E, pady=3)


#Using tkcalender module
cal = DateEntry(login_frame, background='darkblue', foreground='white', borderwidth=2)
cal.grid(row=0,column=1)

task2_text= StringVar()
e11=Entry(login_frame,textvariable=task2_text)
e11.grid(row=1,column=1, ipady=1)

hour_var= StringVar()
hour_choices = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
hour_var.set('Hours') # set the default option
popupMenu1 = OptionMenu(login_frame, hour_var, *hour_choices)
popupMenu1.grid(row = 2, column =1, sticky=W+N+S+E)

min_var= StringVar()
min_choices = ['10 min','20 min','30 min','40 min','50 min']
min_var.set('00 min') # set the default option
popupMenu2 = OptionMenu(login_frame, min_var, *min_choices)# * is used to get option below one adter the otehr
popupMenu2.grid(row = 2, column =2, sticky=W+N+S+E)

task4_text=StringVar()
e3=Entry(login_frame,textvariable=task4_text)
e3.grid(row=3,column=1, ipady=1)

task5_text=StringVar()
e4=Entry(login_frame,textvariable=task5_text)
e4.grid(row=4,column=1, ipady=1)

task6_text=StringVar()
e5=Entry(login_frame,textvariable=task6_text)
e5.grid(row=5,column=1, ipady=1)


b1=Button(login_frame,text="Submit")
b1.grid(row=6,column=1, pady=3)

b2=Button(login_frame,text="Close")
b2.grid(row=6,column=0)

b3=Button(login_frame,text="Pull Data in Excel!")
b3.grid(row=6,column=2)

window.mainloop()
