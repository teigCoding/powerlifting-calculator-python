import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Powerlifting Calculator")
window.geometry("380x250")


frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

labels = [
    "Squat:",
    "Bench Press:",
    "Deadlift:",
    "Bodyweight:"
]

entry1 = {}


def calculate_stats(event):
    newList = []
    brandList = []
    total = 0
    for x in entry1:
        newList.append(entry1[x])
    

    bodyweight = newList.pop().get()
    for index,x in enumerate(newList):
        if newList[index].get() != "":
            brandList.append(int(newList[index].get()))
            total += (brandList[index])
        else:
            lbl_result["text"] = "Please fill out all the fields!"
            return
            
    if bodyweight != "":
        timesBodyWeight = int(total)/int(bodyweight)
        lbl_result["text"] = f"Your total is {total} and that's {round(timesBodyWeight,2)}x bodyweight!"
    else:
        lbl_result["text"] = f"Your total is {total}"

def clear_stats(event):
    newList = []
    lbl_result["text"] = ""
    for x in entry1:
        newList.append(entry1[x])
    for index,x in enumerate(newList):
        newList[index].delete(0,END)

for idx, text in enumerate(labels):
    label = tk.Label(master=frm_form, text=text)
    entry1[idx] = tk.Entry(master=frm_form, width=50)
    label.grid(row=idx, column=0, sticky="ew")
    entry1[idx].grid(row=idx, column=1)



frm_buttons = tk.Frame()
frm_buttons.pack()


btn_submit = tk.Button(master=frm_buttons, text="Submit",width=7)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)


btn_clear = tk.Button(master=frm_buttons, text="Clear",width=7)
btn_clear.pack(side=tk.RIGHT, ipadx=10)

frm_result = tk.Frame()
frm_result.pack()

lbl_result = tk.Label(master=frm_result)
lbl_result.grid(row=0, column=0,pady=(20,0))

btn_submit.bind("<Button-1>", calculate_stats)
btn_clear.bind("<Button-1>", clear_stats)   

window.mainloop()
