from tkinter import*
from tkinter import ttk
from datetime import datetime
import tkinter.messagebox
from tkcalendar import DateEntry

root= Tk()

appointment_type= StringVar()
appointment_description= StringVar()

date_label=Label(root,text="Date", font=("arial", 14, "bold"), bd=7)
date_label.grid(row=0,column=0,sticky=W)
#Using tkcalender module
date_entry = DateEntry(root, background='darkblue', foreground='white', borderwidth=2, width= 14)
date_entry.grid(row=0,column=1)

#---------------------------------------------------------------------------------------------


lbl_appointment= Label(root, font=("arial", 14, "bold"), text= "Types of appointments", bd=7)
lbl_appointment.grid(row=1, column=0, sticky=W)

cmbo_appointment= ttk.Combobox(root, textvariable= appointment_type, state= "readonly", font= ("arial", 14, "bold"), width= 14)
cmbo_appointment["value"]= ("Onetime", "Daily", "Monthly")
cmbo_appointment.current(0)
cmbo_appointment.grid(row=1, column=1)

#---------------------------------------------------------------------------------------------

lbl_appoint_description= Label(root, font=("arial", 14, "bold"), text= "Appointment description", bd=7)
lbl_appoint_description.grid(row=2, column=0, sticky=W)

cmbo_appoint_description= ttk.Combobox(root, textvariable= appointment_description, state= "readonly", font= ("arial", 14, "bold"), width= 14)
cmbo_appoint_description["value"]= ("general", "chiropractic", "pediatric", "heart", "gastro", "skin", "osteo")
cmbo_appoint_description.current(0)
cmbo_appoint_description.grid(row=2, column=1)

#-----------------------------------  Button   -------------------------------------------

btn_add= Button(root, padx=18, bd=7, font= ("arial", 16, "bold"), width= 40, text= "See all current Appointments").grid(row=3, column=0)
btn_add= Button(root, padx=18, bd=7, font= ("arial", 16, "bold"), width= 40, text= "See all current Appointments on a given date").grid(row=4, column=0)
btn_add= Button(root, padx=18, bd=7, font= ("arial", 16, "bold"), width= 40, text= "Make a new Appointment").grid(row=5, column=0)
btn_add= Button(root, padx=18, bd=7, font= ("arial", 16, "bold"), width= 40, text= "Cancel an existing Appointment").grid(row=6, column=0)
btn_add= Button(root, padx=18, bd=7, font= ("arial", 16, "bold"), width= 40, text= "See Appointments according to description").grid(row=3, column=1)
btn_add= Button(root, padx=18, bd=7, font= ("arial", 16, "bold"), width= 40, text= "Reload Appointment data from a File").grid(row=4, column=1)
btn_add= Button(root, padx=18, bd=7, font= ("arial", 16, "bold"), width= 40, text= "Exit the Program").grid(row=5, column=1)

root.mainloop()
