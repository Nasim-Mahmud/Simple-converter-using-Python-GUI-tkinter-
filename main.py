from tkinter import *

CONST = 1.60934

window = Tk()
window.title("Mile to Kilometer converter")
window.minsize(width=300, height=50)
window.config(pady=20, padx=50)

# Let's add new unit conversions also
# Asking label
ask = Label()
ask.config(text="Which conversion do you need to check?", font=("Arial", 12, "bold"), padx=15)
ask.grid(row=0, column=2)

# Entry
input = Entry()
input.config(width=8, font=("Arial", 12, "bold"))
input.grid(row=0, column=1)

# Label 01
label = Label()
label.config(text="Miles", font=("Arial", 12, "bold"), padx=15)
label.grid(row=0, column=2)

# Label 02
label = Label()
label.config(text="is equal to", font=("Arial", 12, "bold"))
label.grid(row=1, column=0)

# Label 03
label = Label()
label.config(text="kilometer", font=("Arial", 12, "bold"))
label.grid(row=1, column=2)


# result
def converter():
    n = input.get()
    res = int(n) * CONST
    result.config(text="{:.2f}".format(res))


result = Label()
result.config(font=("Arial", 12, "bold"))
result.grid(row=1, column=1)

# Button
button = Button(text="Calculate", command=converter, font=("Arial", 12, "bold"))
button.grid(row=2, column=1)

window.mainloop()
