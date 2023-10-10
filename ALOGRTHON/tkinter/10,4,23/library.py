# import tkinter as tk
# from PIL import Image, ImageTk
# window = tk.Tk()
# window.title("My game title")
# window.geometry("600x500")

# frame = tk.Frame(window, width=600, height=500)
# frame.pack()
# canvas = tk.Canvas(frame, bg='white')
# canvas.pack()
# getImageFile = Image.open('wall.jpg')
# getImageFile_size = getImageFile.resize((100,100))
# img = ImageTk.PhotoImage(getImageFile_size)
# canvas.img(100,100, image = img)
# lable = tk.Label(frame, image = img)
# lable.pack()
# window.mainloop()


import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Polygon')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)


# create a polygon
points = (
    (100, 300),
    (200, 200),
    (300, 300),
)
canvas.create_polygon(*points, fill='blue')

root.mainloop()

