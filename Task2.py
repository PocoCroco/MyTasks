def passport(name, surname, date_of_birth, city, email, phone_number):
     return f'Имя: {name}, фамилия: {surname}, '\
            f'год рождения: {date_of_birth}, город: {city}, '\
            f'эл. почта: {email}, номер телефона: {phone_number}'
print(passport(surname=input('Введите вашу фамилию: '), name=input('Введите ваше имя: '),
               date_of_birth=input('Введите год рождения: '), city=input('Введите ваш город: '),
               email=input('Введите ваш email: '), phone_number=input('Введите ваш номер телефона: ')))
