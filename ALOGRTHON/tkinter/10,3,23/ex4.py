import tkinter as tk
import random
window = tk.Tk()
window.geometry("410x510")
window.resizable(0,0)
frame = tk.Frame(window, bg='orange')
frame.pack()
canvas = tk.Canvas(frame, width=410, height=510)
canvas.pack()
canvas.create_rectangle(10 , 310 , 150 , 400, fill='red')
canvas.create_rectangle(150 , 200 , 300 , 300, fill='red')
canvas.create_rectangle(310 , 310 , 500 , 500, fill='red')
canvas.create_oval(30,200,120,300,fill='orange')
window.mainloop()