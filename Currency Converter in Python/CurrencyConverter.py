import tkinter as tk
from tkinter import *
from tkinter import ttk
import urllib.request, urllib.parse , urllib.error
import json



#connect to derver
def convertToServer():
    fhand = urllib.request.urlopen("https://api.exchangerate-api.com/v4/latest/USD").read()
    data=json.loads(fhand)
    return data

#func to convert
def convert():
    try:
        _from=_select_from.get()
        _from_count = int(inp_from.get())
        _to =_select_to.get()
        _json=convertToServer()
        currency_value_from=_json["rates"][_from]
        USD_value=(1/currency_value_from)*_from_count
        currency_value_to=_json["rates"][_to]*USD_value
        tv_result.set(str(currency_value_to))
        # label to
        lbl_to_resulr = Label(f, text=tv_result.get(), anchor="w")
        lbl_to_resulr.pack(fill="y")
        #lbl error
        lbl_error.destroy()
        print(currency_value_to)
    except:
        # lbl error
        lbl_error.pack(fill="y")

f = Tk()
f.title(" Currency Converter in Python")
# f.configure(bg = "blue")
f.geometry("350x250+400+300")

# tv result
tv_result = StringVar()
tv_result.set("")

#tv title
tv_title = StringVar()
_json = convertToServer()
tv_title.set(_json["date"])

# tv error
lbl_error = Label(f, text="pleas enter all values", anchor="w")

#list of cons
data=convertToServer()
arr_cons=list(data["rates"].keys())

lbl_hand = Label(f, text="Today is "+tv_title.get(), anchor="w")
lbl_hand.pack(side="top",padx=80, pady=15)

#label from
lbl_from = Label(f, text="From: ", anchor="w")
lbl_from.pack(fill="y")

#select cons from
_from_n = tk.StringVar()
_select_from = ttk.Combobox(f, width = 27, textvariable = _from_n)
_select_from['values'] = arr_cons
_select_from.pack()

#input from
inp_from = Entry(f)
inp_from.pack()

#label to
lbl_to = Label(f, text="To", anchor="w")
lbl_to.pack(fill="y")

#select cons to
_to_n = tk.StringVar()
_select_to = ttk.Combobox(f, width = 27, textvariable = _to_n)
_select_to['values'] = arr_cons
_select_to.pack()

#button to convert
btn = Button(f, text="Convert" ,command=convert)
btn.pack(side= "bottom", padx=80, pady=12)

f.mainloop()
