# name = input('введите имя ')
# print(name.title()) # title начальная буква будет большая
# print(name.upper()) # upper все буквы заглавными 
# print(name.lower()) #lower все буквы маленькими 
# print(name.swapcase()) #swapcase все маленькие буквы в большие а большие в маленькие 
# print(name.capitalize()) #capitalize начальные бувый заглавной 

# a = ' '
# print(a.isdigit()) # isdigit Все ли состоит из цифр 
# print(a.isalpha()) # isalpha Все ли состоит из букв 
# print(a.isidentifier()) # isidentifier Все ли у нас пишется слитно
# print(a.islower()) # islower Все ли у нас в нижнем регистре
# print(a.isupper()) # isupper Все ли у нас в верхнем регистре
# print(a.istitle()) # istitle Все ли у нас начинаются с большой буквы
# print(a.isnumeric()) # isnumeric Все ли у нас состоит из цифр
# print(a.isspace()) # isspace Все ли у нас в тексте состоит из пробелов
# print(a.isprintable()) # Все ли мы можем спинтовать


# text = '1Привет Ади' 
# print(text.strip('1')) # удаление начальнуе букву 
# print(text.rstrip('и')) # удвление последнию букву 
# print(text.lstrip('1'))  # удаление начальной буквы 


# text = 'maggrsegg'
# print(text.center(9,'*')) # Выравнивание строки 
# print(text.rjust(9,'*')) # Выравнивание строки с права 
# print(text.ljust(9,'*')) # Выравнивание строки с лева

# print(text.zfill(100)) # Дополнение текста на 0

# print(f'maasd{text}')
# print("name {0} {1}".format('Marselle','hello'))

# text = 'pgygthon, go, cgg++'
# print(text.replace('c++', 'с')) # замена подстроки в строке

# print(text.find('g')) # Показать индекс буквы
# print(text.find('g',9)) # Показать индекс буквы после 3 индекса
# print(text.rfind('+',17))

# print(text.index('g',4))
# print(text.rindex('g',4))

# print('*'.join(text)) # Вернуть текст после каждой буквы *


# print(text.count('o',5)) #сколько в тексте букв о после 5го индекса 
# print(text.count('o')) #сколько в тексте букв о 

# print(text.split()) #разделит тест  и обернет в массив 
# print(text.splitlines()) #весь тест в массив 
# print(text.partition('Hello')) #разделить 

# print(text.startswith('H')) # Начинается ли наш текст с буквы H
# print(text.endswith('d')) # Заканчивается ли наш тексте с буквы d

# print(len(text)) #Посчитать весь текст 

# text = 'Hello'
# print(text[1:3])

















#1
#a = 'HelloWorld'
#print(a[:5].lower(),a[5:].upper())


# p1 = input('Придумайье пороль ') 
# p2 = input('Повторите пороль ')

# if p1 == p2:
#     if len(p2) >= 8:
#         if '123' not in p2:
#             password = p2 
#             print('*'.join(password))
#         else:
#             print('простой пороль')
#     else:
#         print ('error')
# else:
#     print('хороший пороль')



# name = input('Как вас зовут? ')
# age = input('сколько вам лет? ')
# film = input('Какой любимый фильм? ')

# print(f'Здравствуйте {name}')
# print(f'{film} Классный фильм')



login = input('Придумайте логин ')
passwod = input('Придумайте пороль ')

if (login.lower()):
    if 'qwertyuiopasdfghjklzxcvbnm'  not in login:
        if '!' '"' '№' ';' '%' ':' '?' '*''()' not in login:
            print(login)
        else:
            print('error')
    else:
        print('error')
else:
    print('error')

if len(passwod) > 8:
    if 'qwertyuiopasdfghjklzxcvbnm' not in passwod:
        if '12345678' not in login:
            print('хороший пороль')
    else:
        print('False')
else:
    print('False')