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


def create_get():
    if len(body_test_get_path.get()) > 0:

        if  ((iter_test_get_entry.get().isdigit()) > 0) and (int(iter_test_get_entry.get()) > 0):
            GET = Choice_Type('GET')
            GET.iterrationGET = int(iter_test_get_entry.get())
            GET.pathBodyGET = body_test_get_path.get()

            GET.GET()

        else:
            messagebox.showinfo('Error', 'Поле итераций GET запросов должно содержать натуральное число')

    else:
        messagebox.showinfo('Error', 'Все поля GET запросов должны быть заполнены')

def insert_file_get():
    file_name = fd.askopenfilename()
    body_test_get_path.insert(0, file_name)


def iinsert_file_post():
    file_name = fd.askopenfilename()
    body_test_post_path.insert(0, file_name)


def insert_file_ammo():
    file_name = fd.askopenfilename()
    ammo_test_path.insert(0, file_name)


# //-------------- КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ GET И POST ЗАПРОСОВ ---------------\\

class Widget_GET_and_POST_Requests:

    def __init__(self, name):
        self.name = name
        self.btnType = ''

    def GETandPOST(self):
        global iter_test_post_entry
        global iter_test_get_entry
        global ammo_test_path
        global body_test_post_path
        global body_test_get_path
        global post_req
        global GETreq

        controller_widgets.start.destroy()

        post_req = Frame(controller_widgets.window_yes, relief = FLAT)
        post_req.pack(padx = [5, 5])
        GETreq = Frame(controller_widgets.window_yes, relief = FLAT)
        GETreq.pack(padx = [5, 5])

        loadFileMenu = Menu(controller_widgets.window_yes)
        controller_widgets.window_yes.config(menu = loadFileMenu)
        loadFileMenu.add_command(label = 'Справка')

        nameTestPOST = Label(master = post_req, text = "--- POST ---", font = ("Arial", 16), foreground = 'gray')
        nameTestPOST.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [5, 30])

        iterTest = Label(master = post_req, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iter_test_post_entry = Entry(master = post_req, width = 25)
        iter_test_post_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5])

        bodyTestPOST = Label(master = post_req, text = "Файл с конфигурацией:", font = ("Arial", 12))
        bodyTestPOST.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        body_test_post_path = Entry(master = post_req, width = 25)
        body_test_post_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5])

        ammoTest = Label(master = post_req, text = "Файл запросов:", font = ("Arial", 12))
        ammoTest.grid(column = 0, row = 3, padx = [5, 5], pady = [5, 5], sticky = 'e')
        ammo_test_path = Entry(master = post_req, width = 25)
        ammo_test_path.grid(column = 1, row = 3, padx = [5, 5], pady = [5, 5])

        nameTestGET = Label(master = GETreq, text = "--- GET ---", font = ("Arial", 16), foreground = 'gray')
        nameTestGET.grid(columnspan = 3, row = 0, padx = [5, 5], pady = [25, 30])

        iterTest = Label(master = GETreq, text = "Количество итераций тестов:", font = ("Arial", 12))
        iterTest.grid(column = 0, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'e')
        iter_test_get_entry = Entry(master = GETreq, width = 25)
        iter_test_get_entry.grid(column = 1, row = 1, padx = [5, 5], pady = [5, 5], sticky = 'w')

        bodyTestGET = Label(master = GETreq, text = "Файл с конфигурацией:", font = ("Arial", 12))
        bodyTestGET.grid(column = 0, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'e')
        body_test_get_path = Entry(master = GETreq, width = 25)
        body_test_get_path.grid(column = 1, row = 2, padx = [5, 5], pady = [5, 5], sticky = 'w')

        iterTest_btn = Button(master = GETreq, text = 'Принять', command = lambda:[create_get(), create_post()])
        iterTest_btn.grid(column = 2, row = 3, padx = [10, 20], pady = [50, 10])

        back_btn = Button(master = GETreq, text = 'Вернуться к выбору запросов', command = lambda:[GETreq.destroy(), post_req.destroy(), controller_widgets.widget_dontgenerate(), controller_widgets.window_yes.config(loadFileMenu.destroy())])
        back_btn.grid(column = 1, row = 3, padx = [10, 20], pady = [50, 10])

        btn_insertFile = Button(master = post_req, text = 'Открыть', command = iinsert_file_post)
        btn_insertFile.grid(column = 2, row = 2, padx = [44, 20], pady = [5, 5])
        btn1_insertFile = Button(master = post_req, text = 'Открыть', command = insert_file_ammo)
        btn1_insertFile.grid(column = 2, row = 3, padx = [44, 20], pady = [5, 5])
        btn2_insertFile = Button(master = GETreq, text = 'Открыть', command = insert_file_get)
        btn2_insertFile.grid(column = 2, row = 2, padx = [10, 20], pady = [5, 5])

# \\-------------- КОД ВИДЖЕТА ДЛЯ ЗАГРУЗКИ ФАЙЛОВ КОНФИГУРАЦИИ GET И POST ЗАПРОСОВ ---------------//