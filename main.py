from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog as fd
import run_test

#    messagebox.showinfo('Тест1', "Тест")

def createPOST():
    if len(bodyTestPOST_path.get()) > 0 and len(ammoTest_path.get()) > 0:

        if  ((iterTestPOST_entry.get().isdigit()) > 0) and (int(iterTestPOST_entry.get()) > 0):
            POST = run_test.choiceType('POST')
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
            GET = run_test.choiceType('GET')
            GET.iterrationGET = int(iterTestGET_entry.get())
            GET.pathBodyGET = bodyTestGET_path.get()

            GET.GET()

        else:
            messagebox.showinfo('Error', 'Поле итераций GET запросов должно содержать натуральное число')

    else:
        messagebox.showinfo('Error', 'Все поля GET запросов должны быть заполнены')


def main_destroy():
    main_window.destroy()


def yes_destroy():
    window_yes.destroy()


def no_destroy():
    window_no.destroy()


def destroyPOSTreq():
    POSTreq.destroy()


def destroyGETreq():
    GETreq.destroy()


def insertFileGET():
    file_name = fd.askopenfilename()
    bodyTestGET_path.insert(0, file_name)


def insertFilePOST():
    file_name = fd.askopenfilename()
    bodyTestPOST_path.insert(0, file_name)


def insertFileAmmo():
    file_name = fd.askopenfilename()
    ammoTest_path.insert(0, file_name)

#   //------------------- ВИДЖЕТ ДЛЯ РАБОТЫ С НАПИСАННЫМИ ЗАРАНЕЕ КОНФИГАМИ -------------------\\

def clicked_yes():
    print(choice_tupe.get())
    global iterTestPOST_entry
    global iterTestGET_entry
    global ammoTest_path
    global bodyTestPOST_path
    global bodyTestGET_path
    global POSTreq
    global GETreq


    if 'GET and POST' in choice_tupe.get():
        start.destroy()
        POSTreq = Frame(window_yes, relief = FLAT)
        POSTreq.pack(padx = [5, 5])
        GETreq = Frame(window_yes, relief = FLAT)
        GETreq.pack(padx = [5, 5])

        loadFileMenu = Menu(window_yes)
        window_yes.config(menu = loadFileMenu)
        loadFileMenu.add_command(label = '123')

        nameTestPOST = Label(master = POSTreq, text = "--- POST ---", font = ("Arial", 16), foreground = 'gray')
        nameTestPOST.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 30])

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

        nameTestGET = Label(master = GETreq, text = "--- GET ---", font = ("Arial", 16), foreground = 'gray')
        nameTestGET.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [25, 30])

        iterTest = Label(master = GETreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iterTestGET_entry = Entry(master = GETreq, width = 25)
        iterTestGET_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'w')

        bodyTestGET = Label(master = GETreq, text = "Путь или имя файла конфигурации:", font = ("Arial", 12))
        bodyTestGET.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        bodyTestGET_path = Entry(master = GETreq, width = 25)
        bodyTestGET_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'w')

        iterTest_btn = Button(master = GETreq, text = 'Принять', command = lambda:[createGET(), createPOST()])
        iterTest_btn.grid(column = 2, row = 3, padx = [10, 20], pady = [50, 10])

        back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[destroyGETreq(), destroyPOSTreq(), wiget_dontgenerate(), window_yes.config(loadFileMenu.destroy())])
        back_btn.grid(column = 1, row = 3, padx = [10, 20], pady = [50, 10])

        btn_insertFile = Button(master = POSTreq, text = 'Открыть', command = insertFilePOST)
        btn_insertFile.grid(column = 2, row = 2, padx = [44, 20], pady = [5, 5])
        btn1_insertFile = Button(master = POSTreq, text = 'Открыть', command = insertFileAmmo)
        btn1_insertFile.grid(column = 2, row = 3, padx = [44, 20], pady = [5, 5])
        btn2_insertFile = Button(master = GETreq, text = 'Открыть', command = insertFileGET)
        btn2_insertFile.grid(column = 2, row = 2, padx = [10, 20], pady = [5, 5])

        print('Ожидание ввода параметров')


    elif 'POST' in choice_tupe.get():
        start.destroy()
        POSTreq = Frame(window_yes, relief = FLAT)
        POSTreq.pack(pady = [5, 5])

        loadFileMenu = Menu(window_yes)
        window_yes.config(menu = loadFileMenu)
        loadFileMenu.add_command(label = '123')

        nameTestPOST = Label(master = POSTreq, text = "--- POST ---", font = ("Arial", 16), foreground = 'gray')
        nameTestPOST.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 30])

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
        iterTest_btn.grid(column = 2, row = 4, padx = [10, 20], pady = [50, 10])

        back_btn = Button(master = POSTreq, text = 'Вернуться к выбору запросов', command = lambda:[destroyPOSTreq(), wiget_dontgenerate(), window_yes.config(loadFileMenu.destroy())])
        back_btn.grid(column = 1, row = 4, padx = [10, 20], pady = [50, 10])

        btn_insertFile = Button(master = POSTreq, text = 'Открыть', command = insertFilePOST)
        btn_insertFile.grid(column = 2, row = 2, padx = [10, 20], pady = [5, 5])
        btn1_insertFile = Button(master = POSTreq, text = 'Открыть', command = insertFileAmmo)
        btn1_insertFile.grid(column = 2, row = 3, padx = [10, 20], pady = [5, 5])

        print('Ожидание ввода параметров')


    elif 'GET' in choice_tupe.get():
        start.destroy()
        GETreq = Frame(window_yes, relief = FLAT)
        GETreq.pack(pady = [5, 5])

        loadFileMenu = Menu(window_yes)
        window_yes.config(menu = loadFileMenu)
        loadFileMenu.add_command(label = '123')

        nameTestGET = Label(master = GETreq, text = "--- GET ---", font = ("Arial", 16), foreground = 'gray')
        nameTestGET.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 30])

        iterTest = Label(master = GETreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iterTestGET_entry = Entry(master = GETreq, width = 25)
        iterTestGET_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])

        bodyTestGET = Label(master = GETreq, text = "Путь или имя файла конфигурации:", font = ("Arial", 12))
        bodyTestGET.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        bodyTestGET_path = Entry(master = GETreq, width = 25)
        bodyTestGET_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])

        iterTest_btn = Button(master = GETreq, text = 'Принять', command = createGET)
        iterTest_btn.grid(column = 2, row = 3, padx = [10, 20], pady = [50, 10])

        back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[destroyGETreq(), wiget_dontgenerate(), window_yes.config(loadFileMenu.destroy())])
        back_btn.grid(column = 1, row = 3, padx = [10, 20], pady = [50, 10])

        btn_insertFile = Button(master = GETreq, text = 'Открыть', command = insertFileGET)
        btn_insertFile.grid(column = 2, row = 2, padx = [10, 20], pady = [5, 5])

        print('Ожидание ввода параметров')


    else:
        messagebox.showinfo('Ошибка ввода', 'Вы не выбрали тип запросов, попробуйте еще раз')


def wiget_dontgenerate():
    global choice_tupe
    global start

    start = Frame(window_yes, relief = FLAT)
    start.pack(padx = 10, pady = 10)

    type_req = Label(master = start, text = "Выберите тип запросов:", font = ("Arial", 16))
    type_req.pack(pady = [5, 5])

    tupeTest = ("GET", "POST", "GET and POST")

    choice_tupe = Combobox(master = start, values = tupeTest, width = 25)
    choice_tupe.current()
    choice_tupe.pack(pady = [5, 5])

    choice_btn = Button(master = start,  text = 'Выбрать', command = clicked_yes)
    choice_btn.pack(fill = X, padx = 5, pady = 5)
    back_btn = Button(master = start, text = 'Назад', command = lambda:[yes_destroy(), create_main()])
    back_btn.pack(fill = X, padx = 5, pady = 5)


def create_yes():
    global window_yes

    window_yes = Tk()
    window_yes.title("Тестовое окно")
    window_yes.maxsize(800, 500)
    window_yes.minsize(550, 150)
    window_yes.resizable(False, False)

    wiget_dontgenerate()

    window_yes.mainloop()

#   \\------------------- КОНЕЦ ВИДЖЕТА ДЛЯ РАБОТЫ С НАПИСАННЫМИ ЗАРАНЕЕ КОНФИГАМИ -------------------//
# --------------------------------------------------------------------------------------------------------
# //------------------- ВИДЖЕТ ДЛЯ ГЕНЕРАЦИИ КОНФИГУРАЦИОННЫХ ФАЙЛОВ И РАБОТЫ С НИМИ -------------------\\

def generateFiles():
    
    if 'GET and POST' in choice_tupe.get():
        start.destroy()

        if 'yes' in selected.get():
            print('123')

    elif 'POST' in choice_tupe.get():
        start.destroy()

        if 'yes' in selected.get():
            print('123')

    elif 'GET' in choice_tupe.get():
        start.destroy()

        if 'yes' in selected.get():
            print('123')


def clicked_no():
    global choice_auth
    global selected

    choice_auth = Frame(window_no, relief = FLAT)
    choice_auth.pack(padx = 10, pady = 10)

    auth_yes_no = Label(master = choice_auth, text = "Нужно ли указать токен для авторизации?", font = ("Arial", 16))
    auth_yes_no.grid(columnspan = 2, pady = [5, 5])

    selected = IntVar()
    needToken = Radiobutton(master = choice_auth, text = 'Да, токен необходим', value = 'yes', variable = selected)
    needToken.grid(column = 0, row = 1)
    dontNeedToken = Radiobutton(master = choice_auth, text = 'Нет, токен не требуется', value = 'no', variable = selected)
    dontNeedToken.grid(column = 1, row = 1)
    
    btn = Button(master = choice_auth, text = 'Выбрать', command = generateFiles())
    btn.pack(fill = X, padx = 5, pady = 5)


def wiget_generate():
    global choice_tupe
    global start

    start = Frame(window_no, relief = FLAT, padding = [8, 10])
    start.pack(padx = 10, pady = 10) 

    type_req = Label(master = start, text = "Выберите тип запросов:", font = ("Arial", 16))
    type_req.pack(pady = [5, 5])

    tupeTest = ("GET", "POST", "GET and POST")

    choice_tupe = Combobox(master = start, values = tupeTest, width = 25)
    choice_tupe.current()
    choice_tupe.pack(pady = [5, 5])

    choice_btn = Button(master = start,  text = 'Выбрать', command = clicked_no)
    choice_btn.pack(fill = X, padx = 5, pady = 5)
    back_btn = Button(master = start, text = 'Назад', command = lambda:[no_destroy(), create_main()])
    back_btn.pack(fill = X, padx = 5, pady = 5)


def create_no():
    global window_no

    window_no = Tk()
    window_no.title("Тестовое окно")
    window_no.maxsize(900, 900)
    window_no.minsize(550, 150)
    window_no.resizable(False, False)

    wiget_generate()

    window_no.mainloop()

# \\---------------- КОНЕЦ ВИДЖЕТА ДЛЯ ГЕНЕРАЦИИ КОНФИГУРАЦИОННЫХ ФАЙЛОВ И РАБОТЫ С НИМИ ----------------//


def create_main():
    global main_window

    main_window = Tk()
    main_window.title('Редиска')
    main_window.maxsize(800, 800)
    main_window.minsize(400, 150)

    start_title = Label(main_window, text = "У вас есть файлы конфигурации?", font = ("Arial", 18))
    start_title.pack(padx = 10, pady = 10)

    btn_yes = Button(main_window, text = 'Есть конфигурационные файлы', command = lambda:[main_destroy(), create_yes(), wiget_dontgenerate()])
    btn_yes.pack(fill = X, padx = 10, pady = [10, 10])

    btn_no = Button(main_window, text = 'Нет конфигурационных файлов', command = lambda:[main_destroy(), create_no(), wiget_generate()])
    btn_no.pack(fill = X, padx = 10, pady = [0, 10])

    main_window.mainloop()


create_main()