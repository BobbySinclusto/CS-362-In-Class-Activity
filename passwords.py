import random
n = int(input('Enter the number of characters you want in your password: '))
alphabet = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*()_+'
print(''.join([random.choice(alphabet) for i in range(n)]))
