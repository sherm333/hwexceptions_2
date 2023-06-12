# Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float), и возвращает введенное значение. 
# Ввод текста вместо числа не должно приводить к падению приложения, вместо этого, необходимо повторно запросить 
# у пользователя ввод данных.


def number():
        while True: 
            number = input("Введите дробное число: ")
            try:
                num = float(number)
                if type(num) is float:
                    break
            except ValueError:
                print("Вы ввели неверное значение!")
        return num



print(f"Вы ввели дробное число - {number()}")