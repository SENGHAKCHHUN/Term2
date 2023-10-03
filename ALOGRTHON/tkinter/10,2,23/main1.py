# import tkinter as tk
# import random
# window = tk.Tk()

# window.title("my game window")

# window.configure(bg="black")

# window.resizable(0,0)

# window.geometry("400x300")

# frame = tk.Frame(window, bg='orange', width=400, height=300)

# frame.pack()

# color = ['red', 'orange']
# # color = random.choice(arr)
# canvas = tk.Canvas(frame, width=300, height=200)

# circle_id = canvas.create_oval(10, 10, 100, 100, fill='red')




# rect_id = canvas.create_rectangle(110, 10, 200, 100, fill='orange')
# canvas.itemconfig(circle_id, fill='yellow')
# canvas.itemconfig(rect_id, fill= 'white')
# print('cirele Id' + str(circle_id))
# print('rectagle Id' + str(rect_id))
# canvas.pack()
# def changeColor():
    # color_circle = random.choice(arr)
    # color_rect = random.choice(arr)
    # canvas.itemconfig(circle_id, fill = random.choice(color))
    # canvas.itemconfig(rect_id, fill = random.choice(color))
# arr = ['blue', 'yellow', 'purple', 'orange']
# def changeColor():
#     canvas.itemconfig(circle_id, fill="red")
# btn = tk.Button(frame, text='red', command=changeColor)
# btn.pack()
# def changeColor():
#     canvas.itemconfig(circle_id, fill="orange")
# btn = tk.Button(frame, text='orange', command=changeColor)
# btn.pack()
# window.mainloop()



# import tkinter as tk
# import random

# window = tk.Tk()
# window.title("new window")
# frame = tk.Frame(window, width=400, height=300)
# frame.pack()
# window.geometry("400x300")
# canvas = tk.Canvas(frame, width=300, height=200, bg='green')
# canvas.pack()
# rect_id = canvas.create_rectangle(110, 10, 200, 100, fill='orange')
# def click():

# btn = tk.Button(frame, text='-1', command=click)
# btn.pack()
# btn = tk.Button(frame,text='+1', command=click)
# btn.pack()
# window.mainloop()



import tkinter as tk
window = tk.Tk()
window.geometry("500x500")
window.title("start learning")
frame = tk.Frame(window, width=500, height=500)
frame.pack()
canvas = tk.Canvas(frame,bg='green')
canvas.pack()
# for i in range(1, 10):
#     for j in range(1, 10):
#         canvas.create_rectangle(10 + i * 100 , 10+j *100, 100+i * 100 , 100 +j * 100, fill='pink')
# window.mainloop()


total = 0
canvas.create_rectangle(10, 10, 100,100, fill='red')
result = canvas.create_text(55, 60, text="0", fill="black", font=("bold", 40))
canvas.itemconfig(result, text= total)
def increment(even):
    global total
    total +=1
    canvas.itemconfig(result, text = total)
# btnIncrement = tk.Button(frame, text='Increment', command=increment)
# btnIncrement.pack()

def decrement(even):
    global total
    total -=1
    canvas.itemconfig(result, text = total)
# btnDecrement = tk.Button(frame, text='Decrement', command=increment)
# btnDecrement.pack()

window.bind('<Up>', increment)
window.bind('<Down>', decrement)
window.mainloop()

