import tkinter as tk
import random
window = tk.Tk()
window.geometry("500x500")
window.resizable(0,0)
frame = tk.Frame(window, bg='orange')
frame.pack()
canvas = tk.Canvas(frame, width=500, height=500)
canvas.pack()
canvas.create_rectangle(10, 10, 100, 100, fill='orange')
canvas.create_rectangle(110, 10, 200, 100, fill='red')
canvas.create_rectangle(210, 10, 300, 100, fill='green')
canvas.create_rectangle(310, 10, 400, 100, fill='purple')
canvas.create_rectangle(410, 10, 500, 100, fill='purple')

canvas.create_rectangle(110, 410, 200, 500, fill='orange')
canvas.create_rectangle(210, 410, 300, 500, fill='orange')
canvas.create_rectangle(310, 410, 400, 500, fill='orange')


canvas.create_rectangle(10, 110, 100, 200, fill='purple')
canvas.create_rectangle(10, 210, 100, 300, fill='purple')
canvas.create_rectangle(10, 310, 100, 400, fill='purple')
canvas.create_rectangle(10, 410, 100, 500, fill='purple')


canvas.create_rectangle(410, 110, 500, 200, fill='purple')
canvas.create_rectangle(410, 210, 500, 300, fill='purple')
canvas.create_rectangle(410, 310, 500, 400, fill='purple')
canvas.create_rectangle(410, 410, 500, 500, fill='purple')

canvas.create_oval(210, 210, 310, 310, fill='black')
def change_color(even):
    x = canvas.canvasx(even.x)
    y = canvas.canvasy(even.y)
    shape_id = canvas.find_closest(x, y)
    canvas.itemconfig(shape_id, fill = random.choice(arr))
arr = ['black','orange','red','green','yellow','gray','purple','white']
canvas.bind("<Button-1>", change_color)
window.mainloop()

