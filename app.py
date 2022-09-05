from tkinter import (Tk, Label, Entry, Frame,
                     Button, BOTTOM, TOP, RIGHT, LEFT, Y,
                     Menu, SUNKEN, W, X, END, Listbox, Scrollbar)
from modules.biudzetas import Biudzetas

biudzetas1 = Biudzetas()


def renew():
    entry1.delete(0, "end")
    update_entry.delete(0, "end")
    box.delete(0, "end")
    box.insert(END, *biudzetas1.zurnalas)
    balance['text'] = f"Balansas: {biudzetas1.balansas()}"


def add_income():
    suma = float(entry1.get())
    biudzetas1.prideti_pajamas(suma)
    renew()


def add_expense():
    suma = float(entry2.get())
    biudzetas1.prideti_islaidas(suma)
    renew()

def delete_item():
    biudzetas1.zurnalas.pop(box.curselection()[0])
    biudzetas1.irasyti_zurnala()
    renew()

def update_item():
    biudzetas1.zurnalas[box.curselection()[0]].suma = float(update_entry.get())
    biudzetas1.irasyti_zurnala()
    renew()


window = Tk()
window.geometry("300x400")
window.title("Biudžetas")
frame1 = Frame(window)
label1 = Label(frame1, text="Pajamos:")
entry1 = Entry(frame1)
button1 = Button(frame1, text="Įvesti", command=add_income)

frame2 = Frame(window)
entry2 = Entry(frame2)
label2 = Label(frame2, text="Išlaidos:")
button2 = Button(frame2, text="Įvesti", command=add_expense)

frame3 = Frame(window)
balance = Label(frame3, text=biudzetas1.balansas())
scrollbar = Scrollbar(frame3)
box = Listbox(frame3, yscrollcommand=scrollbar.set)
scrollbar.config(command=box.yview())
label4 = Label(frame3, text="Įrašai: ")
box.insert(END, *biudzetas1.zurnalas)
delete_button = Button(frame3, text="Ištrinti", command=delete_item)
update_button = Button(frame3, text="Redaguoti", command=update_item)
update_entry = Entry(frame3)

frame1.pack()
label1.pack()
entry1.pack()
button1.pack()

frame2.pack()
label2.pack()
entry2.pack()
button2.pack()
frame3.pack()
balance.pack()
label4.pack()
box.pack(side=LEFT)
scrollbar.pack(side=LEFT, fill=Y)
delete_button.pack()
update_entry.pack()
update_button.pack()
window.mainloop()
