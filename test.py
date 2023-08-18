from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import functions

#    messagebox.showinfo('Тест1', "Тест")

def createPOST():
    if len(bodyTestPOST_path.get()) > 0 and len(ammoTest_path.get()) > 0:

        if  ((iterTestPOST_entry.get().isdigit()) > 0) and (int(iterTestPOST_entry.get()) > 0):
            POST = functions.choiceType('POST')
            POST.iterrationPOST = int(iterTestPOST_entry.get())
            POST.pathBodyPOST = bodyTestPOST_path.get()
            POST.pathAmmo = ammoTest_path.get()
            POST.POST()

        else:
            messagebox.showinfo('Error', 'Поле итераций POST запросов должно содержать натуральное число')

    else:
        messagebox.showinfo('Error', 'Все поля POST запросов должны быть заполнены')


def createGET():
    if len(bodyTestGET_path.get()) > 0:

        if  ((iterTestGET_entry.get().isdigit()) > 0) and (int(iterTestGET_entry.get()) > 0):
            GET = functions.choiceType('GET')
            GET.iterrationGET = int(iterTestGET_entry.get())
            GET.pathBodyGET = bodyTestGET_path.get()
            GET.GET()

        else:
            messagebox.showinfo('Error', 'Поле итераций GET запросов должно содержать натуральное число')

    else:
        messagebox.showinfo('Error', 'Все поля GET запросов должны быть заполнены')


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
    global bodyTestPOST_path
    global bodyTestGET_path
    global POSTreq
    global GETreq

    if ('GET and POST' in typeLoad):
        start.destroy()
        POSTreq = Frame(relief = FLAT)
        POSTreq.pack(padx = [5, 5])
        GETreq = Frame(relief = FLAT)
        GETreq.pack(padx = [5, 5])
        nameTestPOST = Label(master = POSTreq, text = "POST", font = ("Arial", 16), foreground = 'red')
        nameTestPOST.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 5])
        iterTest = Label(master = POSTreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iterTestPOST_entry = Entry(master = POSTreq, width = 25)
        iterTestPOST_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])
        bodyTestPOST = Label(master = POSTreq, text = "Путь или имя файла конфигурации:", font = ("Arial", 12))
        bodyTestPOST.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        bodyTestPOST_path = Entry(master = POSTreq, width = 25)
        bodyTestPOST_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])
        ammoTest = Label(master = POSTreq, text = "Путь или имя файла запросов:", font = ("Arial", 12))
        ammoTest.grid(column = 0, row = 3, padx = [5, 5], pady = [5, 5], sticky = 'e')
        ammoTest_path = Entry(master = POSTreq, width = 25)
        ammoTest_path.grid(column = 1, row = 3, padx = [5, 5], pady = [5, 5])
        nameTestGET = Label(master = GETreq, text = "GET", font = ("Arial", 16), foreground = 'red')
        nameTestGET.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 5])
        iterTest = Label(master = GETreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iterTestGET_entry = Entry(master = GETreq, width = 25)
        iterTestGET_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])
        bodyTestGET = Label(master = GETreq, text = "Путь или имя файла конфигурации:", font = ("Arial", 12))
        bodyTestGET.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        bodyTestGET_path = Entry(master = GETreq, width = 25)
        bodyTestGET_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])
        iterTest_btn = Button(master = GETreq, text = 'Принять', command = lambda:[createGET(), createPOST()])
        iterTest_btn.grid(column = 1, row = 3, padx = 5, pady = 5)
        back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[destroyGETreq(), destroyPOSTreq(), wiget_dontgenerate()])
        back_btn.grid(column = 0, row = 3, padx = 5, pady = 5)
        print('Ожидание ввода параметров')
        window.geometry('550x300')

    elif ('POST' in typeLoad):
        start.destroy()
        POSTreq = Frame(relief = FLAT)
        POSTreq.pack(pady = [5, 5])
        nameTestPOST = Label(master = POSTreq, text = "POST", font = ("Arial", 16), foreground = 'red')
        nameTestPOST.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 5])
        iterTest = Label(master = POSTreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iterTestPOST_entry = Entry(master = POSTreq, width = 25)
        iterTestPOST_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])
        bodyTestPOST = Label(master = POSTreq, text = "Путь или имя файла конфигурации:", font = ("Arial", 12))
        bodyTestPOST.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        bodyTestPOST_path = Entry(master = POSTreq, width = 25)
        bodyTestPOST_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])
        ammoTest = Label(master = POSTreq, text = "Путь или имя файла запросов:", font = ("Arial", 12))
        ammoTest.grid(column = 0, row = 3, padx = [5, 5], pady = [5, 5], sticky = 'e')
        ammoTest_path = Entry(master = POSTreq, width = 25)
        ammoTest_path.grid(column = 1, row = 3, padx = [5, 5], pady = [5, 5])
        iterTest_btn = Button(master = POSTreq, text = 'Принять', command = createPOST)
        iterTest_btn.grid(column = 1, row = 4, padx = 5, pady = 5)
        back_btn = Button(master = POSTreq, text = 'Вернуться к выбору запросов', command = lambda:[destroyPOSTreq(), wiget_dontgenerate()])
        back_btn.grid(column = 0, row = 4, padx = 5, pady = 5)
        print('Ожидание ввода параметров')
        window.geometry('550x200')

    elif ('GET' in typeLoad):
        start.destroy()
        GETreq = Frame(relief = FLAT)
        GETreq.pack(pady = [5, 5])
        nameTestGET = Label(master = GETreq, text = "GET", font = ("Arial", 16), foreground = 'red')
        nameTestGET.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 5])
        iterTest = Label(master = GETreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iterTestGET_entry = Entry(master = GETreq, width = 25)
        iterTestGET_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])
        bodyTestGET = Label(master = GETreq, text = "Путь или имя файла конфигурации:", font = ("Arial", 12))
        bodyTestGET.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        bodyTestGET_path = Entry(master = GETreq, width = 25)
        bodyTestGET_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])
        iterTest_btn = Button(master = GETreq, text = 'Принять', command = createGET)
        iterTest_btn.grid(column = 1, row = 3, padx = 5, pady = 5)
        back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[destroyGETreq(), wiget_dontgenerate()])
        back_btn.grid(column = 0, row = 3, padx = 5, pady = 5)
        print('Ожидание ввода параметров')
        window.geometry('550x170')

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