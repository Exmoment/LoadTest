import time
import check
import click
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


class choiceType:

    def __init__(self, name):
        self.name = name
        self.iterrationGET = ''
        self.iterrationPOST = ''
        self.pathBody = ''
        self.pathAmmo = ''

    def POSTandGET(self):
        self.iterrationGET = int()
        self.iterrationPOST = int()
        
        if (self.iterrationGET > 0) and (self.iterrationPOST > 0):
            
            while self.iterrationGET > 0:
                case = check.LoadGETTesting("CaseGET")
                try:
                    case.path = input('Enter the name of the file with the body of the tank: ')
                except:
                    print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
                case.CaseGET()
                self.iterrationGET -= 1
                print('iterration = ', self.iterrationGET)
                time.sleep(30)
            
            while self.iterrationPOST > 0:
                case = check.LoadPOSTTesting("CasePOST")                    
                try:
                    case.path = input('Enter the path to the ammo file, or a name from the working folder: ')
                    case.path_2 = input('Enter the name of the file with the body of the tank: ')
                except:
                    print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
                case.CasePOST()
                self.iterrationPOST -= 1
                print('iterration = ', self.iterrationPOST)
                time.sleep(30)

        else:
            print('You entered an invalid value')
            exit(0)


    def POST(self):
        self.iterrationPOST
        self.pathBody
        self.pathAmmo
        
        if self.iterrationPOST > 0:

            while self.iterrationPOST > 0:
                case = check.LoadPOSTTesting("CasePOST")                    
                try:
                    case.path = self.pathAmmo
                    case.path_2 = self.pathBody
                except:
                    print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
                case.CasePOST()
                self.iterrationPOST -= 1
                print('iterration = ', self.iterrationPOST)
                time.sleep(30)
                
        else:
            print('You entered an invalid value')
            exit(0)


    def GET(self):
        click.pause('Введите количество итераций сценария GET запросов: ')
        self.iterrationGET = int(input('Enter the number of planned scenarios: '))
        
        if self.iterrationGET > 0:

            while self.iterrationGET > 0:
                case = check.LoadGETTesting("CaseGET")
                try:
                    case.path = input('Enter the name of the file with the body of the tank: ')
                except:
                    print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
                case.CaseGET()
                self.iterrationGET -= 1
                print('iterration = ', self.iterrationGET)
                time.sleep(30)

        else:
            print('You entered an invalid value')
            exit(0)