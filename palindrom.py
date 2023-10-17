def is_palindorm(string):
    string = str(string)
    if string == string[::-1]:
        print(f'строка "{string}" является палиндромом')
    else:
        print(f'строка "{string}" не является палиндромом')

