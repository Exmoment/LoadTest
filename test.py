from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import functions
import check


def clicked():
    
    print(chose_tupe.get())
    typeLoad = chose_tupe.get()

    if ('GET and POST' in typeLoad):
        text_1 = Label(window, text = "Введите количество итераций тестов:", font = ("Arial", 12))
        text_1.pack(pady = [5,0])
        entry_path = Entry(window, width = 25)
        entry_path.pack(pady = [5, 5])
        window.geometry('600x450')
        functions.POSTandGET()

    elif ('POST' in typeLoad):
        text_1 = Label(window, text = "Введите количество итераций тестов:", font = ("Arial", 12))
        text_1.pack(pady = [5,0])
        entry_path = Entry(window, width = 25)
        entry_path.pack(pady = [5, 5])
        window.geometry('600x450')
        functions.POST()

    elif ('GET' in typeLoad):
        text_1 = Label(window, text = "Введите количество итераций тестов:", font = ("Arial", 12))
        text_1.pack(pady = [5,0])
        entry_path = Entry(window, width = 25)
        entry_path.pack(pady = [5, 5])
        window.geometry('600x450')
        functions.GET()

    else:
        error_text = Label(window, text = 'Invalid value', font = ("Arial", 12))
        error_text.pack(side = BOTTOM, padx = 5, pady = 5)


#    messagebox.showinfo('Тест1', "Тест")


window = Tk()
window.title("Тест")
window.geometry('400x250')

text = Label(window, text = "Выберите тип запросов:", font = ("Arial", 12))
text.pack(pady = [10, 0])

tupeTest = ("GET", "POST", "GET and POST")
btn1 = Button(window, text = 'ОК', command = clicked).pack(side = BOTTOM, fill = X, padx = 5, pady = 5)
chose_tupe = Combobox(window, values = tupeTest, width = 25)
chose_tupe.current()
chose_tupe.pack(pady = [5, 5])


window.mainloop()