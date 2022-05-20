from tkinter import *

window = Tk("Miles to Kilometer converter")
window.minsize(width=300, height=50)
window.config(pady=20, padx=50)

# Entry
input = Entry()
input.grid(row=0, column=1)

# label
label = Label()
label.config(text="Miles", font=("Arial", 12, "bold"), padx=15)
label.grid(row=0, column=2)

window.mainloop()
