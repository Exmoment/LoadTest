from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import functions
import check


def clicked():
    
    print(chose_tupe.get())
    typeLoad = chose_tupe.get()

    if ('GET and POST' in typeLoad):
        tests_iter = Label(window, text = "Введите количество итераций тестов:", font = ("Arial", 12))
        tests_iter.pack(pady = [5,0])
        entry_path = Entry(window, width = 25)
        entry_path.pack(pady = [5, 5])
        window.geometry('600x450')
        functions.POSTandGET()

    elif ('POST' in typeLoad):
        POSTreq = Frame(relief = FLAT)
        POSTreq.pack(pady = [5, 5])
        tests_iter = Label(master = POSTreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        tests_iter.grid(column = 0, row = 0, padx = [5, 5], pady = [5, 5], sticky = 'e')
        tests_iter_entry = Entry(master = POSTreq, width = 25)
        tests_iter_entry.grid(column = 1, row = 0, padx = [5, 5], pady = [5, 5])
        tests_config = Label(master = POSTreq, text = "Путь к файлу конфигурации:", font = ("Arial", 12))
        tests_config.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        tests_config_path = Entry(master = POSTreq, width = 25)
        tests_config_path.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])
        tests_ammo = Label(master = POSTreq, text = "Путь к файлу запросов:", font = ("Arial", 12))
        tests_ammo.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        tests_ammo_path = Entry(master = POSTreq, width = 25)
        tests_ammo_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])
        window.geometry('650x450')
        functions.POST()

    elif ('GET' in typeLoad):
        GETreq = Frame(relief = FLAT)
        GETreq.pack(pady = [5, 5])
        tests_iter = Label(master = GETreq, text = "Введите количество итераций тестов:", font = ("Arial", 12))
        tests_iter.grid(column = 0, row = 0, padx = [5, 5], pady = [5, 5], sticky = 'e')
        tests_iter_entry = Entry(master = GETreq, width = 25)
        tests_iter_entry.grid(column = 1, row = 0, padx = [5, 5], pady = [5, 5])
        tests_config = Label(master = GETreq, text = "Введите путь к файлу конфигурации:", font = ("Arial", 12))
        tests_config.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        tests_config_path = Entry(master = GETreq, width = 25)
        tests_config_path.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])
        window.geometry('650x450')
        functions.GET()

    else:
        error_text = Label(window, text = 'Invalid value, try again', font = ("Arial", 16))
        error_text.pack(side = BOTTOM, padx = 5, pady = 5)


#    messagebox.showinfo('Тест1', "Тест")


window = Tk()
window.title("Тест")
window.geometry('400x250')

type_req = Label(window, text = "Выберите тип запросов:", font = ("Arial", 12))
type_req.pack(pady = [10, 0])

tupeTest = ("GET", "POST", "GET and POST")
btn1 = Button(window, text = 'ОК', command = clicked).pack(side = BOTTOM, fill = X, padx = 5, pady = 5)
chose_tupe = Combobox(window, values = tupeTest, width = 25)
chose_tupe.current()
chose_tupe.pack(pady = [5, 5])


window.mainloop()