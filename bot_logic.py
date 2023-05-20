import random

def gen_pass(pass_length):
    elements = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def coin():
    flip = random.randint(1,2)

    if flip == 1:
        return 'Орёл'
    else:  
        return 'Решка'

def help():
    return('''**!gpassword** - Генерация пароля
**!coin** - Орёл или решка
**!help** - Помощь!''')
