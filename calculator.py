print('Welcome to the calculator!')

quit = False
while (not quit):
    print(
'''
Choose an option:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Quit''')
    choice = input()

    if choice == '1':
        print(f'Result: {int(input("First number: ")) + int(input("Second number: "))}')
    elif choice == '2':
        print(f'Result: {int(input("First number: ")) - int(input("Second number: "))}')
    elif choice == '3':
        print(f'Result: {int(input("First number: ")) * int(input("Second number: "))}')
    elif choice == '4':
        print(f'Result: {int(input("First number: ")) / int(input("Second number: "))}')
    else:
        break
