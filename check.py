import os
import time
from shell_command import run
    
# Не забыть исправить все условия с заменой файлов с ренейма из рабочей директории на копирование и удаление из любой папки

class LoadPOSTTesting:

    def __init__(self, name):
        self.name = name
        self.path = ''
        self.path_2 = ''

    def ammo_File(self):
        with open(self.path, 'r') as ammo:                               # создаем файл в директории программы
            ammo_text = ammo.read()                                      # путем чтения и записи указанного пользователем
        with open('ammo.json', 'w') as ammo:
            ammo.write(ammo_text)

    def POST_File(self):
        with open(self.path_2, 'r') as load:
            load_config = load.read()
        with open('load.yaml', 'w') as load:
            load.write(load_config)

    def CasePOST(self):
        text_in_get = 'uris:'
        text_in_post = 'ammo_type: phantom'

        if os.path.exists(self.path_2) & os.path.exists('load.yaml'):    # self.path_2 передает текущий путь до тела танка, вызываемого в объекте
            file = open('load.yaml', 'r')                                # открываем файл load.yaml
            text = file.read()

            if text_in_post in text:                                             # действия, выполняемые в случае, если load.yaml в рабочей папке оказался телом танка для POST запросов
                print('Checking and preparing files for sending POST requests')
                time.sleep(5)
                #os.rename('load.yaml', 'OLD_POST_load.yaml')
                self.POST_File()
                self.ammo_File()
                os.system(run)
                os.rename('ammo.txt', self.path)
                os.rename('load.yaml', self.path_2)
                print('Scenario complete')
                time.sleep(5)

            elif text_in_get in text:                                            # действия, выполняемые в случае, если load.yaml в рабочей папке оказался телом танка для GET запросов
                print('Replacing a tank with GET requests for a tank with POST requests')
                time.sleep(5)
                os.rename('load.yaml', 'OLD_GET_load.yaml')
                self.POST_File()
                self.ammo_File()
                os.system(run)
                os.rename('ammo.txt', self.path)
                os.rename('load.yaml', self.path_2)
                print('Scenario complete')
                time.sleep(5)

        elif os.path.exists(self.path_2):                                 # запуск действий, если в рабочей папке не было файла load.yaml и был передан путь к конфигурации тестирования
            print('Preparing files for sending POST requests')
            time.sleep(5)
            self.POST_File()
            self.ammo_File()
            os.system(run)
            os.rename('ammo.txt', self.path)
            os.rename('load.yaml', self.path_2)
            print('Scenario complete')
            time.sleep(5)

        elif os.path.exists('load.yaml'):                                  # запуск проверки, если в рабочей папке был только load.yaml
            file = open('load.yaml', 'r')                                  # открываем файл load.yaml
            text = file.read()

            if text_in_post in text:                                               # действия, выполняемые в случае, если load.yaml оказался телом танка для POST запросов
                print('Checking and preparing files for sending POST requests')
                time.sleep(5)
                os.rename('load.yaml', 'OLD_POST_load.yaml')
                self.POST_File()
                self.ammo_File()
                os.system(run)
                os.rename('ammo.txt', self.path)
                os.rename('load.yaml', self.path_2)
                print('Scenario complete')
                time.sleep(5)

            elif text_in_get in text:                                              # действия, выполняемые в случае, если load.yaml оказался телом танка для GET запросов
                print('Replacing a tank with GET requests for a tank with POST requests')
                time.sleep(5)
                os.rename('load.yaml', 'OLD_GET_load.yaml')
                self.POST_File()
                self.ammo_File()
                os.system(run)
                os.rename('ammo.txt', self.path)
                os.rename('load.yaml', self.path_2)
                print('Scenario complete')
                time.sleep(5)

            else:
                print('File(s) to run testing missing')
                exit(0)      

        else:
            print('File(s) to run testing POST requests are missing')
            exit(0)


class LoadGETTesting:
    
    def __init__(self, name):
        self.name = name
        self.path = ''

    def GET_File(self):
        with open(self.path, 'r') as load:                                  # создаем файл в директории программы
            load_config = load.read()                                       # путем чтения и записи указанного пользователем
        with open('load.yaml', 'w') as load:
            load.write(load_config)

    def CaseGET(self):
        text_in_get = 'uris:'
        text_in_post = 'ammo_type: phantom'

        if os.path.exists(self.path) & os.path.exists('load.yaml'):          # self.path передает текущий путь до тела танка, вызываемого в объекте
            file = open('load.yaml', 'r')                                    # открываем файл load.yaml
            text = file.read()

            if text_in_post in text:                                                 # действия, выполняемые в случае, если load.yaml оказался телом танка для POST запросов
                print('Checking files for sending GET requests')
                print('Changing a tank with POST requests to tank GET requests')
                time.sleep(5)
                os.rename('load.yaml', 'OLD_POST_load.yaml')
                self.GET_File()
                os.system(run)
                os.rename('load.yaml', self.path)
                print('Scenario complete')
                time.sleep(5)

            elif text_in_get in text:                                                 # действия, выполняемые в случае, если load.yaml оказался телом танка для GET запросов
                print('Checking files for sending GET requests')
                time.sleep(5)
                os.rename('load.yaml', 'OLD_GET_load.yaml')
                os.system(run)
                os.rename('load.yaml', self.path)
                print('Scenario complete')
                time.sleep(5)

            else:
                print('File(s) to run testing missing')
                exit(0)

        elif os.path.exists(self.path):                                        # запуск действий, если был только один файл, путь к которому передается в объекте
            print('Preparing files for sending GET requests')
            time.sleep(5)
            self.GET_File()
            os.system(run)
            print('Scenario complete')
            os.rename('load.yaml', self.path)
            time.sleep(5)

        elif os.path.exists('load.yaml'):                                      # запуск проверки, если в рабочей папке был только load.yaml
            file = open('load.yaml', 'r')                                      # открываем файл load.yaml
            text = file.read()

            if text_in_get in text:                                                    # действия, выполняемые в случае, если load.yaml оказался телом танка для GET запросов
                print('Checking files for sending GET requests')
                time.sleep(5)
                os.rename('load.yaml', 'OLD_GET_load.yaml')
                self.GET_File()
                os.system(run)
                os.rename('load.yaml', self.path)
                print('Scenario complete')
                time.sleep(5)

            elif text_in_post in text:                                                 # действия, выполняемые в случае, если load.yaml оказался телом танка для POST запросов
                print('Checking files for sending GET requests')
                print('Changing a tank with POST requests to tank GET requests')
                time.sleep(5)
                os.rename('load.yaml', 'OLD_POST_load.yaml')
                self.GET_File()
                os.system(run)
                os.rename('load.yaml', self.path)
                print('Scenario complete')
                time.sleep(5)

            else:
                print('File(s) to run testing missing')
                exit(0)

        else:
            print('File(s) to run testing GET requests missing')
            exit(0)