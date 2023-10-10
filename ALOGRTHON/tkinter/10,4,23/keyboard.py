import tkinter as tk
import random
window = tk.Tk()
window.title("Image viewer")
window.geometry("600x400")
frame = tk.Frame(window, width=600, height=400)
frame.pack()
canvas = tk.Canvas(frame, width=600, height=400)
canvas.pack()
canvas.create_rectangle(10,10,100,100,tags="rectangle")
canvas.create_rectangle(10,110,100,200)
def change_color(event):
    if event.keysym == 'Up':
        canvas.itemconfig(canvas.find_withtag('rectangle'), fill='green')
    elif event.keysym == 'Down':
        canvas.itemconfig(canvas.find_withtag('rectangle'), fill='black')
    elif event.keysym == 'Right':
        canvas.itemconfig(canvas.find_withtag('rectangle'), fill='red')
    elif event.keysym == 'Left':
        canvas.itemconfig(canvas.find_withtag('rectangle'), fill='blue')
    elif event.keysym == 'g':
        canvas.itemconfig(canvas.find_withtag('rectangle'), fill='pink')
window.bind("<Key>", change_color)      
window.mainloop()