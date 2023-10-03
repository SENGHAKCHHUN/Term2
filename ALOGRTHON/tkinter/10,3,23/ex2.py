import tkinter as tk
import random
window = tk.Tk()
window.geometry("510x510")
window.resizable(0,0)
frame = tk.Frame(window, bg='orange')
frame.pack()
canvas = tk.Canvas(frame, width=510, height=510)
canvas.pack()
# canvas.create_oval(10, 10 ,100, 100, fill='orange')
# canvas.create_oval(110, 110, 200, 200,fill='red')
# canvas.create_oval(210,210,300,300,fill='red')
# canvas.create_oval(310,310,400,400,fill='red')
# canvas.create_oval(410,410,500,500,fill='red')
for i in range(5):
    canvas.create_oval(10+i*100, 10 +i *100, 100 + i *100 , 100 + i *100, fill='orange')
    canvas.create_rectangle(410-i*100, 410+i*100, 500 -i *100, 500 -i *100,fill='red' )
window.mainloop()