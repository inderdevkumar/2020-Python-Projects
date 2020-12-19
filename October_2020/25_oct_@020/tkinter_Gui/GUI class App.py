from tkinter import*
import tkinter.messagebox
from tkinter import messagebox
from datetime import datetime
import math
import cmath

root= Tk()
root.title("Calculator") #it will give a title   

root.geometry("820x400")
root.configure(background= "black")
#----------------------------------------------Variables------------------------------------------------

display= StringVar()
exp= ""
#----------------------------------------------func def------------------------------------------------


    
def to_add():
    global exp
    sign= "+"
    exp= exp + sign
    display.set(exp)

def to_equal():
    try:


        global exp
        exp=  str(eval(exp))
        display.set(exp)

    except SyntaxError:
        display.set("Invalid Expression")
        #messagebox.showinfo(title="Warning: ", message="Expression is not valid, please double check ...")



def to_multply():
    global exp
    sign= "*"
    exp= exp + sign
    display.set(exp)

def to_subtract():
    global exp
    sign= "-"
    exp= exp + sign
    display.set(exp)

def to_divide():
    global exp
    sign= "/"
    exp= exp + sign
    display.set(exp)

def precentage():
    global exp
    sign= "%"
    exp= exp + sign
    display.set(exp)


def to_stop():
    global exp
    sign= "."
    exp= exp + sign
    display.set(exp)
    
     

        


    
    
    

def to_sqrt():
    global exp
    
    exp=  str(math.sqrt(float(exp)))
    display.set(exp)



def to_erase():
    global exp
    
    exp=exp[:-1]
    display.set(exp)

    

 

def to_clr():
    global exp
    
    exp= ""
    display.set(exp)

def to_exit():
    
    display.set(today)
    iExit= tkinter.messagebox.askyesno("MY Scientific CALC", "Please confirm if you wish to exit")
    if iExit > 0:
        root.destroy()

#----------------------------------------------NUmber entry func def------------------------------------------------
def key_dot():
    global exp
    num= "."
    exp= exp + num
    display.set(exp)
def Num_0():
    global exp
    num= "0"
    exp= exp + num
    display.set(exp)
  
def Num_1():
    global exp
    num1= "1"
    exp= exp + num1
    display.set(exp)

def Num_2():
    global exp
    num2= "2"
    exp= exp + num2
    display.set(exp)

def Num_3():
    global exp
    num3= "3"
    exp= exp + num3
    display.set(exp)

def Num_4():
    global exp
    num4= "4"
    exp= exp + num4
    display.set(exp)

def Num_5():
    global exp
    num5= "5"
    exp= exp + num5
    display.set(exp)
    
def Num_6():
    global exp
    num6= "6"
    exp= exp + num6
    display.set(exp)
    
def Num_7():
    global exp
    num7= "7"
    exp= exp + num7
    display.set(exp)
   
def Num_8():
    global exp
    num8= "8"
    exp= exp + num8
    display.set(exp)
    

def Num_9():
    global exp
    num9= "9"
    exp= exp + num9
    display.set(exp)
    

#---------------------------------------For heading and frames---------------------------------------

MainFrame= Frame(root)
MainFrame.grid()

Top= Frame(MainFrame, bd= 15, width= 900, relief= RIDGE)
Top.pack(side= TOP)



btn_Display_frame = Frame(MainFrame, bd= 10, width= 900, height= 50, relief= RIDGE)
btn_Display_frame.pack(side= BOTTOM)

Display_frame = Frame(btn_Display_frame, bd= 5, width= 900, height= 40, relief= RIDGE)
#Display_frame.pack(side= BOTTOM)
Display_frame.grid(row=0, column=0)

Button_frame = Frame(btn_Display_frame, bd= 10, width= 900, height= 400, relief= RIDGE)
Button_frame.grid(row=1, column=0)



#---------------------------------------For dispay---------------------------------------

# txt_display= Text(Display_frame, width=60, height= 10, font= ("arial", 10, "bold"))
# txt_display.grid(row=0, column=0)


txtdisplay= Entry(Display_frame, font=("arial", 35, "bold"), textvariable= display, bd=10, bg= "black", fg="white", insertwidth= 2, justify= RIGHT)
txtdisplay.grid(row=0, column=0)


#---------------------------------------For buttons---------------------------------------

btnplus= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "+", command= to_add)
btnplus.grid(row=1, column=8)

btnequal= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "=", command= to_equal)
btnequal.grid(row=5, column=8)

btnminus= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "-", command= to_subtract)
btnminus.grid(row=2, column=8)

btnmultipln= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "*", command= to_multply)
btnmultipln.grid(row=3, column=8)

btndivide= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "/", command= to_divide)
btndivide.grid(row=4, column=8)




btndot= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= ".", command= to_stop)
btndot.grid(row=3, column=7)

btnclr= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "clr", command= to_clr)
btnclr.grid(row=3, column=8)

btnexit= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "exit", command= to_exit)
btnexit.grid(row=3, column=9)






#---------------------------------------For number buttons---------------------------------------
btn_MC= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "MC", command= key_MC)
btn_MC.grid(row=0, column=5)

btn_M= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "M+", command= keyM)
btn_M.grid(row=0, column=6)

btnM= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "M-", command= key_M)
btnM.grid(row=0, column=7)

btn_MR= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "MR", command= key_MR)
btn_MR.grid(row=0, column=8)

btn7= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "7", command= Num_7)
btn7.grid(row=2, column=5)

btn8= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "8", command= Num_8)
btn8.grid(row=2, column=6)

btn9= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "9", command= Num_9)
btn9.grid(row=2, column=7)

btn4= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "4", command= Num_4)
btn4.grid(row=3, column=5)

btn5= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "5", command= Num_5)
btn5.grid(row=3, column=6)

btn6= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "6", command= Num_6)
btn6.grid(row=3, column=7)

btn1= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "1", command= Num_1)
btn1.grid(row=4, column=5)

btn2= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "2", command= Num_2)
btn2.grid(row=4, column=6)

btn3= Button(Button_frame, padx=18, bd=7, font= ("arial", 16, "bold"), width= 2, text= "3", command= Num_3)
btn3.grid(row=4, column=7)

btn0= Button(Button_frame, padx=5, bd=7, font= ("arial", 16, "bold"), width= 2, text= "0", command= Num_0)
btn0.grid(row=5, column=5)

btndot= Button(Button_frame, padx=5, bd=7, font= ("arial", 16, "bold"), width= 2, text= ".", command= key_dot)
btndot.grid(row=5, column=6)

root.mainloop() # it will run with an infinite loop
