print(""" Здравствуйте.
Для получения посылки необходимы ваши контактные данные.
Пожалуйста, заполните форму ниже:""")
while True:
    first_name = input("Ведите вашу фамилию: ")
    if first_name == "":
        print("Вы не ввели фамилию")
        continue
    else:
        while True:
            second_name = input("Ведите ваше имя: ")
            if second_name == "":
                print("Вы не ввели имя")
                continue
            else:
                while True:
                    father_name = input("Ведите ваше отчество: ")
                    if father_name == "":
                        print("Вы не ввели отчество")
                        continue
                    else:
                        while True:
                            full_name = f"{first_name} {second_name} {father_name}"
                            adress = input('Введите ваш адресс: ')
                            if adress != "":
                                print(
                                    f'Здравствуйте, {full_name.title()}. Посылка была отправлена по адресу: {adress.title()}')
                                break
                            else:
                                print('Вы не ввели адресс')
                        break
                    break
            break
    break
