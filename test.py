from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import functions


def clicked():
    text_1 = Label(window, text = "Введите путь к файлу конфигурации:", font = ("Arial", 12))
    text_1.pack(pady = [10, 0])
    entry_path = Entry(window, width = 10)
    entry_path.pack(pady = 10)
    print(chose_tupe.get())
    typeLoad = chose_tupe.get()

    if ('GET and POST' in typeLoad) or ('get and post' in typeLoad) or ('POST and GET' in typeLoad) or ('post and get' in typeLoad):
        functions.POSTandGET()

    elif ('POST' in typeLoad) or ('post' in typeLoad):
        functions.POST()

    elif ('GET' in typeLoad) or ('get' in typeLoad):
        functions.GET()

    else:
        print('Invalid value')


#    messagebox.showinfo('Тест1', "Тест")


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


window.mainloop()