import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
from tkinter import messagebox as nsg

def on_clonsing():
    if nsg.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_clonsing)
window.title("Image Viewer")
window.geometry("600x500")

frame = tk.Frame(window, width=600, height=400)
frame.pack()

canvas = tk.Canvas(frame, width=500, height=400, bg="white")
canvas.pack(pady=20)

# Image 1
file_1 = Image.open('1.png')
file_1_size = file_1.resize((100, 100))
img_1 = ImageTk.PhotoImage(file_1_size)
img_id = canvas.create_image(50, 50, image=img_1, )

def moveLeft(event):
    x = -10
    y = 0
    canvas.move(img_id, x, y)
def moveRight(event):
    x = 10
    y = 0
    canvas.move(img_id, x, y)

window.bind("<Left>", moveLeft)
window.bind("<Right>", moveRight)

file_2 = Image.open('2.png')
file_2_size = file_2.resize((100,150))
img_2 = ImageTk.PhotoImage(file_2_size)
canvas.create_image(140,80, image = img_2)

file_3 = Image.open('3.png')
file_3_resize = file_3.resize((100,170))
img_3 = ImageTk.PhotoImage(file_3_resize)
canvas.create_image(240,90, image = img_3)

file_4 = Image.open('4.png')
file_4_resize = file_4.resize((100,100))
img_4 = ImageTk.PhotoImage(file_4_resize)
canvas.create_image(350,70, image = img_4)

file_5 = Image.open('5.png')
file_5_resize = file_5.resize((100,100))
img_5 = ImageTk.PhotoImage(file_5_resize)
canvas.create_image(450, 70, image = img_5)


# Text
canvas.create_text(250, 200, text="Football Game", font=("Robus", 60, "bold"), fill="purple")


file_6 = Image.open('ucl.png')
file_6_resize = file_6.resize((50,50))
img_6 = ImageTk.PhotoImage(file_6_resize)
canvas.create_image(240, 260, image = img_6)


file_fb = Image.open('fb-b.png')
file_fb_resize = file_fb.resize((50,50))
img_fb = ImageTk.PhotoImage(file_fb_resize)
canvas.create_image( 70, 310, image = img_fb)

canvas.create_text(150, 310, text='Bayern Munich',font=("Arial", 10, "bold"), fill="purple" )
canvas.create_text(250, 310, text='VS .',font=("Arial", 25, "bold"), fill="purple" )
canvas.create_text(330, 310, text='Bacelona',font=("Arial", 10, "bold"), fill="purple" )

file_fc = Image.open('fc-b.png')
file_fc_resize = file_fc.resize((50,50))
img_fc = ImageTk.PhotoImage(file_fc_resize)
canvas.create_image(400,310, image = img_fc)
canvas.create_text(240,370, text='8   :   2',font=("Arial", 25, "bold"), fill="purple")
# window.resizable(0, 0)
window.mainloop()
