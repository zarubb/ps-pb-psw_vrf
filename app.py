psw = input('Введите пароль: ') #запрос ввода пароля
msg = 'Ваш пароль состоит только из цифр' # задаем "по-умолчанию" значение сообщения, которое будет выводиться после ввода пароля
psw_len = len(psw) #вычисление длинны пароля

try:
    result_1 = 2/psw_len # проверка пустого пароля
    result_2 = int(psw) # проверка "не только цифры"
except ZeroDivisionError: # вывод "пустой пароль" в случае ошибки деления на "0"
     msg = 'Вы ввели пустой пароль' 
except ValueError: # вывод "все норм" в случае ошибки наличия символов
    msg = 'Требования к паролю соблюдены'

print(msg) # вывод получившегося сообщения
