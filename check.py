import os
import time
from shell_command import run
    

class LoadPOSTTesting:

    def __init__(self, name):
        self.name = name
        self.path = ''
        self.path_2 = ''
    
    def CasePOST(self):
        GET = 'uris:'
        POST = 'ammo_type: phantom'

        if os.path.exists(self.path_2) & os.path.exists('load.yaml'): # self.path передает текущий путь до тела танка, вызываемого в объекте
            file = open('load.yaml', 'r') # открываем файл load.yaml
            text = file.read()

            if POST in text: # действия, выполняемые в случае, если load.yaml оказался телом танка для POST запросов
                print('Checking and preparing files for sending POST requests')
                time.sleep(5)
                os.rename(self.path, 'ammo.txt')
                os.system(run)
                os.rename('ammo.txt', self.path)
                os.rename('load.yaml', self.path_2)
                print('Scenario complete')
                time.sleep(5)

            elif GET in text: # действия, выполняемые в случае, если load.yaml оказался телом танка для GET запросов
                os.rename('load.yaml', 'GET_запросы.yaml')
                print('Replacing a tank with GET requests for a tank with POST requests')
                time.sleep(5)
                os.rename(self.path, 'ammo.txt')
                os.rename(self.path_2, 'load.yaml')
                os.system(run)
                os.rename('ammo.txt', self.path)
                os.rename('load.yaml', self.path_2)
                print('Scenario complete')
                time.sleep(5)

        elif os.path.exists(self.path_2): # запуск действий, если в рабочей папке был только один файл, путь к которому передается в объекте
            print('Preparing files for sending POST requests')
            time.sleep(5)
            os.rename(self.path, 'ammo.txt')
            os.rename(self.path_2, 'load.yaml')
            os.system(run)
            os.rename('ammo.txt', self.path)
            os.rename('load.yaml', self.path_2)
            print('Scenario complete')
            time.sleep(5)

        elif os.path.exists('load.yaml'): # запуск проверки, если в рабочей папке был только load.yaml
            file = open('load.yaml', 'r') # открываем файл load.yaml
            text = file.read()

            if POST in text: # действия, выполняемые в случае, если load.yaml оказался телом танка для POST запросов
                print('Checking and preparing files for sending POST requests')
                time.sleep(5)
                os.rename(self.path, 'ammo.txt')
                os.system(run)
                os.rename('ammo.txt', self.path)
                os.rename('load.yaml', self.path_2)
                print('Scenario complete')
                time.sleep(5)

            elif GET in text: # действия, выполняемые в случае, если load.yaml оказался телом танка для GET запросов
                os.rename('load.yaml', 'GET_запросы.yaml')
                print('Replacing a tank with GET requests for a tank with POST requests')
                time.sleep(5)
                os.rename(self.path, 'ammo.txt')
                os.rename(self.path_2, 'load.yaml')
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

    def CaseGET(self):
        GET = 'uris:'
        POST = 'ammo_type: phantom'

        if os.path.exists(self.path) & os.path.exists('load.yaml'): # self.path передает текущий путь до тела танка, вызываемого в объекте
            file = open('load.yaml', 'r') # открываем файл load.yaml
            text = file.read()

            if POST in text: # действия, выполняемые в случае, если load.yaml оказался телом танка для POST запросов
                print('Checking files for sending GET requests')
                print('Changing a tank with POST requests to tank GET requests')
                os.rename('load.yaml', 'POST_запросы.yaml')
                time.sleep(5)
                os.rename(self.path, 'load.yaml')
                os.system(run)
                os.rename('load.yaml', self.path)
                print('Scenario complete')
                time.sleep(5)

            elif GET in text: # действия, выполняемые в случае, если load.yaml оказался телом танка для GET запросов
                print('Checking files for sending GET requests')
                time.sleep(5)
                os.system(run)
                os.rename('load.yaml', self.path)
                print('Scenario complete')
                time.sleep(5)

            else:
                print('File(s) to run testing missing')
                exit(0)

        elif os.path.exists(self.path): # запуск действий, если в рабочей папке был только один файл, путь к которому передается в объекте
            print('Preparing files for sending GET requests')
            os.rename(self.path, 'load.yaml')        
            time.sleep(5)
            os.system(run)
            print('Scenario complete')
            os.rename('load.yaml', self.path)
            time.sleep(5)

        elif os.path.exists('load.yaml'): # запуск проверки, если в рабочей папке был только load.yaml
            file = open('load.yaml', 'r') # открываем файл load.yaml
            text = file.read()

            if GET in text: # действия, выполняемые в случае, если load.yaml оказался телом танка для GET запросов
                print('Checking files for sending GET requests')
                time.sleep(5)
                os.system(run)
                os.rename('load.yaml', self.path)
                print('Scenario complete')
                time.sleep(5)

            elif POST in text: # действия, выполняемые в случае, если load.yaml оказался телом танка для POST запросов
                print('Checking files for sending GET requests')
                print('Changing a tank with POST requests to tank GET requests')
                os.rename('load.yaml', 'POST_запросы.yaml')
                time.sleep(5)
                os.rename(self.path, 'load.yaml')
                time.sleep(5)
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