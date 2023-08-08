from tkinter import *
from objects import objects

'''
def clicked():
    text.configure(text = '123')
        
#    objects.objects
'''

window = Tk()
window.title("Тест")
window.geometry('350x100')
text = Label(window, text = "Редиска!", font = ("Arial", 36))
#text.grid(row = 0, column = 0)
text.pack()
btn = Button(window, text = "Запуск программы", command = objects)
btn.pack()



window.mainloop()