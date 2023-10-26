from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from run_test import Choice_Type
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

        get_req = Frame(controller_widgets.window_yes, relief = FLAT)
        get_req.pack(pady = [5, 5])

        load_file_menu = Menu(controller_widgets.window_yes)
        controller_widgets.window_yes.config(menu = load_file_menu)
        load_file_menu.add_command(label = 'Справка')

        back_btn = Button(master = get_req, text = 'Вернуться к выбору запросов', command = lambda:[get_req.destroy(), controller_widgets.widget_dontgenerate(), 
                                                                                                    controller_widgets.window_yes.config(load_file_menu.destroy())])
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

# \\------------------ КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ GET ЗАПРОСОВ ------------------//