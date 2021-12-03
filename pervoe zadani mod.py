print("Для получения заказа, пожалуйста, введите ваши данные: ")
while True:
    first_name = input("Введите вашу фамилию: ")
    while first_name == "":
        print("Вы не ввели вашу фамилию")
        first_name = input("Введите вашу фамилию: ")
    last_name = input("Введите ваш имя: ")
    while last_name == "":
        print("Вы не ввели ваше имя")
        last_name = input("Введите ваш имя: ")
    father_name = input("Введите ваш отчество: ")
    while father_name == "":
        print("Вы не ввели ваше отчество")
        father_name = input("Введите ваш отчество: ")
    adress = input("Введите ваш адрес: ")
    while adress == "":
        print("Вы не ввели ваш адрес")
        adress = input("Введите ваш отчество: ")
    full_name = f'{first_name} {last_name} {father_name}'
    print(f"""
        Заказ будет доставлен на адрес: {adress.title()}
        Получатель: {full_name.title()}""")
    ready = input("""
        Если все данные введены верны, то Y.
        Если заметили ошибку и необходимо ввести данные заново, то любую клавишу: """)
    if ready.title() == 'Y' or 'Н':
        break
    else:
        continue

