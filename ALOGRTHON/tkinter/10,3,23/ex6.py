import tkinter as tk
window = tk.Tk()
window.title("draw shape")
window.geometry("1024x600")
window.resizable(0,0)
frame = tk.Frame(window, width=1024, height=600)
frame.pack()
canvas = tk.Canvas(frame, width=1024, height=600, bg='white')
canvas.pack()
canvas.create_text(500,130,text='Play Game', font=('bold',50))
canvas.create_oval(10,560,45,590,fill='black')

canvas.create_rectangle(100,575,300,590,fill='black')
canvas.create_rectangle(200,535,400,550,fill='black')
canvas.create_rectangle(300,505,500,520,fill='black')

canvas.create_rectangle(580,420,600,600,fill='gray')
canvas.create_rectangle(535,450,555,600,fill='gray')

canvas.create_rectangle(10,400,250,420,fill='black')
canvas.create_rectangle(300,400,500,420,fill='black')
canvas.create_rectangle(80,385,300,400,fill='gray')
canvas.create_oval(10,370,45,400,fill='green')


canvas.create_rectangle(185,325,350,340,fill='black')
canvas.create_rectangle(390,325,550,340,fill='black')
canvas.create_rectangle(600,325,750,340,fill='black')
canvas.create_rectangle(735,205,750,340,fill='black')
canvas.create_oval(700,295,735,325,fill='green')
window.mainloop()
