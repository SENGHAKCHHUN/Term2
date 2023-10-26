# from tkinter import *
# from tkinter import ttk

# splash_window =Tk()
# time = 10
# splash_window.title("Splash Screen")
# splash_window.overrideredirect(True)
# splash_window.geometry("600x230")
# splash_window.config(bg="black")
# window_label = Label(splash_window, text="Jump to heart", font=("Robus",60, "bold"), fg="red", bg="black")
# window_label.pack(pady=30)

# window_label2 = Label(splash_window, text="", font=("bold", 20), fg="green", bg="black")
# window_label2.pack()

# progressbar = ttk.Progressbar()
# progress = ttk.Style()
# progress.theme_use('alt')

# progressbar.place(x=100, y=150, width=400, height=10)
# progressbar.step(time)
# progressbar.start()

# def main():
#     splash_window.destroy()
#     window = Tk()
#     window.geometry("600x600")
#     window.title("Jump to heart")
#     # frame
#     frame = Frame(window)
#     frame.pack()

#     # canvas
#     canvas = Canvas(frame, width=500, height=500, bg="white")
#     canvas.pack(pady=10)

#     window.mainloop()
    
# splash_window.after(5000, main)
# splash_window.mainloop()




import tkinter as tk
from PIL import Image, ImageTk
from pygame import mixer
import time

# score 
score = 0

window = tk.Tk()
window.geometry("800x500")
window.title("Move Shape")
window.resizable(False, False)

# frame 
frame = tk.Frame(window)
frame.pack()

# canvas
canvas = tk.Canvas(frame, width=700, height=400, bg="white")
canvas.pack(pady=20)

img_file = Image.open("actor.png")
img_size = img_file.resize((50, 70))
ball = ImageTk.PhotoImage(img_size)
ball_id = canvas.create_image(30, 30, image=ball)

banana_file = Image.open("banana.jpg")
banana_size = banana_file.resize((50, 50))
banana = ImageTk.PhotoImage(banana_size)

skin_file = Image.open("banan-skin.jpg")
skin_size = skin_file.resize((50, 50))
skin = ImageTk.PhotoImage(skin_size)
canvas.create_image(70, 70,  image=banana, tags="banana")
canvas.create_image(300, 300, image=banana, tags="banana")
canvas.create_image(400, 70, image=banana, tags="banana")
canvas.create_image(70, 200,  image=banana, tags="banana")
canvas.create_image(500, 70, image=banana, tags="banana")
canvas.create_image(30, 300,  image=banana, tags="banana")

score_id = canvas.create_text(600, 15, text="Score:", font=("bold", 15))

chili_file = Image.open("chili.jpg")
chili_size = chili_file.resize((50, 50))
chili = ImageTk.PhotoImage(chili_size)

newActor_file = Image.open("actor-2.png")
newActor_size = newActor_file.resize((60, 60))
newActor = ImageTk.PhotoImage(newActor_size)

canvas.create_image(100, 300, image=chili, tags="chili")
canvas.create_image(200, 350, image=chili, tags="chili")
canvas.create_image(150, 200, image=chili, tags="chili")
def eat_banana():
    coord = canvas.coords(ball_id)
    bananas = canvas.find_withtag("banana")
    print(bananas)
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + ball.width(),coord[1] + ball.height())
    print(overlap)
    for bn in bananas:
        if bn in overlap:
            return bn
    return 0
def eat_chili():
    coord = canvas.coords(ball_id)
    chilis = canvas.find_withtag("chili")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + ball.width(),coord[1] + ball.height())
    for ch in chilis:
        if ch in overlap:
            return ch
    return 0
def is_border_left():
    return canvas.coords(ball_id)[0] < 30
def is_border_right():
    return canvas.coords(ball_id)[0] > 670
def is_border_top():
    return canvas.coords(ball_id)[1] < 30
def is_border_bottom():
    return canvas.coords(ball_id)[1] > 370
# def playSound():
#     mixer.init() #Initialzing pyamge mixer
#     mixer.music.load('sound-3.mp3') #Loading Music File
#     mixer.music.play() #Playing Music with Pygame
#     time.sleep(1)
#     mixer.music.stop()
def move_shape(event):
    if event.keysym == "Left" and not is_border_left():
        canvas.move(ball_id, -5, 0)
    elif event.keysym == "Right" and not is_border_right():
        canvas.move(ball_id, 5, 0)
    elif event.keysym == "Up" and not is_border_top():
        canvas.move(ball_id, 0, -5)
    elif event.keysym == "Down" and not is_border_bottom():
        canvas.move(ball_id, 0, 5)
    banana_id =  eat_banana()
    chili_id =  eat_chili()
    
    if banana_id > 0:
        coord = canvas.coords(banana_id)
        canvas.delete(banana_id)
        canvas.create_image(coord[0], coord[1], image=skin)
        # playSound()
        global score
        score += 1 
        update_score()
    if chili_id > 0:
        coord = canvas.coords(chili_id)
        canvas.delete(chili_id)
        canvas.itemconfigure(ball_id, image=newActor)
        # playSound()
        score -= 1 
        update_score()
def update_score():
    canvas.itemconfigure(score_id, text="Score: " + str(score))
window.bind("<Key>", move_shape)
window.mainloop()