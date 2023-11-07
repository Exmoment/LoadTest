from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import scrolledtext
from idlelib.tooltip import Hovertip
from run_test import Choice_Type
from config_generator import *
import interface.controller_widgets as controller_widgets


def create_get():
    if len(body_test_get_path.get()) > 0 and (body_test_get_path.get() != 'Укажите путь к файлу'):

        if  ((iter_test_get_entry.get().isdigit()) > 0) and (int(iter_test_get_entry.get()) > 0):
            start_get = Choice_Type('GET')
            start_get.iterrationGET = int(iter_test_get_entry.get())
            start_get.pathBodyGET = body_test_get_path.get()

            start_get.GET()

        else:
            messagebox.showinfo('Error_GET', 'Поле итераций GET запросов должно содержать натуральное число')

    else:
        messagebox.showinfo('Error_POST', 'Необходимо указать путь к файлу конфигурации')

# //---------------------- КОД ВИДЖЕТА ГЕНЕРАТОРА КОНФИГУРАЦИЙ GET ЗАПРОСОВ -----------------------\\

class Widget_Generator_GET:

    def __init__(self, name):
        self.name = name
        self.create_token = ''

    def generator_get(self):
        global generate_get

        generate_get = Frame(controller_widgets.window_no, relief = FLAT)
        generate_get.pack(pady = [5, 5])

        generator_get_name = Label(master = generate_get, text = '--- GET query customization generator ---', font = ('Arial', 16), foreground = 'gray')
        generator_get_name.grid(columnspan = 3, row = 0, pady = [5, 5])

        if 'no' in self.create_token:
            labels = ['Хост сайта:', 'Порт:', 'User agent:', 'Количество экземпляров:',
                      'Параметры нагрузки:', 'Имя теста:', 'Вывод в консоли',
                      'Загрузить и обработать результат']
        
        elif 'yes' in self.create_token:
            labels = ['Хост сайта:', 'Порт:', 'User agent:', 'Токен авторизации:',
                      'Количество экземпляров:', 'Параметры нагрузки:', 'Имя теста:',
                      'Вывод в консоли', 'Загрузить и обработать результат']

        y = 1
        for a in labels:
            enter_name = Label(master = generate_get, text = a, font = ('Arial', 12))
            enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [5, 5], sticky = 'se')
            if a == 'Порт:':
                enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [5, 5], sticky = 'e')
            if a == 'Хост сайта:':
                enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [5, 15], sticky = 'se')
            if a == 'User agent:':
                enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [15, 5], sticky = 'se')
            y += 1

        host_entry = Entry(master = generate_get, width = 35)
        host_entry.insert(0, 'Например: example.com')
        host_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        host_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 15])
        host_entry.bind('<FocusIn>', (lambda args: [placeholder_host_entry_delete()]))
        host_entry.bind('<FocusOut>', (lambda args: [placeholder_host_entry_insert()]))

        port_entry = Entry(master = generate_get, width = 35)
        port_entry.insert(0, 'Введите или выберите значение')
        port_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        port_entry.bind('<FocusIn>', (lambda args: [placeholder_port_entry_delete()]))
        port_entry.bind('<FocusOut>', (lambda args: [placeholder_port_entry_insert()]))
        port_entry.grid(column = 1, row = 2, sticky = N, padx = [5, 5], pady = [5, 25])
        selected_port = StringVar()
        selected_port.set('')
        port_radiobutton_443 = Radiobutton(master = generate_get, text = 'https://', command = selected_https, value = '443', variable = selected_port)
        port_radiobutton_443.grid(column = 1, row = 2, sticky = SW, padx = [15, 15])
        port_radiobutton_80 = Radiobutton(master = generate_get, text = 'http://', command = selected_http, value = '80', variable = selected_port)
        port_radiobutton_80.grid(column = 1, row = 2, sticky = S, padx = [25, 15])

        user_agent_entry = Entry(master = generate_get, width = 35)
        user_agent_entry.insert(0, 'Используемый браузер')
        user_agent_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        user_agent_entry.bind('<FocusIn>', (lambda args: [placeholder_user_agent_delete()]))
        user_agent_entry.bind('<FocusOut>', (lambda args: [placeholder_user_agent_insert()]))
        user_agent_entry.grid(column = 1, row = 3, padx = [5, 5], pady = [15, 5])

        y = 4
        if 'yes' in self.create_token:
            y += 1
            auth_token_entry = Entry(master = generate_get, width = 35)
            auth_token_entry.insert(0, 'Введите cookie авторизации')
            auth_token_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
            auth_token_entry.grid(column = 1, row = 4, padx = [5, 5], pady = [5, 5])
            auth_token_entry.bind('<FocusIn>', (lambda args: [placeholder_auth_token_delete()]))
            auth_token_entry.bind('<FocusOut>', (lambda args: [placeholder_auth_token_insert()]))

        quantity_threads_entry = Entry(master = generate_get, width = 35)
        quantity_threads_entry.insert(0, '1000')
        quantity_threads_entry.configure(foreground = 'gray')
        quantity_threads_entry.grid(column = 1, row = y, padx = [5, 5], pady = [5, 5])
        quantity_threads_entry.bind('<FocusIn>', (lambda args: [placeholder_quantity_threads_entry_delete()]))
        quantity_threads_entry.bind('<FocusOut>', (lambda args: [placeholder_quantity_threads_entry_insert()]))
        
        y += 1
        load_params_entry = Entry(master = generate_get, width = 35)
        load_params_entry.insert(0, 'line(1, 100, 5m) const(50,2m)')
        load_params_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        load_params_entry.grid(column = 1, row = y, padx = [5, 5], pady = [5, 5])
        load_params_entry.bind('<FocusIn>', (lambda args: [placeholder_load_params_delete()]))
        load_params_entry.bind('<FocusOut>', (lambda args: [placeholder_load_params_insert()]))

        y += 1
        name_test_entry = Entry(master = generate_get, width = 35)
        name_test_entry.insert(0, 'Введите название теста')
        name_test_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        name_test_entry.grid(column = 1, row = y, padx = [5, 5], pady = [5, 5])
        name_test_entry.bind('<FocusIn>', (lambda args: [placeholder_name_delete()]))
        name_test_entry.bind('<FocusOut>', (lambda args: [placeholder_name_insert()]))

        y += 1
        selected_console = StringVar()
        selected_console.set('')
        console_radiobutton_on = Radiobutton(master = generate_get, text = 'включить', value = 'true', variable = selected_console)
        console_radiobutton_on.grid(column = 1, row = y, sticky = W, padx = [15, 5])
        console_radiobutton_off = Radiobutton(master = generate_get, text = 'отключить', value = 'false', variable = selected_console)
        console_radiobutton_off.grid(column = 1, row = y, padx = [55, 5])

        y += 1
        selected_overload = StringVar()
        selected_overload.set('')
        overload_radiobutton_on = Radiobutton(master = generate_get, text = 'включить', value = 'true', variable = selected_overload)
        overload_radiobutton_on.grid(column = 1, row = y, sticky = W, padx = [15, 5])
        overload_radiobutton_off = Radiobutton(master = generate_get, text = 'отключить', value = 'false', variable = selected_overload)
        overload_radiobutton_off.grid(column = 1, row = y, padx = [55, 5])


        path_url_label = Label(master = generate_get, text = 'Введите ссылки на страницы без хоста сайта:', font = ('Arial', 12))
        path_url_label.grid(columnspan = 3, row = (y + 1), pady = [25, 5])
        path_url_entry = scrolledtext.ScrolledText(master = generate_get, width = 57, height = 5)
        path_url_entry.insert(1.0, 'Пример ввода:\n-/my/example/url\n\nКаждая ссылка должна быть с новой строки')
        path_url_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        path_url_entry.grid(columnspan = 3, row = (y + 2), padx = [5, 5], pady = [5, 5])
        path_url_entry.bind('<FocusIn>', (lambda args:[placeholder_url_delete()]))
        path_url_entry.bind('<FocusOut>', (lambda args:[placeholder_url_insert()]))

        select_btn = Button(master = generate_get, text = 'Принять', command = lambda: [created_file_for_get(), create_next_widget(), generate_get.destroy()])
        select_btn.grid(column = 2, row = (y + 3), padx = [10, 10], pady = [20, 10])
        back_btn = Button(master = generate_get, text = 'Вернуться к выбору запросов', command = lambda:[generate_get.destroy(), controller_widgets.widget_generate()])
        back_btn.grid(column = 1, row = (y + 3), padx = [10, 10], pady = [20, 10])

        Hovertip(select_btn, 'adfgaertqergtrh')
    
        def created_file_for_get():
            if 'yes' in self.create_token:
                created_file = Load_GET_With_Token('Load_GET_With_Token')
            elif 'no' in self.create_token:
                created_file = Load_GET_Non_Token('Load_GET_Non_Token')
            created_file.host = host_entry.get()
            created_file.port = port_entry.get()
            if port_entry.get() == '443':
                created_file.ssl = 'true'
            elif port_entry.get() == '80':
                created_file.ssl = 'false'
            created_file.agent = user_agent_entry.get()
            if 'yes' in self.create_token:
                created_file.token = auth_token_entry.get()
            created_file.url = path_url_entry.get(1.0, 'end-1c')
            created_file.instances = quantity_threads_entry.get()
            created_file.schedule = load_params_entry.get()
            created_file.c_enabled = selected_console.get()
            created_file.t_enabled = 'false'
            created_file.o_enabled = selected_overload.get()
            created_file.job_dsc = name_test_entry.get()
            created_config_text = created_file.load()
            with open(name_test_entry.get()+'.yaml', 'w+') as file:
                file.write(created_file.load())
            print(created_config_text)

        def create_next_widget():
            next_widget = Widget_GET_Requests('next_widget')
            next_widget.file_name = name_test_entry.get()+'.yaml'
            next_widget.GET()
                        
        def selected_https():
            if port_entry.get() == 'Введите или выберите значение' or '80':
                port_entry.delete(0, 'end')
                port_entry.insert(0, '443')
                port_entry.configure(foreground = 'black', font = ('Arial', 11))

        def selected_http():
            if port_entry.get() == 'Введите или выберите значение' or '443':
                port_entry.delete(0, 'end')
                port_entry.insert(0, '80')
                port_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_url_delete():
            if path_url_entry.get(1.0, 'end-1c') == 'Пример ввода:\n-/my/example/url\n\nКаждая ссылка должна быть с новой строки':
                path_url_entry.delete(1.0, 'end')
                path_url_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_name_delete():            
            if name_test_entry.get() == 'Введите название теста':
                name_test_entry.delete(0, 'end')
                name_test_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_load_params_delete():
            if load_params_entry.get() == 'line(1, 100, 5m) const(50,2m)':
                load_params_entry.delete(0, 'end')
                load_params_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_quantity_threads_entry_delete():
            if quantity_threads_entry.get() == '1000':
                quantity_threads_entry.delete(0, 'end')
                quantity_threads_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_auth_token_delete():
            if auth_token_entry.get() == 'Введите cookie авторизации':
                auth_token_entry.delete(0, 'end')
                auth_token_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_host_entry_delete():
            if host_entry.get() == 'Например: example.com':
                host_entry.delete(0, 'end')
                host_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_user_agent_delete():
            if user_agent_entry.get() == 'Используемый браузер':
                user_agent_entry.delete(0, 'end')
                user_agent_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_port_entry_delete():
            if port_entry.get() == 'Введите или выберите значение':
                port_entry.delete(0, 'end')
                port_entry.configure(foreground = 'black', font = ('Arial', 11))
        
        def placeholder_url_insert():
            if path_url_entry.get(1.0, 'end-1c') == '':
                path_url_entry.insert(1.0, 'Пример ввода:\n-/my/example/url\n\nКаждая ссылка должна быть с новой строки')
                path_url_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        def placeholder_name_insert():
            if name_test_entry.get() == '':
                name_test_entry.insert(0, 'Введите название теста')
                name_test_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))
        
        def placeholder_load_params_insert():
            if load_params_entry.get() == '':
                load_params_entry.insert(0, 'line(1, 100, 5m) const(50,2m)')
                load_params_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        def placeholder_quantity_threads_entry_insert():
            if quantity_threads_entry.get() == '':
                quantity_threads_entry.insert(0, '1000')
                quantity_threads_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        def placeholder_auth_token_insert():
            if auth_token_entry.get() == '':
                auth_token_entry.insert(0, 'Введите cookie авторизации')
                auth_token_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        def placeholder_host_entry_insert():
            if host_entry.get() == '':
                host_entry.insert(0, 'Например: example.com')
                host_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        def placeholder_user_agent_insert():
            if user_agent_entry.get() == '':
                user_agent_entry.insert(0, 'Используемый браузер')
                user_agent_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        def placeholder_port_entry_insert():
            if port_entry.get() == '':
                selected_port.set('')
                port_entry.insert(0, 'Введите или выберите значение')
                port_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))
            
            if port_entry.get() == '443':
                selected_port.set('443')

            if (port_entry.get() == 'https') or (port_entry.get() == 'https://') or (port_entry.get() == 'https:') or (port_entry.get() == 'https:/'):
                selected_port.set('443')
                port_entry.delete(0, 'end')
                port_entry.insert(0, '443')

            if (port_entry.get() == 'http') or (port_entry.get() == 'http://') or (port_entry.get() == 'http:') or (port_entry.get() == 'http:/'):
                selected_port.set('80')
                port_entry.delete(0, 'end')
                port_entry.insert(0, '80')

            if port_entry.get() == '80':
                selected_port.set('80')

# \\----------------------- КОД ВИДЖЕТА ГЕНЕРАТОРА КОНФИГУРАЦИЙ GET ЗАПРОСОВ ----------------------//
# --------------------------------------------------------------------------------------------------
# //------------------ КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ GET ЗАПРОСОВ ------------------\\

class Widget_GET_Requests:

    def __init__(self, name):
        self.name = name
        self.file_name = ''

    def GET(self):
        global iter_test_get_entry
        global body_test_get_path
        global get_req

        controller_widgets.start.destroy()

        get_req = Frame(controller_widgets.window_no, relief = FLAT)
        get_req.pack(pady = [5, 5])

        load_file_menu = Menu(controller_widgets.window_no)
        controller_widgets.window_no.config(menu = load_file_menu)
        load_file_menu.add_command(label = 'Справка')

        back_btn = Button(master = get_req, text = 'Вернуться к конфигуратору', command = lambda:[get_req.destroy(), controller_widgets.generate_files(), controller_widgets.window_no.config(load_file_menu.destroy())])
        back_btn.grid(column = 1, row = 3, padx = [10, 20], pady = [50, 10])

        name_test_get = Label(master = get_req, text = "--- GET ---", font = ("Arial", 16), foreground = 'gray')
        name_test_get.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 30])

        iter_test = Label(master = get_req, text = "Количество итераций тестов:", font = ("Arial", 12))
        iter_test.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iter_test_get_entry = Entry(master = get_req, width = 25)
        iter_test_get_entry.insert(0, '1')
        iter_test_get_entry.configure(foreground = 'gray', font = 'Arial 11 italic')
        iter_test_get_entry.bind('<FocusIn>', (lambda args: [iter_test_get_entry_delete()]))
        iter_test_get_entry.bind('<FocusOut>', (lambda args: [iter_test_get_entry_insert()]))
        iter_test_get_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])

        body_test_get = Label(master = get_req, text = "Файл с конфигурацией:", font = ("Arial", 12))
        body_test_get.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        body_test_get_path = Entry(master = get_req, width = 25)
        body_test_get_path.insert(0, 'Укажите путь к файлу')
        body_test_get_path.configure(foreground = 'gray', font = 'Arial 11 italic')
        body_test_get_path.bind('<FocusIn>', (lambda args: [body_test_get_path_delete()]))
        body_test_get_path.bind('<FocusOut>', (lambda args: [body_test_get_path_insert()]))
        body_test_get_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])

        iter_test_btn = Button(master = get_req, text = 'Принять', command = create_get)
        iter_test_btn.grid(column = 2, row = 3, padx = [10, 20], pady = [50, 10])

        btn_insert_file = Button(master = get_req, text = 'Открыть', command = select_file)
        btn_insert_file.grid(column = 2, row = 2, padx = [10, 20], pady = [5, 5])

        def select_file():
            file_path = fd.askopenfilename()

            if file_path:          
                body_test_get_path.delete(0, 'end')
                body_test_get_path.insert(0, file_path)

                if len(file_path) > 0 and (body_test_get_path.get() != 'Укажите путь к файлу'):
                    body_test_get_path.configure(foreground = 'black', font = ('Arial', 11))
            
            else:
                pass

        def iter_test_get_entry_delete():
            if iter_test_get_entry.get() == '1':
                iter_test_get_entry.delete(0, 'end')
                iter_test_get_entry.configure(foreground = 'black', font = ('Arial', 11))

        def body_test_get_path_delete():
            if body_test_get_path.get() == self.file_name:
                body_test_get_path.delete(0, 'end')
                body_test_get_path.configure(foreground = 'black', font = ('Arial', 11))
            
            elif body_test_get_path.get() == 'Укажите путь к файлу':
                body_test_get_path.delete(0, 'end')
                body_test_get_path.configure(foreground = 'black', font = ('Arial', 11))

        def iter_test_get_entry_insert():
            if iter_test_get_entry.get() == '':
                iter_test_get_entry.insert(0, '1')
                iter_test_get_entry.configure(foreground = 'gray', font = 'Arial 11 italic')

        def body_test_get_path_insert():
            if (len(self.file_name) > 0) and body_test_get_path.get() == '':
                body_test_get_path.insert(0, self.file_name)
                body_test_get_path.configure(foreground = 'gray', font = 'Arial 11 italic')

            elif (len(self.file_name) == 0) and body_test_get_path.get() == '':
                body_test_get_path.insert(0, 'Укажите путь к файлу')
                body_test_get_path.configure(foreground = 'gray', font = 'Arial 11 italic')

# \\------------------ КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ GET ЗАПРОСОВ ------------------//