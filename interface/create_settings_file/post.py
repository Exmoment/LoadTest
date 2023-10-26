from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import scrolledtext
from run_test import Choice_Type
from config_generator import *
import interface.controller_widgets as controller_widgets


def create_post():
    if len(body_test_post_path.get()) > 0 and len(ammo_test_path.get()) > 0:

        if  ((iter_test_post_entry.get().isdigit()) > 0) and (int(iter_test_post_entry.get()) > 0):
            POST = Choice_Type('POST')
            POST.iterrationPOST = int(iter_test_post_entry.get())
            POST.pathBodyPOST = body_test_post_path.get()
            POST.pathAmmo = ammo_test_path.get()
            POST.POST()

        else:
            messagebox.showinfo('Error', 'Поле итераций POST запросов должно содержать натуральное число')

    else:
        messagebox.showinfo('Error', 'Все поля POST запросов должны быть заполнены')


def iinsert_file_post():
    file_name = fd.askopenfilename()
    body_test_post_path.insert(0, file_name)


def insert_file_ammo():
    file_name = fd.askopenfilename()
    ammo_test_path.insert(0, file_name)


# //----------------- КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ POST ЗАПРОСОВ ------------------\\

class Widget_POST_Requests:

    def __init__(self, name):
        self.name = name
        self.body_file_name = ''
        self.ammo_file_name = ''

    def POST(self):
        global iter_test_post_entry
        global ammo_test_path
        global body_test_post_path
        global post_req

        controller_widgets.start.destroy()

        def iter_test_get_entry_delete():
            if iter_test_post_entry.get() == '1':
                iter_test_post_entry.delete(0, 'end')
                iter_test_post_entry.configure(foreground = 'black', font = ('Arial', 11))

        def body_test_get_path_delete():
            if (body_test_post_path.get() == self.body_file_name) or (body_test_post_path.get() == 'Укажите путь к файлу'):
                body_test_post_path.delete(0, 'end')
                body_test_post_path.configure(foreground = 'black', font = ('Arial', 11))

        def ammo_test_path_delete():
            if (ammo_test_path.get() == self.ammo_file_name) or (ammo_test_path.get() == 'Укажите путь к файлу'):
                ammo_test_path.delete(0, 'end')
                ammo_test_path.configure(foreground = 'black', font = ('Arial', 11))

        def iter_test_get_entry_insert():
            if iter_test_post_entry.get() == '':
                iter_test_post_entry.insert(0, '1')
                iter_test_post_entry.configure(foreground = 'gray', font = 'Arial 11 italic')

        def body_test_get_path_insert():
            if (len(self.body_file_name) > 0) and body_test_post_path.get() == '':
                body_test_post_path.insert(0, self.body_file_name)
                body_test_post_path.configure(foreground = 'gray', font = 'Arial 11 italic')

            elif (len(self.body_file_name) == 0) and body_test_post_path.get() == '':
                body_test_post_path.insert(0, 'Укажите путь к файлу')
                body_test_post_path.configure(foreground = 'gray', font = 'Arial 11 italic')

        def ammo_test_path_insert():
            if (len(self.ammo_file_name) > 0) and ammo_test_path.get() == '':
                ammo_test_path.insert(0, self.ammo_file_name)
                ammo_test_path.configure(foreground = 'gray', font = 'Arial 11 italic')

            elif (len(self.ammo_file_name) == 0) and ammo_test_path.get() == '':
                ammo_test_path.insert(0, 'Укажите путь к файлу')
                ammo_test_path.configure(foreground = 'gray', font = 'Arial 11 italic')

        post_req = Frame(controller_widgets.window_no, relief = FLAT)
        post_req.pack(pady = [5, 5])

        loadFileMenu = Menu(controller_widgets.window_no)
        controller_widgets.window_no.config(menu = loadFileMenu)
        loadFileMenu.add_command(label = 'Справка')

        body_test_post = Label(master = post_req, text = 'Файл с конфигурацией', font = ("Arial", 12))
        body_test_post.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        body_test_post_path = Entry(master = post_req, width = 25)
        body_test_post_path.insert(0, self.body_file_name)
        body_test_post_path.configure(foreground = 'gray', font = 'Arial 11 italic')
        body_test_post_path.bind('<FocusIn>', (lambda args: [body_test_get_path_delete()]))
        body_test_post_path.bind('<FocusOut>', (lambda args: [body_test_get_path_insert()]))
        body_test_post_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])

        ammo_test = Label(master = post_req, text = 'Файл запросов', font = ("Arial", 12))
        ammo_test.grid(column = 0, row = 3, padx = [5, 5], pady = [5, 5], sticky = 'e')
        ammo_test_path = Entry(master = post_req, width = 25)
        ammo_test_path.insert(0, self.ammo_file_name)
        ammo_test_path.configure(foreground = 'gray', font = 'Arial 11 italic')
        ammo_test_path.bind('<FocusIn>', (lambda args: [ammo_test_path_delete()]))
        ammo_test_path.bind('<FocusOut>', (lambda args: [ammo_test_path_insert()]))
        ammo_test_path.grid(column = 1, row = 3, padx = [5, 5], pady = [5, 5])

        back_btn = Button(master = post_req, text = 'Вернуться к выбору запросов', command = lambda:[post_req.destroy(), controller_widgets.generate_files(), controller_widgets.window_no.config(loadFileMenu.destroy())])
        back_btn.grid(column = 1, row = 4, padx = [10, 20], pady = [50, 10])

        nameTestPOST = Label(master = post_req, text = "--- POST ---", font = ("Arial", 16), foreground = 'gray')
        nameTestPOST.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 30])

        iter_test = Label(master = post_req, text = "Количество итераций тестов:", font = ("Arial", 12))
        iter_test.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iter_test_post_entry = Entry(master = post_req, width = 25)
        iter_test_post_entry.insert(0, '1')
        iter_test_post_entry.configure(foreground = 'gray', font = 'Arial 11 italic')
        iter_test_post_entry.bind('<FocusIn>', (lambda args: [iter_test_get_entry_delete()]))
        iter_test_post_entry.bind('<FocusOut>', (lambda args: [iter_test_get_entry_insert()]))
        iter_test_post_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])

        iterTest_btn = Button(master = post_req, text = 'Принять', command = create_post)
        iterTest_btn.grid(column = 2, row = 4, padx = [10, 20], pady = [50, 10])

        btn_insertFile = Button(master = post_req, text = 'Открыть', command = iinsert_file_post)
        btn_insertFile.grid(column = 2, row = 2, padx = [10, 20], pady = [5, 5])
        btn1_insertFile = Button(master = post_req, text = 'Открыть', command = insert_file_ammo)
        btn1_insertFile.grid(column = 2, row = 3, padx = [10, 20], pady = [5, 5])

# \\----------------- КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ POST ЗАПРОСОВ ------------------//
# --------------------------------------------------------------------------------------------------
# //--------------------- КОД ВИДЖЕТА ГЕНЕРАТОРА КОНФИГУРАЦИЙ POST ЗАПРОСОВ -----------------------\\

class Widget_Generator_POST:

    def __init__(self, name):
        self.name = name
        self.create_token = ''

    def generator_post(self):
        global generate_post

        generate_post = Frame(controller_widgets.window_no, relief = FLAT)
        generate_post.pack(pady = [5, 5])

        generator_get_name = Label(master = generate_post, text = '--- POST query customization generator ---', font = ('Arial', 16), foreground = 'gray')
        generator_get_name.grid(columnspan = 3, row = 0, pady = [5, 5])

        labels = ['Хост сайта:', 'Порт:', 'Файл с запросами:', 'Количество экземпляров:',
                  'Параметры нагрузки:', 'Имя теста:', 'Вывод в консоли',
                  'Загрузить и обработать результат']
        
        y = 1
        for a in labels:
            enter_name = Label(master = generate_post, text = a, font = ('Arial', 12))
            enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [5, 5], sticky = 'se')
            if a == 'Порт:':
                enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [5, 5], sticky = 'e')
            if a == 'Хост сайта:':
                enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [5, 15], sticky = 'se')
            if a == 'User agent:':
                enter_name.grid(column = 0, row = y, padx = [5, 5], pady = [15, 5], sticky = 'se')
            y += 1

        def created_file_for_post():
            created_file = load_POST('Load_POST')
            created_file.host = host_entry.get()
            created_file.port = port_entry.get()
            if port_entry.get() == '443':
                created_file.ssl = 'true'
            elif port_entry.get() == '80':
                created_file.ssl = 'false'
            created_file.ammo_file = request_file_entry.get()
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
            next_widget = Widget_POST_Requests('next_widget')
            next_widget.body_file_name = name_test_entry.get()+'.yaml'
            next_widget.ammo_file_name = request_file_entry.get()
            next_widget.POST()

        def placeholder_host_entry_delete():
            if host_entry.get() == 'Например: example.com':
                host_entry.delete(0, 'end')
                host_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_port_entry_delete():
            if port_entry.get() == 'Введите или выберите значение':
                port_entry.delete(0, 'end')
                port_entry.configure(foreground = 'black', font = ('Arial', 11))

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

        def placeholder_request_file_delete():
            if request_file_entry.get() == 'Сгенерируйте или укажите путь к файлу':
                request_file_entry.delete(0, 'end')
                request_file_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_quantity_threads_entry_delete():
            if quantity_threads_entry.get() == '1000':
                quantity_threads_entry.delete(0, 'end')
                quantity_threads_entry.configure(foreground = 'black', font = ('Arial', 11))
        
        def placeholder_load_params_delete():
            if load_params_entry.get() == 'line(1, 100, 5m) const(50,2m)':
                load_params_entry.delete(0, 'end')
                load_params_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_name_delete():            
            if name_test_entry.get() == 'Введите название теста':
                name_test_entry.delete(0, 'end')
                name_test_entry.configure(foreground = 'black', font = ('Arial', 11))

        def placeholder_host_entry_insert():
            if host_entry.get() == '':
                host_entry.insert(0, 'Например: example.com')
                host_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

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

        def placeholder_request_file_insert():
            if request_file_entry.get() == '':
                request_file_entry.insert(0, 'Сгенерируйте или укажите путь к файлу')
                request_file_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        def placeholder_quantity_threads_entry_insert():
            if quantity_threads_entry.get() == '':
                quantity_threads_entry.insert(0, '1000')
                quantity_threads_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        def placeholder_load_params_insert():
            if load_params_entry.get() == '':
                load_params_entry.insert(0, 'line(1, 100, 5m) const(50,2m)')
                load_params_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        def placeholder_name_insert():
            if name_test_entry.get() == '':
                name_test_entry.insert(0, 'Введите название теста')
                name_test_entry.configure(foreground = 'gray', font = ('Arial 11 italic'))

        host_entry = Entry(master = generate_post, width = 35)
        host_entry.insert(0, 'Например: example.com')
        host_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        host_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 15])
        host_entry.bind('<FocusIn>', (lambda args: [placeholder_host_entry_delete()]))
        host_entry.bind('<FocusOut>', (lambda args: [placeholder_host_entry_insert()]))

        port_entry = Entry(master = generate_post, width = 35)
        port_entry.insert(0, 'Введите или выберите значение')
        port_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        port_entry.bind('<FocusIn>', (lambda args: [placeholder_port_entry_delete()]))
        port_entry.bind('<FocusOut>', (lambda args: [placeholder_port_entry_insert()]))
        port_entry.grid(column = 1, row = 2, sticky = N, padx = [5, 5], pady = [5, 25])
        selected_port = StringVar()
        selected_port.set('')
        port_radiobutton_443 = Radiobutton(master = generate_post, text = 'https://', command = selected_https, value = '443', variable = selected_port)
        port_radiobutton_443.grid(column = 1, row = 2, sticky = SW, padx = [15, 15])
        port_radiobutton_80 = Radiobutton(master = generate_post, text = 'http://', command = selected_http, value = '80', variable = selected_port)
        port_radiobutton_80.grid(column = 1, row = 2, sticky = S, padx = [25, 15])

        request_file_entry = Entry(master = generate_post, width = 35)
        request_file_entry.insert(0, 'Сгенерируйте или укажите путь к файлу')
        request_file_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        request_file_entry.bind('<FocusIn>', (lambda args: [placeholder_request_file_delete()]))
        request_file_entry.bind('<FocusOut>', (lambda args: [placeholder_request_file_insert()]))
        request_file_entry.grid(column = 1, row = 3, padx = [5, 5], pady = [15, 5])

        quantity_threads_entry = Entry(master = generate_post, width = 35)
        quantity_threads_entry.insert(0, '1000')
        quantity_threads_entry.configure(foreground = 'gray')
        quantity_threads_entry.grid(column = 1, row = 4, padx = [5, 5], pady = [5, 5])
        quantity_threads_entry.bind('<FocusIn>', (lambda args: [placeholder_quantity_threads_entry_delete()]))
        quantity_threads_entry.bind('<FocusOut>', (lambda args: [placeholder_quantity_threads_entry_insert()]))

        load_params_entry = Entry(master = generate_post, width = 35)
        load_params_entry.insert(0, 'line(1, 100, 5m) const(50,2m)')
        load_params_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        load_params_entry.grid(column = 1, row = 5, padx = [5, 5], pady = [5, 5])
        load_params_entry.bind('<FocusIn>', (lambda args: [placeholder_load_params_delete()]))
        load_params_entry.bind('<FocusOut>', (lambda args: [placeholder_load_params_insert()]))

        name_test_entry = Entry(master = generate_post, width = 35)
        name_test_entry.insert(0, 'Введите название теста')
        name_test_entry.configure(foreground = 'gray', font = 'helvetica 11 italic')
        name_test_entry.grid(column = 1, row = 6, padx = [5, 5], pady = [5, 5])
        name_test_entry.bind('<FocusIn>', (lambda args: [placeholder_name_delete()]))
        name_test_entry.bind('<FocusOut>', (lambda args: [placeholder_name_insert()]))

        selected_console = StringVar()
        selected_console.set('')
        console_radiobutton_on = Radiobutton(master = generate_post, text = 'включить', value = 'true', variable = selected_console)
        console_radiobutton_on.grid(column = 1, row = 7, sticky = W, padx = [15, 5])
        console_radiobutton_off = Radiobutton(master = generate_post, text = 'отключить', value = 'false', variable = selected_console)
        console_radiobutton_off.grid(column = 1, row = 7, padx = [55, 5])

        selected_overload = StringVar()
        selected_overload.set('')
        overload_radiobutton_on = Radiobutton(master = generate_post, text = 'включить', value = 'true', variable = selected_overload)
        overload_radiobutton_on.grid(column = 1, row = 8, sticky = W, padx = [15, 5])
        overload_radiobutton_off = Radiobutton(master = generate_post, text = 'отключить', value = 'false', variable = selected_overload)
        overload_radiobutton_off.grid(column = 1, row = 8, padx = [55, 5])

        save_btn = Button(master = generate_post, text = 'Создать файл с конфигурацией', command = created_file_for_post)
        save_btn.grid(columnspan = 3, row = 9, padx = [10, 10], pady = [10, 10], ipadx = 50)
        select_btn = Button(master = generate_post, text = 'Принять', command = lambda: [created_file_for_post(), create_next_widget(), generate_post.destroy()])
        select_btn.grid(column = 2, row = 10, padx = [10, 10], pady = [20, 10])
        back_btn =Button(master = generate_post, text = 'Вернуться к выбору запросов', command = lambda:[generate_post.destroy(), controller_widgets.widget_generate()])
        back_btn.grid(column = 1, row = 10, padx = [10, 10], pady = [20, 10])

# \\---------------------- КОД ВИДЖЕТА ГЕНЕРАТОРА КОНФИГУРАЦИЙ POST ЗАПРОСОВ ----------------------//