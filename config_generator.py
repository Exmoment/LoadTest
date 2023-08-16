import os


class ammo_POST:
    request = ''
    
    def __init__(post, name):
        post.name = name
        post.method = ""
        post.path_url = ""
        post.host = ""
        post.port = ""
        post.body = """"""     

    def ammo(post):
        request = "{method} {path_url} HTTP/1.1\r\n{headers}\r\n{body}".format(
            method = post.method,
            path_url = post.path_url,
            headers = "Host: {host}:{port}\r\nContent-Type: application/json; charset=utf-8\r\nContent-Length: {content_len}".format(
                host = post.host,
                port = post.port,
                content_len = len(post.body.encode('utf-8'))
            ),
            body = post.body
        )
        return "{request_size}\n{request}\r\n".format(request_size = len(request.encode('utf-8')), request = request)


class loadPOST:

    def __init__(post, name):
        post.name = name
        post.host = ""
        post.port = ""
        post.ammo_file = ""
        post.ssl = ""
        post.schedule = ""
        post.instances = ""
        post.c_enabled = ""
        post.t_enabled = ""
        post.o_enabled = ""
        post.job_dsc = ""

    def load(post):
        tank = "{phantom}\r\n{console}\r\n{telegraf}\r\n{autostop}\r\n{overload}".format(
            phantom = "phantom:\r\n  address: {host}:{port}\r\n  ammo_type: phantom\r\n  ammofile: {ammo_file}\r\n  ssl: {ssl}\r\n  load_profile:\r\n{load_profile}\r\n  instances: {instances}".format(
                host = post.host,
                port = post.port,
                ammo_file = post.ammo_file,
                ssl = post.ssl,
                load_profile = "    load_type: rps\r\n    schedule: {schedule}".format(
                    schedule = post.schedule
                ),
                instances = post.instances,
            ),
            console = "console:\r\n  enabled: {c_enabled}".format(
                c_enabled = post.c_enabled
            ),
            telegraf = "telegraf:\r\n enabled: {t_enabled}".format(
                t_enabled = post.t_enabled
            ),
            autostop = "autostp:\r\n  enabled: true\r\n  package: yandextank.plugins.Autostop\r\n  autostop:\r\n    - http(5xx,10%,20s), time(10s,20s), net(110,5%,60s)",
            overload = "overload:\r\n  enabled: {o_enabled}\r\n  job_name: {name}\r\n  job_dsc: {dsc}\r\n  package: yandextank.plugins.DataUploader\r\n  token_file: \"token.txt\"".format(
                o_enabled = post.o_enabled,
                name = post.name,
                dsc = post.job_dsc
            ),
        )
        return tank


class loadGET:

    def __init__(get, name):
        get.name = name
        get.host = ""
        get.port = ""
        get.agent = ""
        get.url = """"""
        get.ssl = ""
        get.instances = ""
        get.schedule = ""
        get.c_enabled = ""
        get.t_enabled = ""
        get.o_enabled = ""
        get.job_dsc = ""

    
    def load(get):
        tank = "{phantom}\r\n{console}\r\n{telegraf}\r\n{autostop}\r\n{overload}".format(
            phantom = "phantom:\r\n  address: {host}:{port}\r\n  header_http: \"1.1\"\r\n{headers}\r\n{uris}\r\n  ssl: {ssl}\r\n  instances: {instances}\r\n{load_profile}".format(
                host = get.host,
                port = get.port,
                headers = "  headers:\r\n-\"[Host: {host}]\"\r\n-\"[User-Agent: {agent}]\"".format(
                    host = get.host,
                    agent = get.agent
                ).replace('-"[', '    - "['),
                uris = "  uris:\r\n{url}".format(
                    url = get.url.replace('- /', '    - /')
                ),
                ssl = get.ssl,
                instances = get.instances,
                load_profile = "  load_profile:\r\n    load_type: rps\r\n    schedule: {schedule}".format(
                    schedule = get.schedule
                ),
            ),
            console = "console:\r\n  enabled: {c_enabled}".format(
                c_enabled = get.c_enabled
            ),
            telegraf = "telegraf:\r\n enabled: {t_enabled}".format(
                t_enabled = get.t_enabled
            ),
            autostop = "autostp:\r\n  enabled: true\r\n  package: yandextank.plugins.Autostop\r\n  autostop:\r\n    - http(5xx,10%,20s), time(10s,20s), net(110,5%,60s)",
            overload = "overload:\r\n  enabled: {o_enabled}\r\n  job_name: {name}\r\n  job_dsc: {dsc}\r\n  package: yandextank.plugins.DataUploader\r\n  token_file: \"token.txt\"".format(
                o_enabled = get.o_enabled,
                name = get.name,
                dsc = get.job_dsc
            ),
        )
        return tank


'''
def create_loadGET():

    create_loadGET = loadGET("loadGET")
    create_loadGET.host = "example.net"
    create_loadGET.port = "443"
    create_loadGET.agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    create_loadGET.url = """- /example
- /my
- /test"""
    create_loadGET.ssl = "true"
    create_loadGET.instances = "1000"
    create_loadGET.schedule = "line(1, 10000, 5m) const(5000,2m)"
    create_loadGET.c_enabled = "true"
    create_loadGET.t_enabled = "false"
    create_loadGET.o_enabled = "true"
    create_loadGET.job_dsc = "example"
    loadGET_text = create_loadGET.load()
    with open('load.yaml', 'w+') as loadGET_file:
        loadGET_file.write(loadGET_text)
    print(loadGET_text)

create_loadGET()
'''

def create_LoadPOST():
    
    create_loadPOST = loadPOST("loadPOST")
    create_loadPOST.host = "example.net"
    create_loadPOST.port = "443"
    create_loadPOST.ammo_file = "ammo_POST.txt"
    create_loadPOST.ssl = "true"
    create_loadPOST.schedule = "line(1, 10000, 5m) const(5000,2m)"
    create_loadPOST.instances = "1000"
    create_loadPOST.c_enabled = "true"
    create_loadPOST.t_enabled = "false"
    create_loadPOST.o_enabled = "true"
    create_loadPOST.job_dsc = "testing_POST_requests"
    loadPOST_text = create_loadPOST.load()
    with open('load.yaml', 'w+') as loadPOST_file:
        loadPOST_file.write(loadPOST_text)
    print(loadPOST_text)

create_LoadPOST()


'''
def create_ammo():

    create_ammo = ammo_POST("POST")
    create_ammo.method = "POST"
    create_ammo.path_url = "/my/test"
    create_ammo.host = "example.net"
    create_ammo.port = "443"
    create_ammo.body = """
    {
        example
    }
    """
    ammo_text = create_ammo.ammo()
    nameAmmoFile = str(input('Введите имя для создаваемого файла: '))
    with open(nameAmmoFile+'.txt', "w+") as file:
        file.write(create_ammo.ammo())
    print("Файл с запросом успешно создан")
    print(ammo_text)

create_ammo()
'''