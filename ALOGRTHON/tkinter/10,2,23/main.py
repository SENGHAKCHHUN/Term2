import tkinter as tk
window = tk.Tk()
window.title("My game title")
window.geometry("600x500")
frame = tk.Frame(window, bg='orange')
frame.pack()
canvas = tk.Canvas(frame, bg='white')
canvas.pack()
total = 0
canvas.create_rectangle(10,10,100,100, fill='green')
number = canvas.create_text(55, 60, text='0', fill='white', font=('bold', 60))
def Increase():
    global total
    total = total + 1
    canvas.itemconfig(number, text = total)
def Decrease():
    global total 
    total = total - 1
    canvas.itemconfig(number, text = total)
btn = tk.Button(window, text='Increase', command=Increase, width='10',height='1')
btn.pack()
btn = tk.Button(window, text='Decrease', command=Decrease)
btn.pack()
window.mainloop()
