from tkinter import *
from tkinter import messagebox
from tkinter import ttk


root = Tk()
root.title("Calculator") 


#logic of calculator
def calc(key):
    global memory
    if key == "=":
#spelling exception 
        str1 = "-+0123456789.*/"
        if calc_entery.get()[0] not in str1:
            calc_entery.insert(END, "First symwol is not number!")
            messagebox.showerror("Eror!")

#score
        try:
            result = eval(calc_entery.get())
            calc_entery.insert(END, "=" + str(result))
        except:
            calc_entery.insert(END, "Error!")
            messagebox.showerror("Error!", "Please try again")
#clear the field
    elif key == "C":
        calc_entery.delete(0, END)

#change +-
    elif key == "-/+":
        if "=" in calc_entery.get():
            calc_entery.delete(0, END)
        try:
            if calc_entery.get()[0] == "-":
                calc_entery.delete(0)
            else:
                calc_entery.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calc_entery.get():
            calc_entery.delete(0, END)
        calc_entery.insert(END, key)
              

#creat buttons
bttn_list = [
    "7", "8", "9",  "+", "-",
    "4", "5", "6",  "*", "/",
    "1", "2", "3",  "-/+", "=",
    "0", ".", "C", "", ""
]

r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c>4:
        c=0
        r += 1

calc_entery = Entry(root, width=33)
calc_entery.grid(row=0, column=0, columnspan=5)   


root.mainloop()