import os
import time
import re
from errors.phantom.errors import *
from shell_command import run
from datetime import datetime
'''
class Check_POST:

    def __init__(self, name):
        self.name = name
        self.path_to_body = ''
        self.path_to_ammo = ''
        self.name_ammo_in_body = ''

    def ammo_file(self):
        with open(self.path_to_ammo, 'r') as request:                                         # создаем файл в директории программы
            request_text = request.read()
        slash_pos = self.path_to_ammo.rfind("/")
        name_ammo = self.path_to_ammo[slash_pos+1:]
        with open(name_ammo, 'w') as request:                                                 # путем чтения и записи указанного пользователем
            request.write(request_text)

    def configuration_file(self):
        with open(self.path_to_body, 'r') as configuration:
            configuration_text = configuration.read()
        with open('load.yaml', 'w') as configuration:
            configuration.write(configuration_text)

    def move_file_after_test(self, current_time, now_time):
        slash_pos = self.path_to_body.rfind("/")
        name_body = self.path_to_body[slash_pos+1:]
        slash_pos = self.path_to_ammo.rfind("/")
        name_ammo = self.path_to_ammo[slash_pos+1:]
        os.rename('load.yaml', 'OLD_TESTS/{curent_time}/OLD_{now_time}_{name_body}')
        os.rename(name_ammo, 'OLD_TESTS/{current_time}/OLD_{now_time}_{name_ammo}')

    def start_checking(self):
        type_generator_load = 'phantom:'
        type_get = 'uris:'
        type_post = 'ammo_type: phantom'

        if os.path.exists(self.path_to_body) and os.path.exists(self.path_to_ammo):
            
            if (self.path_to_body == 'load.yaml') and (self.path_to_ammo == 'ammo.json'):
                self.if_standart_names(type_generator_load, type_post)

            elif (self.path_to_body != 'load.yaml') and (self.path_to_ammo != "ammo.json"):
                file_body = open(self.path_to_body, 'r')
                text_body = file_body.read()
                file_ammo = open(self.path_to_ammo, 'r')
                text_body = file_ammo.read()
                print('Checking files for sending POST requests')
                time.sleep(5)

                if (type_generator_load in text_body) and (type_post in text_body) and (self.path_to_ammo in text_body):
                    check_or_create_dir_for_old()

                    if os.path.exists('load.yaml'):
                        os.remove('load.yaml')
                    else:
                        pass

                    if os.path.exists('ammo.json'):
                        os.remove('ammo.json')
                    else:
                        pass
# Разобраться с неймингом файлов внутри конфига и в коде!!!
                    check_or_create_dir_for_old()
                    self.configuration_file()
                    self.ammo_file()
                    print('File is ready')
                    time.sleep(5)
                    current_time = datetime.now().strftime('%Y-%m-%d')
                    now_time = datetime.now().strftime('%H:%M')
                    os.system(run)
                    self.move_file_after_test(current_time, now_time)
                    print('Scenario complete')
                    time.sleep(5)

                elif (type_generator_load in text_body) and (type_post in text_body) and (not self.path_to_ammo in text_body):
                    phantom_cant_search_name_ammo_in_body()

                elif (not type_generator_load in text_body) and (not type_post in text_body) and (not self.path_to_ammo in text_body):
                    phantom_not_post_and_not_ammo()

                elif (not type_generator_load in text_body) or (not type_post in text_body) and (self.path_to_ammo in text_body):
                    phantom_not_post()

        else:
            phantom_cant_search_post()
                    
    def if_standart_names(self, type_generator_load, type_post):
        file_body = open(self.path_to_body, 'r')
        text_body = file_body.read()
        file_ammo = open(self.path_to_ammo, 'r')
        text_body = file_ammo.read()
        print('Checking files for sending POST requests')
        time.sleep(5)

        if (type_generator_load in text_body) and (type_post in text_body) and (self.path_to_ammo in text_body):
            check_or_create_dir_for_old()
            self.configuration_file()
            self.ammo_file()
            print('File is ready')
            time.sleep(5)
            current_time = datetime.now().strftime('%Y-%m-%d')
            now_time = datetime.now().strftime('%H:%M')
            os.system(run)
            self.move_file_after_test(current_time, now_time)
            print('Scenario complete')
            time.sleep(5)

        elif (type_generator_load in text_body) and (type_post in text_body) and (not self.path_to_ammo in text_body):
            phantom_cant_search_name_ammo_in_body()

        elif (not type_generator_load in text_body) and (not type_post in text_body) and (not self.path_to_ammo in text_body):
            phantom_not_post_and_not_ammo()

        elif (not type_generator_load in text_body) or (not type_post in text_body) and (self.path_to_ammo in text_body):
            phantom_not_post()

    def if_not_standart_names(self, type_generator_load, type_post):
        file_body = open(self.path_to_body, 'r')
        text_body = file_body.read()
        file_ammo = open(self.path_to_ammo, 'r')
        text_body = file_ammo.read()
        print('Checking files for sending POST requests')
        time.sleep(5)


        self.configuration_file()
        self.ammo_file()
        print('File is ready')
        time.sleep(5)

def check_or_create_dir_for_old():
    current_time = datetime.now().strftime('%Y-%m-%d')

    if os.path.exists('OLD_TESTS') and os.path.isdir('OLD_TESTS'):            
        if os.path.exists('OLD_TESTS/{current_time}') and os.path.isdir('OLD_TESTS/{current_time}'):
            pass

    else:
        os.makedirs('OLD_TESTS')
        
        if os.path.exists('OLD_TESTS/{current_time}') and os.path.isdir('OLD_TESTS/{current_time}'):
            pass
        else:
            os.makedirs('OLD_TESTS/{current_time}')

# Не забыть исправить все условия с заменой файлов с ренейма из рабочей директории на копирование и удаление из любой папки
'''
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