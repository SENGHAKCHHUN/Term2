import tkinter as tk
import time
from tkinter import messagebox as nsg
window = tk.Tk()
window.geometry("400x300")
window.title("timer")
window.resizable(False,False),
def on_clonsing():
    if nsg.askokcancel("Quit", "Do you want ot quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_clonsing)
frame = tk.Frame(window)
frame.pack()
canvas = tk.Canvas(frame, width=400, height=300, bg='orange')
canvas.pack()
time_id = canvas.create_text(190,150, text='', font=('bold',50), fill='white')
def clock():
    hour = time.strftime("%H:%M:%S")
    canvas.itemconfig(time_id, text= hour)
def update_time():
    clock()
    window.after(1000,update_time)
window.after(1000, update_time)
window.mainloop()