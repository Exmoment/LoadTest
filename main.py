from tkinter import *
from wigets import wiget_dontgenerate, create_window


def main_destroy():
    main_window.destroy()


main_window = Tk()
main_window.title('Редиска')
main_window.maxsize(800, 800)
main_window.minsize(400, 150)
start_title = Label(main_window, text = "У вас есть файлы конфигурации?", font = ("Arial", 18))
start_title.pack(padx = 10, pady = 10)
btn_yes = Button(main_window, text = 'Есть конфигурационные файлы', command = lambda:[main_destroy(), create_window(), wiget_dontgenerate()])
btn_yes.pack(fill = X, padx = 10, pady = [10, 10])
btn_no = Button(main_window, text = 'Нет конфигурационных файлов', command = lambda:[main_destroy(), create_window(), wiget_dontgenerate()])
btn_no.pack(fill = X, padx = 10, pady = [0, 10])

main_window.mainloop()