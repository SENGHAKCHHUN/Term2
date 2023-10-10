import tkinter as tk
window = tk.Tk()
window.geometry("600x400")
window.title("Move Game")
window.resizable(0, 0)
#frame 
frame = tk.Frame(window)
frame.pack()

#canvas

canvas = tk.Canvas(frame, width =500, height = 350, bg="white")
canvas.pack(pady=20)
shape_id = canvas.create_rectangle(0, 0, 50, 50, fill = "black")
rect_id = canvas.create_rectangle(120, 10, 170, 140, fill='yellow')
rect_id = canvas.create_rectangle(250, 250, 300, 350, fill='orange')
print(canvas.coords(rect_id))
def check_shape_on_left():
    if canvas.coords(shape_id)[0] > 0 and (canvas.coords(shape_id)[0] < 100 or canvas.coords(shape_id)[0] > 170 or canvas.coords(shape_id)[3]> 140):
        print(canvas.coords(shape_id))
        canvas.move(shape_id, -10, 0)
def check_shape_on_right():
    if canvas.coords(shape_id)[2] <500:
       canvas.move(shape_id, 10, 0)
def check_shape_on_top():
    if canvas.coords(shape_id)[1] >0:
        canvas.move(shape_id,0,-10)
def check_shape_on_bottom():
    if canvas.coords(shape_id)[3] < 350:
        canvas.move(shape_id,0,10)
def moveShape(event):
    if event.keysym == 'Up':
        check_shape_on_top()
    elif event.keysym == 'Left':
        check_shape_on_left()
    elif event.keysym == 'Right':
        check_shape_on_right()
    elif event.keysym == 'Down':
        check_shape_on_bottom()
window.bind("<Key>", moveShape)
window.mainloop()
