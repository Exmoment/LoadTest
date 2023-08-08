import functions


def objects():

    typeLoad = str(input('Enter which load tests you want to run POST/GET/GET and POST: '))

    if ('GET and POST' in typeLoad) or ('get and post' in typeLoad) or ('POST and GET' in typeLoad) or ('post and get' in typeLoad):
        functions.POSTandGET()

    elif ('POST' in typeLoad) or ('post' in typeLoad):
        functions.POST()

    elif ('GET' in typeLoad) or ('get' in typeLoad):
        functions.GET()

    else:
        print('Invalid value')

print('Test completed')