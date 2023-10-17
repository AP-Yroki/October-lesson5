def three_args(var1, var2, var3):
    res = locals()
    print('Переданы аргументы: ', *(f'{key} = {value}' for key, value in res.items() if value))

three_args(1, None, 'test')