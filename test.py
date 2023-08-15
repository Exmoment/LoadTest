from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import functions

#    messagebox.showinfo('Тест1', "Тест")

def createGETandPOST():
    GET_POST = functions.choiceType('GET and POST')
    GET_POST.iterrationGET = int(iterTest_entry.get())
    GET_POST.iterrationPOST = int(iterTest_entry.get())
    GET_POST.POSTandGET()
    print(iterTest_entry.get())

def createPOST():

    if  ((iterTest_entry.get().isdigit()) > 0) and (int(iterTest_entry.get()) > 0):
        POST = functions.choiceType('POST')
        POST.iterrationPOST = int(iterTest_entry.get())
        POST.POST()
        print(iterTest_entry.get())

    else:
        messagebox.showinfo('Error', 'В поле итераций должно быть введено положительно число')

def clicked():
    print(choice_tupe.get())
    typeLoad = choice_tupe.get()
    global iterTest_entry

    if ('GET and POST' in typeLoad):
        tests_iter = Label(window, text = "Введите количество итераций тестов:", font = ("Arial", 12))
        tests_iter.pack(pady = [5,0])
        entry_path = Entry(window, width = 25)
        entry_path.pack(pady = [5, 5])
        window.geometry('600x450')

    elif ('POST' in typeLoad):
        POSTreq = Frame(relief = FLAT)
        POSTreq.pack(pady = [5, 5])
        iterTest = Label(master = POSTreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 0, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iterTest_entry = Entry(master = POSTreq, width = 25)
        iterTest_entry.grid(column = 1, row = 0, padx = [5, 5], pady = [5, 5])
        iterTest_btn = Button(master = POSTreq, text = 'ОК', command = createPOST)
        iterTest_btn.grid(column = 2, row = 0, padx = [5, 5], pady = [5, 5])
        bodyTest = Label(master = POSTreq, text = "Путь к файлу конфигурации:", font = ("Arial", 12))
        bodyTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        bodyTest_path = Entry(master = POSTreq, width = 25)
        bodyTest_path.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])
        ammoTest = Label(master = POSTreq, text = "Путь к файлу запросов:", font = ("Arial", 12))
        ammoTest.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        ammoTest_path = Entry(master = POSTreq, width = 25)
        ammoTest_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])
        print('Введите количество итераций сценариев POST запросов:')
        window.geometry('650x450')

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

    else:
        messagebox.showinfo('Ошибка ввода', 'Вы не выбрали тип запросов, попробуйте еще раз')


window = Tk()
window.title("Тест")
window.geometry('400x150')

type_req = Label(window, text = "Выберите тип запросов:", font = ("Arial", 12))
type_req.pack(pady = [5, 5])

tupeTest = ("GET", "POST", "GET and POST")
btn1 = Button(window, text = 'ОК', command = clicked).pack(side = BOTTOM, fill = X, padx = 5, pady = 5)
choice_tupe = Combobox(window, values = tupeTest, width = 25)
choice_tupe.current()
choice_tupe.pack(pady = [5, 5])


window.mainloop()