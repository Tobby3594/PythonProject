from tkinter import *
app = Tk()
app.title("Base Gui")
app.geometry("200x100+400+300")
app.configure(bg = "green")
lblNum = Label(app, text="Please enter a number:", height = 10)
lblNum.pack()
app.mainloop()