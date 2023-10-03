import tkinter as tk
import random
window = tk.Tk()
window.geometry("410x510")
window.resizable(0,0)
frame = tk.Frame(window, bg='orange')
frame.pack()
canvas = tk.Canvas(frame, width=410, height=510)
canvas.pack()
canvas.create_rectangle(10, 350, 100, 500, fill='orange')
canvas.create_rectangle(110, 200, 200, 500, fill='orange')
canvas.create_rectangle(210, 300, 300, 500, fill='orange')
canvas.create_rectangle(310, 100, 400, 500, fill='orange')
window.mainloop()