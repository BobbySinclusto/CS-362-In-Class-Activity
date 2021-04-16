import random

def gen_pwd(n):
    alphabet = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*()_+'
    print(''.join([random.choice(alphabet) for i in range(n)]))

n = int(input('Enter the number of characters you want in your password: '))
gen_pwd(n)
