import tkinter as tk
import time
window = tk.Tk()
window.title("Image viewer")
window.geometry("600x400")
window.resizable(False,False)
frame = tk.Frame(window, width=600, height=400)
frame.pack()
canvas = tk.Canvas(frame, width=600, height=400)
canvas.pack()
time_id = canvas.create_text(300, 150, text='', font=('Arial',70), fill='orange')
def clock():
    hour = time.strftime("%H:%M:%S")
    print(hour)
    canvas.itemconfig(time_id, text=hour)
def updateTime():
    clock()
    window.after(1000, updateTime)
window.after(1000, updateTime)
window.mainloop()


# import tkinter as tk

# class TimerApp:
#     def __init__(self, master):
#         self.master = master
#         self.time = 0
#         self.is_running = False

#         self.timer_label = tk.Label(master, text="00:00:00", font=("Arial", 24))
#         self.timer_label.pack(pady=10)

#         self.start_button = tk.Button(master, text="Start", command=self.start_timer)
#         self.start_button.pack(side=tk.LEFT, padx=5)

#         self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
#         self.stop_button.pack(side=tk.LEFT, padx=5)

#         self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
#         self.reset_button.pack(side=tk.LEFT, padx=5)

#     def start_timer(self):
#         if not self.is_running:
#             self.is_running = True
#             self.update_timer()

#     def stop_timer(self):
#         if self.is_running:
#             self.is_running = False

#     def reset_timer(self):
#         self.time = 0
#         self.timer_label.config(text="00:00:00")

#     def update_timer(self):
#         if self.is_running:
#             self.time += 1
#             hours = self.time // 3600
#             minutes = (self.time % 3600) // 60
#             seconds = (self.time % 60)

#             time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
#             self.timer_label.config(text=time_string)

#         self.master.after(1000, self.update_timer)

# root = tk.Tk()
# app = TimerApp(root)
# root.mainloop()

