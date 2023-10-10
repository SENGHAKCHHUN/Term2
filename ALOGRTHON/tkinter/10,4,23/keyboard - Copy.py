import tkinter as tk
import random
window = tk.Tk()
window.title("Image viewer")
window.geometry("600x400")
window.resizable(False,False)
frame = tk.Frame(window, width=600, height=400)
frame.pack()
canvas = tk.Canvas(frame, width=600, height=400)
canvas.pack()
rect_id = canvas.create_oval(10,10,100,100,tags="rectangle", fill='orange')
def moveLeft():
    if canvas.coords(rect_id)[0] > 10:
        canvas.move(rect_id, -10, 0)
def moveRight():
    if canvas.coords(rect_id)[2] < 590:
        canvas.move(rect_id, 10, 0)
def moveUp():
    if canvas.coords(rect_id)[1] > 10:
        canvas.move(rect_id, 0, -10)
def moveDown():
    if canvas.coords(rect_id)[3] < 390:
        canvas.move(rect_id, 0, 10)
def move(event):
    if event.keysym == 'Up':
        moveUp()
    elif event.keysym == 'Down':
        moveDown()
    elif event.keysym == 'Right':
        moveRight()
    elif event.keysym == 'Left':
        moveLeft()
window.bind("<Key>", move)    
window.mainloop()