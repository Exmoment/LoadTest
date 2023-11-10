from tkinter import messagebox


def phantom_cant_search_post():
    messagebox.showinfo('Error', 'Один или несколько файлов не существуют по указанному пути')

def phantom_cant_search_name_ammo_in_body():
    messagebox.showinfo('Error', 'В файле конфигурации неверно указано имя файла с запросом')

def phantom_not_post_and_not_ammo():
    messagebox.showinfo('Error', 'В файле конфигурации отсутствуют: генератор нагрзуки(phantom), тип запррсов, неверно указано название файла с запросом(ами)')

def phantom_not_post():
    messagebox.showinfo('Error', 'В файле конфигурации не указан генератор нагрузки или тип запросов')