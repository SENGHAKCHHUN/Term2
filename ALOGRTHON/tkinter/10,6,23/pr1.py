# import tkinter as tk
# from tkinter import messagebox as nsg
# import random
# window = tk.Tk()
# window.title("Hak gaming")
# window.geometry("600x500")
# window.resizable(False, False)
# def on_clonsing():
#     if nsg.askokcancel("Quit", "Do you want to quit ?"):
#         window.destroy()
# window.protocol("WM_DELETE_WINDOW", on_clonsing)
# canvas = tk.Canvas(window,)
# canvas.pack()
# rect = canvas.create_rectangle(150, 150, 250 ,250, fill='orange')
# def changeColor(event):
#     canvas.itemconfig(rect, fill =random.choice(arr))
# arr = ['white', 'gray','red','orange','purple','pink']
# window.bind("<Button-1>", changeColor)
# window.mainloop()


import tkinter as tk
import time
window = tk.Tk()
window.title("timer")
window.geometry("200x100")
window.config(bg='black')
canvas = tk.Canvas(window, width=200, height=100)
canvas.pack()
time_id = canvas.create_text(100,50, text='', font=('bold', 30), fill='orange')
def clock():
    hour = time.strftime("%H:%M:%S")
    canvas.itemconfig(time_id, text = hour)
def updateTime():
    clock()
    window.after(1000, updateTime)
window.after(1000, updateTime)
window.mainloop()


