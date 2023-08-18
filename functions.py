import time
import check
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


class choiceType:

    def __init__(self, name):
        self.name = name
        self.iterrationGET = ''
        self.iterrationPOST = ''
        self.pathBodyPOST = ''
        self.pathBodyGET = ''
        self.pathAmmo = ''

    def POSTandGET(self):
        
        if (self.iterrationGET > 0) and (self.iterrationPOST > 0):
            
            while self.iterrationGET > 0:
                case = check.LoadGETTesting("CaseGET")
                try:
                    case.path = self.pathBodyGET
                except:
                    print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
                case.CaseGET()
                self.iterrationGET -= 1
                print('iterration = ', self.iterrationGET)
                time.sleep(30)
            
            while self.iterrationPOST > 0:
                case = check.LoadPOSTTesting("CasePOST")                    
                try:
                    case.path = self.pathAmmo
                    case.path_2 = self.pathBodyPOST
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
        
        if self.iterrationPOST > 0:

            while self.iterrationPOST > 0:
                case = check.LoadPOSTTesting("CasePOST")                    
                try:
                    case.path = self.pathAmmo
                    case.path_2 = self.pathBodyPOST
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
        
        if self.iterrationGET > 0:

            while self.iterrationGET > 0:
                case = check.LoadGETTesting("CaseGET")
                try:
                    case.path = self.pathBodyGET
                except:
                    print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
                case.CaseGET()
                self.iterrationGET -= 1
                print('iterration = ', self.iterrationGET)
                time.sleep(30)

        else:
            print('You entered an invalid value')
            exit(0)