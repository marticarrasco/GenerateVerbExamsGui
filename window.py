from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("493x577")
window.configure(bg = "#dcdcdc")
canvas = Canvas(
    window,
    bg = "#dcdcdc",
    height = 577,
    width = 493,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    248.5, 204.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    248.5, 404.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#89cff0",
    highlightthickness = 0)

entry0.place(
    x = 57.0, y = 383,
    width = 383.0,
    height = 40)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 138, y = 459,
    width = 220,
    height = 73)

canvas.create_text(
    316.0, 303.0,
    text = "output path",
    fill = "#000000",
    font = ("Rambla-Regular", int(18.0)))

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 45, y = 278,
    width = 132,
    height = 53)

canvas.create_text(
    316.0, 204.0,
    text = "input path",
    fill = "#000000",
    font = ("Rambla-Regular", int(18.0)))

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 45, y = 179,
    width = 132,
    height = 53)

window.resizable(False, False)
window.mainloop()
