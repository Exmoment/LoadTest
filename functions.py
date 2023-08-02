import time
import check #import LoadPOSTTesting, LoadGETTesting

def POSTandGET():
    iterrationGET = int(input('Enter the number of planned scenarios GET requests: '))
    iterrationPOST = int(input('Enter the number of planned scenarios POST requests: '))
    
    if (iterrationGET > 0) and (iterrationPOST > 0):
        
        while iterrationGET > 0:
            case = check.LoadGETTesting("CaseGET")
            try:
                case.path = input('Enter the name of the file with the body of the tank: ')
            except:
                print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
            case.CaseGET()
            iterrationGET -= 1
            print('iterration = ', iterrationGET)
            time.sleep(30)
        
        while iterrationPOST > 0:
            case = check.LoadPOSTTesting("CasePOST")                    
            try:
                case.path = input('Enter the path to the ammo file, or a name from the working folder: ')
                case.path_2 = input('Enter the name of the file with the body of the tank: ')
            except:
                print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
            case.CasePOST()
            iterrationPOST -= 1
            print('iterration = ', iterrationPOST)
            time.sleep(30)

    else:
        print('You entered an invalid value')
        exit(0)


def POST():
    iterration = int(input('Enter the number of planned scenarios: '))
    
    if iterration > 0:

        while iterration > 0:
            case = check.LoadPOSTTesting("CasePOST")                    
            try:
                case.path = input('Enter the path to the ammo file, or a name from the working folder: ')
                case.path_2 = input('Enter the name of the file with the body of the tank: ')
            except:
                print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
            case.CasePOST()
            iterration -= 1
            print('iterration = ', iterration)
            time.sleep(30)
            
    else:
        print('You entered an invalid value')
        exit(0)


def GET():
    iterration = int(input('Enter the number of planned scenarios: '))
    
    if iterration > 0:

        while iterration > 0:
            case = check.LoadGETTesting("CaseGET")
            try:
                case.path = input('Enter the name of the file with the body of the tank: ')
            except:
                print('No ammo file or tank body found for the first scenario. You need to check the path to the files')
            case.CaseGET()
            iterration -= 1
            print('iterration = ', iterration)
            time.sleep(30)

    else:
        print('You entered an invalid value')
        exit(0)