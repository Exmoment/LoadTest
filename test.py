from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


def clicked():
    print(chose_tupe.get())
    text.configure(text = "Введите путь к файлу конфигурации:")
    messagebox.showinfo('Тест1', "Тест")


window = Tk()
window.title("Тест")
window.geometry('400x250')

text = Label(window, text = "Выберите тип запросов:", font = ("Arial", 12))
text.pack(pady = [10, 0])

tupeTest = ("GET", "POST", "GET and POST")
btn1 = Button(window, text = 'ОК', command = clicked).pack(side = BOTTOM, fill = X, padx= 5, pady= 5)
chose_tupe = Combobox(window, values = tupeTest)
chose_tupe.current()
chose_tupe.pack(pady = 10)
#input_path = Label(window, text = "Введите путь к файлу конфигурации:", font = ("Arial", 12))
#input_path.pack()


window.mainloop()