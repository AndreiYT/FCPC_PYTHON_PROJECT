
from tkinter import Tk, StringVar, ttk, Frame
from tkinter import *
import time
import datetime

window = Tk()

window.title("Currency Converter")

window.geometry("775x160")


#Frame Spacing
LeftMainFrame = Frame(window, relief="raise")
LeftMainFrame.pack(side=LEFT)

#String
DateofOrder = StringVar()
value0 = StringVar()
convert = DoubleVar()
currency = DoubleVar()

#Function
def ConCurrency():
    if value0.get() == "USA":
        convert1 = float(convert.get() * 51.895392)
        convert2 = "USA Dollars", str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "Japan":
        convert1 = float(convert.get() * 0.463493)
        convert2 = "Japanese Yen", str('%.2f' %(convert1))
        currency.set(convert2)
    elif value0.get() == "Euro":
        convert1 = float(convert.get() * 58.980601)
        convert2 = "Euro", str('%.2f' % (convert1))
        currency.set(convert2)
    elif value0.get() == "India":
        convert1 = float(convert.get() * 0.731426)
        convert2 = "Indian Rupee", str('%.2f' % (convert1))
        currency.set(convert2)
    elif value0.get() == "Brazil":
        convert1 = float(convert.get() * 13.721358)
        convert2 = "Brazillian Real", str('%.2f' % (convert1))
        currency.set(convert2)

#Reset
def Reset():
    value0.set("")
    convert.set("0.0")
    currency.set("0.0")

#-----------------Date------------------
DateofOrder.set(time.strftime("%d/%m/%Y"))
#-----------------Date------------------

#Entry
Entry1= Entry(LeftMainFrame,font=('arial',20,'bold'), textvariable=convert, width=19, justify='center')
Entry1.grid(row=1, column=1)

#Label
label1= Label(LeftMainFrame, font=('arial',20,'bold'), text='Philippine Peso Equals')
label1.grid(row=1, column=2, sticky=W)
#------------------------------------------------------------------------------------------------------------------#

box = ttk.Combobox(LeftMainFrame, textvariable=value0, state='readonly',font=('arial',20,'bold'))
box['values'] = (' ', 'USA', 'Japan', 'Euro', 'India', 'Brazil')
box.current(0)
box.grid(row=2, column=2)

#Label
label2= Label(LeftMainFrame, font=('arial', 20, 'bold'), textvariable=currency ,width=17, background='white',
              relief='sunken')
label2.grid(row=2, column=1)

#------------------------------------------------------------------------------------------------------------------#

#Label
label3= Label(LeftMainFrame, font=('arial', 20, 'bold'), textvariable=DateofOrder, justify='center')
label3.grid(row=0, column=7, sticky=W)

#Button
button1 = Button(LeftMainFrame, text='Convert', font=('arial', 20, 'bold'), command=ConCurrency)
button1.grid(row=1, column=7)

button2 = Button(LeftMainFrame, text='Reset', font=('arial', 20, 'bold'), command=Reset)
button2.grid(row=2,column=7)


window.mainloop()
