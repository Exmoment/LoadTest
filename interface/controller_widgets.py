from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from .create_settings_file.get import *
from .create_settings_file.post import *
from .create_settings_file.get_and_post import *
from .upload_the_finished_file.get import *
from .upload_the_finished_file.post import *
from .upload_the_finished_file.get_and_post import *



# //--------------------- ВИДЖЕТ ДЛЯ РАБОТЫ С НАПИСАННЫМИ ЗАРАНЕЕ КОНФИГАМИ -----------------------\\

def clicked_yes():

    if 'GET and POST' in choice_type.get():
        create_widget = Widget_GET_and_POST_Requests('create_widget')
        create_widget.GETandPOST()

    elif 'POST' in choice_type.get():
        create_widget = Widget_POST_Requests('create_widget')
        create_widget.POST()

    elif 'GET' in choice_type.get():
        create_widget = Widget_GET_Requests('create_widget')
        create_widget.GET()

    else:
        messagebox.showinfo('Ошибка ввода', 'Не выбран тип запросов или введен неверный формат, попробуйте еще раз')


def widget_dontgenerate():
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

    widget_dontgenerate()

    window_yes.mainloop()

# \\------------------- КОНЕЦ ВИДЖЕТА ДЛЯ РАБОТЫ С НАПИСАННЫМИ ЗАРАНЕЕ КОНФИГАМИ ------------------//
# ---------------------------------------------------------------------------------------------------
# //---------------- ВИДЖЕТ ДЛЯ ГЕНЕРАЦИИ КОНФИГУРАЦИОННЫХ ФАЙЛОВ И РАБОТЫ С НИМИ -----------------\\


def generate_files():

    if ('yes' in selected.get()) or ('no' in selected.get()):

        if 'GET and POST' in typeREQ:
            choice_auth.destroy()

            if 'yes' in selected.get():

                print(selected.get())
                #config_generator.generateGET()
                #config_generator.generateAmmo()
                #config_generator.generatePOST()

        elif 'POST' in typeREQ:
            choice_auth.destroy()

            if 'yes' in selected.get():
                create_widget = Widget_Generator_POST('create_widget')
                create_widget.create_token = selected.get()
                create_widget.generator_post()
                
            elif 'no' in selected.get():
                create_widget = Widget_Generator_POST('create_widget')
                create_widget.create_token = selected.get()
                create_widget.generator_post()

        elif 'GET' in typeREQ:
            choice_auth.destroy()

            if 'yes' in selected.get(): 
                create_widget = Widget_Generator_GET('create_widget')
                create_widget.create_token = selected.get()
                create_widget.generator_get()

            elif 'no' in selected.get(): 
                create_widget = Widget_Generator_GET('create_widget')
                create_widget.create_token = selected.get()
                create_widget.generator_get()

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
        
        btn = Button(master = choice_auth, text = 'Выбрать', command = generate_files)
        btn.grid(columnspan = 2, row = 2, padx = 5, pady = [25, 5])
        back_btn = Button(master = choice_auth, text = 'Назад', command = lambda:[choice_auth.destroy(), widget_generate()])
        back_btn.grid(columnspan = 2, row = 3, padx = 5, pady = 5)

    else:
        messagebox.showinfo('Ошибка ввода', 'Не выбран тип запросов или введен неверный формат, попробуйте еще раз')


def widget_generate():
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

    widget_generate()

    window_no.mainloop()

# \\------------- КОНЕЦ ВИДЖЕТА ДЛЯ ГЕНЕРАЦИИ КОНФИГУРАЦИОННЫХ ФАЙЛОВ И РАБОТЫ С НИМИ -------------//


def create_main():
    global main_window

    main_window = Tk()
    main_window.title('Редиска')
    main_window.maxsize(800, 800)
    main_window.minsize(400, 150)

    start_title = Label(main_window, text = "У вас есть файлы конфигурации?", font = ("Arial", 18))
    start_title.pack(padx = 10, pady = 10)

    btn_yes = Button(main_window, text = 'Есть конфигурационные файлы', command = lambda:[main_window.destroy(), create_present(), widget_dontgenerate()])
    btn_yes.pack(fill = X, padx = 10, pady = [10, 10])

    btn_no = Button(main_window, text = 'Нет конфигурационных файлов', command = lambda:[main_window.destroy(), create_absent(), widget_generate()])
    btn_no.pack(fill = X, padx = 10, pady = [0, 10])

    main_window.mainloop()