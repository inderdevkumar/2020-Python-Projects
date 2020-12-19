from tkinter import*
import name_backend as backend

root= Tk()
root.title("HW-Database")
root.geometry("410x330")
root.configure(background= "grey")

name_text=StringVar()
#==================Functiion Defination==========================================


#To make list box selectable
def get_selected_row(event):
    global selected_tuple
    index=list_box.curselection()[0]
    selected_tuple=list_box.get(index)
    print(selected_tuple) 
    
#To insert name into database    
def insert_into_db():
    name_var= name_text.get()
    #print(name_var)
    backend.insert(name_var)


#========================  Widgets  =============================================
label_name=Label(root,font=("arial", 14, "bold"), text="Name")
label_name.grid(row=0,column=0)

entry_name=Entry(root,font=("arial", 14, "bold"), bd=7, textvariable=name_text)
entry_name.grid(row=0,column=1)

label_list=Label(root,font=("arial", 14, "bold"), text="Roster")
label_list.grid(row=1,column=0)

list_box=Listbox(root, height=15,width=50)
list_box.grid(row=2,column=0, columnspan= 2)

sb1=Scrollbar(root)
sb1.grid(row=2,column=2, sticky=NS)  #Fpr scrolbar

list_box.configure(yscrollcommand=sb1.set)
sb1.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>',get_selected_row)  #To select row of list


btn_submit= Button(root, padx=18, bd=7, font= ("arial", 16, "bold"), text="Submit", width=4,command= insert_into_db)
btn_submit.grid(row=0,column=2)


#The values of Database are displayed once program is run
list_box.delete(0,END)
for row in backend.view():
    list_box.insert(END,row)

root.mainloop()
