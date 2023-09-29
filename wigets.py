from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import scrolledtext
from textwrap import wrap
import run_test
import config_generator

#    messagebox.showinfo('Тест1', "Тест")

def create_post():
    if len(bodyTestPOST_path.get()) > 0 and len(ammoTest_path.get()) > 0:

        if  ((iterTestPOST_entry.get().isdigit()) > 0) and (int(iterTestPOST_entry.get()) > 0):
            POST = run_test.Choice_Type('POST')
            POST.iterrationPOST = int(iterTestPOST_entry.get())
            POST.pathBodyPOST = bodyTestPOST_path.get()
            POST.pathAmmo = ammoTest_path.get()
            POST.POST()

        else:
            messagebox.showinfo('Error', 'Поле итераций POST запросов должно содержать натуральное число')

    else:
        messagebox.showinfo('Error', 'Все поля POST запросов должны быть заполнены')


def create_get():
    if len(bodyTestGET_path.get()) > 0:

        if  ((iterTestGET_entry.get().isdigit()) > 0) and (int(iterTestGET_entry.get()) > 0):
            GET = run_test.Choice_Type('GET')
            GET.iterrationGET = int(iterTestGET_entry.get())
            GET.pathBodyGET = bodyTestGET_path.get()

            GET.GET()

        else:
            messagebox.showinfo('Error', 'Поле итераций GET запросов должно содержать натуральное число')

    else:
        messagebox.showinfo('Error', 'Все поля GET запросов должны быть заполнены')

'''
def generatePOST():

    generatePOST = config_generator.loadPOST("loadPOST")
    generatePOST.host = "example.net"
    generatePOST.port = "443"
    generatePOST.ammo_file = "ammo_POST.txt"
    generatePOST.ssl = "true"
    generatePOST.schedule = "line(1, 10000, 5m) const(5000,2m)"
    generatePOST.instances = "1000"
    generatePOST.c_enabled = "true"
    generatePOST.t_enabled = "false"
    generatePOST.o_enabled = "true"
    generatePOST.job_dsc = "testing_POST_requests"
    loadPOST_text = generatePOST.load()
    with open('load.yaml', 'w+') as loadPOST_file:
        loadPOST_file.write(loadPOST_text)
    print(loadPOST_text)
'''
#  //--------------- КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ GET И POST ЗАПРОСОВ ----------------\\

class wigetGETandPOST_requests:

    def __init__(self, name):
        self.name = name
        self.btnType = ''

    def GETandPOST(self):
        global iterTestPOST_entry
        global iterTestGET_entry
        global ammoTest_path
        global bodyTestPOST_path
        global bodyTestGET_path
        global POSTreq
        global GETreq

        start.destroy()

        POSTreq = Frame(window_yes, relief = FLAT)
        POSTreq.pack(padx = [5, 5])
        GETreq = Frame(window_yes, relief = FLAT)
        GETreq.pack(padx = [5, 5])

        loadFileMenu = Menu(window_yes)
        window_yes.config(menu = loadFileMenu)
        loadFileMenu.add_command(label = 'Справка')

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

        
        if 'yes' in self.btnType:
            iterTest_btn = Button(master = GETreq, text = 'Принять', command = lambda:[create_get(), create_post()])
            iterTest_btn.grid(column = 2, row = 3, padx = [10, 20], pady = [50, 10])

            back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[GETreq.destroy(), POSTreq.destroy(), wiget_dontgenerate(), window_yes.config(loadFileMenu.destroy())])
            back_btn.grid(column = 1, row = 3, padx = [10, 20], pady = [50, 10])

        elif 'no' in self.btnType:
            iterTest_btn = Button(master = GETreq, text = 'Принять', command = lambda:[create_get(), create_get()])
            iterTest_btn.grid(column = 2, row = 3, padx = [10, 20], pady = [50, 10])

            back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[GETreq.destroy(), POSTreq.destroy(), wiget_dontgenerate(), window_yes.config(loadFileMenu.destroy())])
            back_btn.grid(column = 1, row = 3, padx = [10, 20], pady = [50, 10])

        btn_insertFile = Button(master = POSTreq, text = 'Открыть', command = insertFilePOST)
        btn_insertFile.grid(column = 2, row = 2, padx = [44, 20], pady = [5, 5])
        btn1_insertFile = Button(master = POSTreq, text = 'Открыть', command = insertFileAmmo)
        btn1_insertFile.grid(column = 2, row = 3, padx = [44, 20], pady = [5, 5])
        btn2_insertFile = Button(master = GETreq, text = 'Открыть', command = insertFileGET)
        btn2_insertFile.grid(column = 2, row = 2, padx = [10, 20], pady = [5, 5])

#  \\--------------- КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ GET И POST ЗАПРОСОВ ----------------//
#  ------------------------------------------------------------------------------------------------------
#  //------------------ КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ POST ЗАПРОСОВ -------------------\\

class wigetPOST_requests:

    def __init__(self, name):
        self.name = name
        self.btnType = ''

    def POST(self):
        global iterTestPOST_entry
        global ammoTest_path
        global bodyTestPOST_path
        global POSTreq

        start.destroy()

        POSTreq = Frame(window_yes, relief = FLAT)
        POSTreq.pack(pady = [5, 5])

        loadFileMenu = Menu(window_yes)
        window_yes.config(menu = loadFileMenu)
        loadFileMenu.add_command(label = 'Справка')

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

        if 'yes' in self.btnType:
            iterTest_btn = Button(master = POSTreq, text = 'Принять', command = create_post)
            iterTest_btn.grid(column = 2, row = 4, padx = [10, 20], pady = [50, 10])
        
            back_btn = Button(master = POSTreq, text = 'Вернуться к выбору запросов', command = lambda:[POSTreq.destroy(), wiget_dontgenerate(), window_yes.config(loadFileMenu.destroy())])
            back_btn.grid(column = 1, row = 4, padx = [10, 20], pady = [50, 10])

        elif 'no' in self.btnType:
            iterTest_btn = Button(master = POSTreq, text = 'Принять', command = create_post)
            iterTest_btn.grid(column = 2, row = 4, padx = [10, 20], pady = [50, 10])

            back_btn = Button(master = POSTreq, text = 'Вернуться к выбору запросов', command = lambda:[POSTreq.destroy(), wiget_dontgenerate(), window_yes.config(loadFileMenu.destroy())])
            back_btn.grid(column = 1, row = 4, padx = [10, 20], pady = [50, 10])

        btn_insertFile = Button(master = POSTreq, text = 'Открыть', command = insertFilePOST)
        btn_insertFile.grid(column = 2, row = 2, padx = [10, 20], pady = [5, 5])
        btn1_insertFile = Button(master = POSTreq, text = 'Открыть', command = insertFileAmmo)
        btn1_insertFile.grid(column = 2, row = 3, padx = [10, 20], pady = [5, 5])

#  \\------------------ КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ POST ЗАПРОСОВ -------------------//
#  ------------------------------------------------------------------------------------------------------
#  //------------------- КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ GET ЗАПРОСОВ -------------------\\

class wigetGET_requests:

    def __init__(self, name):
        self.name = name
        self.btnType = ''

    def GET(self):
        global iterTestGET_entry
        global bodyTestGET_path
        global GETreq

        start.destroy()

        GETreq = Frame(window_yes, relief = FLAT)
        GETreq.pack(pady = [5, 5])

        loadFileMenu = Menu(window_yes)
        window_yes.config(menu = loadFileMenu)
        loadFileMenu.add_command(label = 'Справка')

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

        if 'yes' in self.btnType:
            iterTest_btn = Button(master = GETreq, text = 'Принять', command = create_get)
            iterTest_btn.grid(column = 2, row = 3, padx = [10, 20], pady = [50, 10])

            back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[GETreq.destroy(), wiget_dontgenerate(), window_yes.config(loadFileMenu.destroy())])
            back_btn.grid(column = 1, row = 3, padx = [10, 20], pady = [50, 10])

        elif 'no' in self.btnType:
            iterTest_btn = Button(master = GETreq, text = 'Принять', command = create_get)
            iterTest_btn.grid(column = 2, row = 3, padx = [10, 20], pady = [50, 10])

            back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[GETreq.destroy(), wiget_dontgenerate(), window_yes.config(loadFileMenu.destroy())])
            back_btn.grid(column = 1, row = 3, padx = [10, 20], pady = [50, 10])

        btn_insertFile = Button(master = GETreq, text = 'Открыть', command = insertFileGET)
        btn_insertFile.grid(column = 2, row = 2, padx = [10, 20], pady = [5, 5])

# \\------------------- КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ GET ЗАПРОСОВ -------------------//
#  ------------------------------------------------------------------------------------------------------
#      //------------------- КОД ВИДЖЕТА ГЕНЕРАТОРА КОНФИГУРАЦИЙ GET ЗАПРОСОВ -------------------\\

class wiget_generator_GET:

    def __init__(self, name):
        self.name = name
        self.create_token = ''

    def generator_GET(self):
        
        generate_GET = Frame(window_no, relief = FLAT)
        generate_GET.pack(pady = [5, 5])

        generatorGET_name = Label(master = generate_GET, text = '--- GET query customization generator ---', font = ('Arial', 16), foreground = 'gray')
        generatorGET_name.grid(columnspan = 3, row = 0, pady = [5, 5])

        if 'no' in self.create_token:
            labels = ['Хост сайта:', 'Порт:', 'Agent:', 'Количество потоков:',
                      'Параметры нагрузки:', 'Имя теста:', 'Визуализация в консоли',
                      'Загрузить и обработать результат']
        
        elif 'yes' in self.create_token:
            labels = ['Хост сайта:', 'Порт:', 'User agent:', 'Токен авторизации:',
                      'Количество потоков:', 'Параметры нагрузки:', 'Имя теста:',
                      'Визуализация в консоли', 'Загрузить и обработать результат']

        y = 1
        for a in labels:
            enter_name = Label(master = generate_GET, text = a, font = ('Arial', 12))
            enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [5, 5], sticky = 'se')
            if a == 'Порт:':
                enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [5, 5], sticky = 'e')
            if a == 'Хост сайта:':
                enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [5, 15], sticky = 'se')
            if a == 'User agent:':
                enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [15, 5], sticky = 'se')
            y += 1

        def selected_https():
            if port_entry.get() == 'Введите или выберите значение' or '80':
                port_entry.delete(0, 'end')
                port_entry.insert(0, '443')
                port_entry.configure(foreground = 'black')

        def selected_http():
            if port_entry.get() == 'Введите или выберите значение' or '443':
                port_entry.delete(0, 'end')
                port_entry.insert(0, '80')
                port_entry.configure(foreground = 'black')

        def placeholder_url_delete():
            if path_url_entry.get(1.0, 'end-1c') == 'Пример ввода:\n-/my/example/url\n\nКаждая ссылка должна быть с новой строки':
                path_url_entry.delete(1.0, 'end')
                path_url_entry.configure(foreground = 'black')

        def placeholder_name_delete():            
            if name_test_entry.get() == 'Как-нибудь назовите тест':
                name_test_entry.delete(0, 'end')
                name_test_entry.configure(foreground = 'black')

        def placeholder_load_params_delete():
            if load_params_entry.get() == 'line(1, 100, 5m) const(50,2m)':
                load_params_entry.delete(0, 'end')
                load_params_entry.configure(foreground = 'black')

        def placeholder_quantity_threads_entry_delete():
            if quantity_threads_entry.get() == '1000':
                quantity_threads_entry.delete(0, 'end')
                quantity_threads_entry.configure(foreground = 'black')

        def placeholder_auth_token_delete():
            if auth_token_entry.get() == 'Введите cookie авторизации':
                auth_token_entry.delete(0, 'end')
                auth_token_entry.configure(foreground = 'black')

        def host_entry_delete():
            if host_entry.get() == 'Например: example.com':
                host_entry.delete(0, 'end')
                host_entry.configure(foreground = 'black')

        def port_entry_delete():
            if port_entry.get() == 'Введите или выберите значение':
                port_entry.delete(0, 'end')
                port_entry.configure(foreground = 'black')
        
        def placeholder_url_insert():
            if path_url_entry.get(1.0, 'end-1c') == '':
                path_url_entry.insert(1.0, 'Пример ввода:\n-/my/example/url\n\nКаждая ссылка должна быть с новой строки')
                path_url_entry.configure(foreground = 'gray')

        def placeholder_name_insert():
            if name_test_entry.get() == '':
                name_test_entry.insert(0, 'Как-нибудь назовите тест')
                name_test_entry.configure(foreground = 'gray')
        
        def placeholder_load_params_insert():
            if load_params_entry.get() == '':
                load_params_entry.insert(0, 'line(1, 100, 5m) const(50,2m)')
                load_params_entry.configure(foreground = 'gray')

        def placeholder_quantity_threads_entry_insert():
            if quantity_threads_entry.get() == '':
                quantity_threads_entry.insert(0, '1000')
                quantity_threads_entry.configure(foreground = 'gray')

        def placeholder_auth_token_insert():
            if auth_token_entry.get() == '':
                auth_token_entry.insert(0, 'Введите cookie авторизации')
                auth_token_entry.configure(foreground = 'gray')

        def host_entry_insert():
            if host_entry.get() == '':
                host_entry.insert(0, 'Например: example.com')
                host_entry.configure(foreground = 'gray')

        def port_entry_insert():
            if port_entry.get() == '':
                selected_port.set('')
                port_entry.insert(0, 'Введите или выберите значение')
                port_entry.configure(foreground = 'gray')
            
            if port_entry.get() == '443':
                selected_port.set('443')
                ssl = 'true'

            if (port_entry.get() == 'https') or (port_entry.get() == 'https://') or (port_entry.get() == 'https:') or (port_entry.get() == 'https:/'):
                selected_port.set('443')
                port_entry.delete(0, 'end')
                port_entry.insert(0, '443')
                ssl = 'true'

            if (port_entry.get() == 'http') or (port_entry.get() == 'http://') or (port_entry.get() == 'http:') or (port_entry.get() == 'http:/'):
                selected_port.set('80')
                port_entry.delete(0, 'end')
                port_entry.insert(0, '80')
                ssl = 'false'

            if port_entry.get() == '80':
                selected_port.set('80')
                ssl = 'false'

        host_entry = Entry(master = generate_GET, width = 27)
        host_entry.insert(0, 'Например: example.com')
        host_entry.configure(foreground = 'gray')
        host_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 15])
        host_entry.bind('<FocusIn>', (lambda args: [host_entry_delete()]))
        host_entry.bind('<FocusOut>', (lambda args: [host_entry_insert()]))

        port_entry = Entry(master = generate_GET, width = 27)
        port_entry.insert(0, 'Введите или выберите значение')
        port_entry.configure(foreground = 'gray')
        port_entry.bind('<FocusIn>', (lambda args: [port_entry_delete()]))
        port_entry.bind('<FocusOut>', (lambda args: [port_entry_insert()]))
        port_entry.grid(column = 1, row = 2, sticky = N, padx = [5, 5], pady = [5, 25])
        selected_port = StringVar()
        selected_port.set('')
        port_radiobutton_443 = Radiobutton(master = generate_GET, text = 'https://', command = selected_https, value = '443', variable = selected_port)
        port_radiobutton_443.grid(column = 1, row = 2, sticky = SW, padx = [15, 15])
        port_radiobutton_80 = Radiobutton(master = generate_GET, text = 'http://', command = selected_http, value = '80', variable = selected_port)
        port_radiobutton_80.grid(column = 1, row = 2, sticky = SE, padx = [15, 15])

        user_agent_entry = Entry(master = generate_GET, width = 27)
        user_agent_entry.grid(column = 1, row = 3, padx = [5, 5], pady = [15, 5])

        y = 4
        if 'yes' in self.create_token:
            y += 1
            auth_token_entry = Entry(master = generate_GET, width = 27)
            auth_token_entry.insert(0, 'Введите cookie авторизации')
            auth_token_entry.configure(foreground = 'gray')
            auth_token_entry.grid(column = 1, row = 4, padx = [5, 5], pady = [5, 5])
            auth_token_entry.bind('<FocusIn>', (lambda args: [placeholder_auth_token_delete()]))
            auth_token_entry.bind('<FocusOut>', (lambda args: [placeholder_auth_token_insert()]))

        quantity_threads_entry = Entry(master = generate_GET, width = 27)
        quantity_threads_entry.insert(0, '1000')
        quantity_threads_entry.configure(foreground = 'gray')
        quantity_threads_entry.grid(column = 1, row = y, padx = [5, 5], pady = [5, 5])
        quantity_threads_entry.bind('<FocusIn>', (lambda args: [placeholder_quantity_threads_entry_delete()]))
        quantity_threads_entry.bind('<FocusOut>', (lambda args: [placeholder_quantity_threads_entry_insert()]))
        
        y += 1
        load_params_entry = Entry(master = generate_GET, width = 27)
        load_params_entry.insert(0, 'line(1, 100, 5m) const(50,2m)')
        load_params_entry.configure(foreground = 'gray')
        load_params_entry.grid(column = 1, row = y, padx = [5, 5], pady = [5, 5])
        load_params_entry.bind('<FocusIn>', (lambda args: [placeholder_load_params_delete()]))
        load_params_entry.bind('<FocusOut>', (lambda args: [placeholder_load_params_insert()]))

        y += 1
        name_test_entry = Entry(master = generate_GET, width = 27)
        name_test_entry.insert(0, 'Введите название теста')
        name_test_entry.configure(foreground = 'gray')
        name_test_entry.grid(column = 1, row = y, padx = [5, 5], pady = [5, 5])
        name_test_entry.bind('<FocusIn>', (lambda args: [placeholder_name_delete()]))
        name_test_entry.bind('<FocusOut>', (lambda args: [placeholder_name_insert()]))

        y += 1
        console_entry = Radiobutton(master = generate_GET)
        console_entry.grid(column = 1, row = y, padx = [5, 5], pady = [5, 5])

        y += 1
        overload_entry = Entry(master = generate_GET, width = 27)
        overload_entry.grid(column = 1, row = y, padx = [5, 5], pady = [5, 5])

        path_url_label = Label(master = generate_GET, text = 'Введите ссылки на страницы без хоста сайта:', font = ('Arial', 12))
        path_url_label.grid(columnspan = 3, row = (y + 1), pady = [25, 5])
        path_url_entry = scrolledtext.ScrolledText(master = generate_GET, width = 50, height = 5)
        path_url_entry.insert(1.0, 'Пример ввода:\n-/my/example/url\n\nКаждая ссылка должна быть с новой строки')
        path_url_entry.configure(foreground = 'gray')
        path_url_entry.grid(columnspan = 3, row = (y + 2), padx = [5, 5], pady = [5, 5])
        path_url_entry.bind('<FocusIn>', (lambda args:[placeholder_url_delete()]))
        path_url_entry.bind('<FocusOut>', (lambda args:[placeholder_url_insert()]))

        select_btn = Button(master = generate_GET, text = 'Принять', command = print('selected'))
        select_btn.grid(column = 2, row = (y + 3), padx = [10, 10], pady = [20, 10])
        back_btn =Button(master = generate_GET, text = 'Вернуться к выбору запросов', command = lambda:[generate_GET.destroy(), wiget_generate()])
        back_btn.grid(column = 1, row = (y + 3), padx = [10, 10], pady = [20, 10])

#      \\------------------- КОД ВИДЖЕТА ГЕНЕРАТОРА КОНФИГУРАЦИЙ GET ЗАПРОСОВ -------------------//

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

    if 'GET and POST' in choice_type.get():
        create_wiget = wigetGETandPOST_requests('create_wiget')
        create_wiget.btnType = 'yes'
        create_wiget.GETandPOST()

    elif 'POST' in choice_type.get():
        create_wiget = wigetPOST_requests('create_wiget')
        create_wiget.btnType = 'yes'
        create_wiget.POST()

    elif 'GET' in choice_type.get():
        create_wiget = wigetGET_requests('create_wiget')
        create_wiget.btnType = 'yes'
        create_wiget.GET()

    else:
        messagebox.showinfo('Ошибка ввода', 'Не выбран тип запросов или введен неверный формат, попробуйте еще раз')


def wiget_dontgenerate():
    global choice_type
    global start

    start = Frame(window_yes, relief = FLAT)
    start.pack(padx = 10, pady = 10)

    type_req = Label(master = start, text = "Выберите тип запросов:", font = ("Arial", 16))
    type_req.pack(pady = [5, 5])

    tupeTest = ("GET", "POST", "GET and POST")

    choice_type = Combobox(master = start, values = tupeTest, width = 25)
    choice_type.current()
    choice_type.pack(pady = [5, 5])

    choice_btn = Button(master = start,  text = 'Выбрать', command = clicked_yes)
    choice_btn.pack(fill = X, padx = 5, pady = 5)
    back_btn = Button(master = start, text = 'Назад', command = lambda:[window_yes.destroy(), create_main()])
    back_btn.pack(fill = X, padx = 5, pady = 5)


def create_present():
    global window_yes

    window_yes = Tk()
    window_yes.title("Тестовое окно")
    window_yes.maxsize(1000, 1000)
    window_yes.minsize(750, 500)
    window_yes.resizable(False, False)

    wiget_dontgenerate()

    window_yes.mainloop()

#   \\------------------- КОНЕЦ ВИДЖЕТА ДЛЯ РАБОТЫ С НАПИСАННЫМИ ЗАРАНЕЕ КОНФИГАМИ -------------------//
# --------------------------------------------------------------------------------------------------------
# //------------------- ВИДЖЕТ ДЛЯ ГЕНЕРАЦИИ КОНФИГУРАЦИОННЫХ ФАЙЛОВ И РАБОТЫ С НИМИ -------------------\\


def generateFiles():
    choice_type

    if ('yes' in selected.get()) or ('no' in selected.get()):

        if 'GET and POST' in typeREQ:
            choice_auth.destroy()

            if "yes" in selected.get():

                print(selected.get())
                #config_generator.generateGET()
                #config_generator.generateAmmo()
                #config_generator.generatePOST()

        elif 'POST' in typeREQ:
            choice_auth.destroy()

            if "yes" in selected.get():
                
                print(selected.get())
                #config_generator.generatePOST()
                #config_generator.generateAmmo()

        elif 'GET' in typeREQ:
            choice_auth.destroy()

            if "yes" in selected.get(): 
                create_wiget = wiget_generator_GET('create_wiget')
                create_wiget.create_token = selected.get()
                create_wiget.generator_GET()

            elif "no" in selected.get(): 
                create_wiget = wiget_generator_GET('create_wiget')
                create_wiget.create_token = selected.get()
                create_wiget.generator_GET()

    else:
        messagebox.showinfo('Ошибка ввода', 'Необходимо указать нужен ли токен для авторизации на сайте')
       

def clicked_no():
    if choice_type.get() in typeTest:
        global choice_auth
        global selected
        global typeREQ
        typeREQ = choice_type.get()

        start.destroy()

        choice_auth = Frame(window_no, relief = FLAT)
        choice_auth.pack(padx = 10, pady = 10)

        auth_yes_no = Label(master = choice_auth, text = "Нужно ли указать токен для авторизации?", font = ("Arial", 16))
        auth_yes_no.grid(columnspan = 2, pady = [5, 5])

        selected = StringVar()
        selected.set('')
        needToken = Radiobutton(master = choice_auth, text = 'Да, токен необходим', value = 'yes', variable = selected)
        needToken.grid(column = 0, row = 1)
        dontNeedToken = Radiobutton(master = choice_auth, text = 'Нет, токен не требуется', value = 'no', variable = selected)
        dontNeedToken.grid(column = 1, row = 1)
        
        btn = Button(master = choice_auth, text = 'Выбрать', command = generateFiles)
        btn.grid(columnspan = 2, row = 2, padx = 5, pady = [25, 5])
        back_btn = Button(master = choice_auth, text = 'Назад', command = lambda:[choice_auth.destroy(), wiget_generate()])
        back_btn.grid(columnspan = 2, row = 3, padx = 5, pady = 5)

    else:
        messagebox.showinfo('Ошибка ввода', 'Не выбран тип запросов или введен неверный формат, попробуйте еще раз')


def wiget_generate():
    global choice_type
    global start
    global typeTest

    start = Frame(window_no, relief = FLAT)
    start.pack(padx = 10, pady = 10) 

    type_req = Label(master = start, text = "Выберите тип запросов:", font = ("Arial", 16))
    type_req.pack(pady = [5, 5])

    typeTest = ("GET", "POST", "GET and POST")

    choice_type = Combobox(master = start, values = typeTest, width = 25)
    choice_type.current()
    choice_type.pack(pady = [5, 5])

    choice_btn = Button(master = start,  text = 'Выбрать', command = clicked_no)
    choice_btn.pack(fill = X, padx = 5, pady = 5)
    back_btn = Button(master = start, text = 'Назад', command = lambda:[window_no.destroy(), create_main()])
    back_btn.pack(fill = X, padx = 5, pady = 5)


def create_absent():
    global window_no

    window_no = Tk()
    window_no.title("Тестовое окно")
    window_no.maxsize(1000, 1000)
    window_no.minsize(750, 500)
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

    btn_yes = Button(main_window, text = 'Есть конфигурационные файлы', command = lambda:[main_window.destroy(), create_present(), wiget_dontgenerate()])
    btn_yes.pack(fill = X, padx = 10, pady = [10, 10])

    btn_no = Button(main_window, text = 'Нет конфигурационных файлов', command = lambda:[main_window.destroy(), create_absent(), wiget_generate()])
    btn_no.pack(fill = X, padx = 10, pady = [0, 10])

    main_window.mainloop()


create_main()