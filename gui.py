import tkinter as tk

HEIGHT = 400
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#2b6e5e", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg="white", bd=5)
entry.place(relx=0, rely=0, relwidth=0.6, relheight=1)

button = tk.Button(frame, text="Test button", bg="#417cab", fg="white", activebackground="#2b6e5e")
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# label = tk.Label(frame, text="This is a label", bg="#6e6a2b",)
# label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)


#

root.mainloop()
