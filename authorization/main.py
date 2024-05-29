def check_password(password):
    try:
        with open('students.txt', 'r') as file:
            for line in file:
                if line.strip() == password:
                    return True
    except FileNotFoundError:
        print("Файл не найден!")
        return False
    return False

str = "Хотите ли вы добавить новый пароль?"
print(str, "\n Yes/No\t[Y][N]")

if input().upper() == "Y":
    print("Введите новый пароль")
    psw = input()
    with open('students.txt', 'a') as file:
        file.write(psw + '\n')
else:
    print("Ну нет - так нет =)")

while True:
    us_data = input("Введите пароль: ")
    if check_password(us_data):
        print("Добро пожаловать в систему!\n")
        break
    else:
        print("Неправильный пароль! Отказано в доступе.")