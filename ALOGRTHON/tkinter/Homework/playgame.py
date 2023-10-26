import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
# ------------- Constants ---------------------
SCREEN_WIDTH = 1536
SCREEN_HEIGHT = 700
GRAVITY_FORCE = 9
JUMP_FORCE = 25
SPEED = 7
TIMED_LOOP = 5

# ------------- Variables ---------------------
keyPressed = []
# ------------- Window ------------------------
window = tk.Tk()
window.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
window.title("Movement")
# window.attributes("-fullscreen", True)
# window.iconbitmap('c:gui/codemy.ico')

# ------------- bg ---------------------
# bg = PhotoImage(file="bg_image.jpg")
# my_label = Label(window, image = bg)
# my_label.place(x = 0, y = 0,relwidth=1, relheight=1)
frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

# ------------- Game --------------------------
player_img = PhotoImage(file="player.png")
img_file1 = Image.open("stair.jpg")
img_resize1 = img_file1.resize((200,40))
img1  = ImageTk.PhotoImage(img_resize1)
canvas.create_image(100,600, image = img1, tag = "PLATFORM")
canvas.create_image(300,500, image = img1, tag = "PLATFORM")
canvas.create_image(1200,400, image = img1, tag = "PLATFORM")
canvas.create_image(1000,300, image = img1, tag = "PLATFORM")
canvas.create_image(500,300, image = img1, tag = "PLATFORM")
canvas.create_image(700,600, image = img1, tag = "PLATFORM")
canvas.create_image(800,400, image = img1, tag = "PLATFORM")

# img_file_botton = Image.open("stair.jpg")
# img_resize_botton = img_file_botton.resize((200,40))
# img_botton  = ImageTk.PhotoImage(img_resize_botton)
# canvas.create_image(1500,650, image = img_botton, tag = "PLATFORM",)

canvas.create_rectangle(0,690,SCREEN_WIDTH,SCREEN_HEIGHT, tags="PLATFORM", fill='green')

# player = canvas.create_rectangle(100, 150, 150, 200, fill="red", outline="red")
player = canvas.create_image(100,150, image = player_img,)
# ------------- Functions ---------------------
# Check if the player can move by projecting the movement with dx and dy
# If checkGround is True, check if the player is on the ground by projecting the movement with the last coordinate
# Instead of getting the platform list with canvas.find_withtag("PLATFORM"), we could have used a global list
# Return True if the player can move (i.e. is not near any wall), False otherwise
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("PLATFORM")

    if coord[0] + dx < 0 or coord[1] + dx > SCREEN_WIDTH:
        return False

    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1] - 50) + player_img.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+ player_img.width() + dx, (coord[1] - 50) + player_img.height())

    for platform in platforms:
        if platform in overlap:
            return False

    return True

# -----------------------Jump by moving the player up by force pixels-----------------------------
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)


# ----------------start_move------------------------
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()


#---------------Move_object----------------------------------
def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player, x, 0)
        window.after(TIMED_LOOP, move)


#--------check_player_move---------------------
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)


#--------------stop_move and remove key------------------------
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)


gravity()

window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)
window.mainloop()