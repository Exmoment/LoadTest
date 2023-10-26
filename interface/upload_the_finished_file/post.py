from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from run_test import Choice_Type
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

        post_req = Frame(controller_widgets.window_yes, relief = FLAT)
        post_req.pack(pady = [5,    5])

        loadFileMenu = Menu(controller_widgets.window_yes)
        controller_widgets.window_yes.config(menu = loadFileMenu)
        loadFileMenu.add_command(label = 'Справка')

        body_test_post = Label(master = post_req, text = "Файл с конфигурацией:", font = ("Arial", 12))
        body_test_post.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        body_test_post_path = Entry(master = post_req, width = 25)
        body_test_post_path.insert(0, 'Укажите путь к файлу')
        body_test_post_path.configure(foreground = 'gray', font = 'Arial 11 italic')
        body_test_post_path.bind('<FocusIn>', (lambda args: [body_test_get_path_delete()]))
        body_test_post_path.bind('<FocusOut>', (lambda args: [body_test_get_path_insert()]))
        body_test_post_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])

        ammo_test = Label(master = post_req, text = "Файл запросов:", font = ("Arial", 12))
        ammo_test.grid(column = 0, row = 3, padx = [5, 5], pady = [5, 5], sticky = 'e')
        ammo_test_path = Entry(master = post_req, width = 25)
        ammo_test_path.insert(0, 'Укажите путь к файлу')
        ammo_test_path.configure(foreground = 'gray', font = 'Arial 11 italic')
        ammo_test_path.bind('<FocusIn>', (lambda args: [ammo_test_path_delete()]))
        ammo_test_path.bind('<FocusOut>', (lambda args: [ammo_test_path_insert()]))
        ammo_test_path.grid(column = 1, row = 3, padx = [5, 5], pady = [5, 5])

        back_btn = Button(master = post_req, text = 'Вернуться к выбору запросов', command = lambda:[post_req.destroy(), controller_widgets.widget_dontgenerate(), controller_widgets.window_yes.config(loadFileMenu.destroy())])
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