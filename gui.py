import tkinter as tk
from PIL import ImageTk, Image

HEIGHT = 500
WIDTH = 600

def test(entry):
    print("Button clicked", entry)

root = tk.Tk()
root.title("Mandelschmandel")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open("image.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#2b6e5e", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg="white", bd=5)
entry.place(relx=0, rely=0, relwidth=0.6, relheight=1)

button = tk.Button(frame, text="Get Weather", bg="#417cab", fg="white", activebackground="#2b6e5e", command=lambda: test(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#2b6e5e", bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text="Text label", bg="white")
label.place(relwidth=1, relheight=1)

root.mainloop()
