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
canvas.create_rectangle(0, 300, 500, 350, fill = "black", tags='wall')
def check_moveable():
    coord = canvas.coords(shape_id)
    print(coord)
    walls = canvas.find_withtag("wall")
    print(walls)
    touch = canvas.find_overlapping(coord[0], coord[1], coord[2], coord[3])
    print(touch)
    for wall in walls:
        if wall in touch:
            return False
    return True
def gravity():
    if check_moveable():
        canvas.move(shape_id, 0,10)
        window.after(50, gravity)
gravity()
window.mainloop()
