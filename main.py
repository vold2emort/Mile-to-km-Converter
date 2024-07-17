from tkinter import *

window = Tk()
window.minsize(width=150, height=150)
window.title("Miles to Kilometer Converter")
window.config(padx=100, pady=100)

def miles_to_km():
    mile = int(mile_input.get())
    km = mile * 1.609
    km_output.config(text=f"{km}")
    # print(f"{km:.2f}")
    # return km




mile_input = Entry(width=5)
mile_input.grid(column=1, row=0)
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)

km_output = Label(text=0)
km_output.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()