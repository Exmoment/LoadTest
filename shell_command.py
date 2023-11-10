
'''
run = "docker run \
-v $(pwd):/var/loadtest \
-v $SSH_AUTH_SOCK:/ssh-agent -e SSH_AUTH_SOCK=/ssh-agent \
--net host \
-it yandex/yandex-tank"
'''

path = "C:/Users/User/Documents/file.txt"
slash_pos = path.rfind("/")
name = path[slash_pos+1:]
print(name)