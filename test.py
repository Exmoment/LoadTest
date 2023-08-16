from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import functions

#    messagebox.showinfo('Тест1', "Тест")

def createGETandPOST():
    if  ((iterTest_entry.get().isdigit()) > 0) and (int(iterTest_entry.get()) > 0):
        GET_POST = functions.choiceType('GET and POST')
        GET_POST.iterrationGET = int(iterTest_entry.get())
        GET_POST.iterrationPOST = int(iterTest_entry.get())
        GET_POST.pathBody = bodyTest_path.get()
        GET_POST.pathAmmo = ammoTest_path.get()
        GET_POST.POSTandGET()


def createPOST():
    if  ((iterTestPOST_entry.get().isdigit()) > 0) and (int(iterTestPOST_entry.get()) > 0):
        POST = functions.choiceType('POST')
        POST.iterrationPOST = int(iterTestPOST_entry.get())
        POST.pathBody = bodyTest_path.get()
        POST.pathAmmo = ammoTest_path.get()
        POST.POST()

    else:
        messagebox.showinfo('Error', 'В поле итераций должно быть введено значение больше нуля')


def createGET():
    if  ((iterTestGET_entry.get().isdigit()) > 0) and (int(iterTestGET_entry.get()) > 0):
        GET = functions.choiceType('GET')
        GET.iterrationGET = int(iterTestGET_entry.get())
        GET.pathBody = bodyTest_path.get()
        GET.GET()
    else:
        messagebox.showinfo('Error', 'В поле итераций должно быть введено значение больше нуля')


def destroyPOSTreq():
    POSTreq.destroy()


def destroyGETreq():
    GETreq.destroy()


def clicked():
    print(choice_tupe.get())
    typeLoad = choice_tupe.get()
    global iterTestPOST_entry
    global iterTestGET_entry
    global ammoTest_path
    global bodyTest_path
    global POSTreq
    global GETreq

    if ('GET and POST' in typeLoad):
        tests_iter = Label(window, text = "Введите количество итераций тестов:", font = ("Arial", 12))
        tests_iter.pack(pady = [5,0])
        entry_path = Entry(window, width = 25)
        entry_path.pack(pady = [5, 5])
        window.geometry('600x450')

    elif ('POST' in typeLoad):
        start.destroy()
        POSTreq = Frame(relief = FLAT)
        POSTreq.pack(pady = [5, 5])
        iterTest = Label(master = POSTreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 0, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iterTestPOST_entry = Entry(master = POSTreq, width = 25)
        iterTestPOST_entry.grid(column = 1, row = 0, padx = [5, 5], pady = [5, 5])
        bodyTest = Label(master = POSTreq, text = "Путь или имя файла конфигурации:", font = ("Arial", 12))
        bodyTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        bodyTest_path = Entry(master = POSTreq, width = 25)
        bodyTest_path.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])
        ammoTest = Label(master = POSTreq, text = "Путь или имя файла запросов:", font = ("Arial", 12))
        ammoTest.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        ammoTest_path = Entry(master = POSTreq, width = 25)
        ammoTest_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])
        iterTest_btn = Button(master = POSTreq, text = 'Принять', command = createPOST)
        iterTest_btn.grid(column = 1, row = 3, padx = 5, pady = 5)
        back_btn = Button(master = POSTreq, text = 'Вернуться к выбору запросов', command = lambda:[destroyPOSTreq(), wiget_dontgenerate()])
        back_btn.grid(column = 0, row = 3, padx = 5, pady = 5)
        print('Ожидание ввода параметров')
        window.geometry('550x150')

    elif ('GET' in typeLoad):
        start.destroy()
        GETreq = Frame(relief = FLAT)
        GETreq.pack(pady = [5, 5])
        iterTest = Label(master = GETreq, text = "Введите количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 0, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iterTestGET_entry = Entry(master = GETreq, width = 25)
        iterTestGET_entry.grid(column = 1, row = 0, padx = [5, 5], pady = [5, 5])
        tests_config = Label(master = GETreq, text = "Путь или имя файла конфигурации:", font = ("Arial", 12))
        tests_config.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        tests_config_path = Entry(master = GETreq, width = 25)
        tests_config_path.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])
        iterTest_btn = Button(master = GETreq, text = 'Принять', command = createGET)
        iterTest_btn.grid(column = 1, row = 2, padx = 5, pady = 5)
        back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[destroyGETreq(), wiget_dontgenerate()])
        back_btn.grid(column = 0, row = 2, padx = 5, pady = 5)
        print('Ожидание ввода параметров')
        window.geometry('550x120')

    else:
        messagebox.showinfo('Ошибка ввода', 'Вы не выбрали тип запросов, попробуйте еще раз')

def wiget_dontgenerate():
        global choice_tupe
        global start

        start = Frame(window, relief = FLAT, padding = [8, 10])
        start.pack(padx = 10, pady = 10)
        type_req = Label(master = start, text = "Выберите тип запросов:", font = ("Arial", 12))
        type_req.pack(pady = [5, 5])
        tupeTest = ("GET", "POST", "GET and POST")
        choice_btn = Button(master = start, text = 'Выбрать', command = clicked)
        choice_btn.pack(side = BOTTOM, fill = X, padx = 5, pady = 5)
        choice_tupe = Combobox(master = start, values = tupeTest, width = 25)
        choice_tupe.current()
        choice_tupe.pack(pady = [5, 5])
        window.geometry('400x150')


window = Tk()
window.title("Тестовое окно")
window.geometry('400x150')
window.resizable(False, False)
wiget_dontgenerate()


window.mainloop()