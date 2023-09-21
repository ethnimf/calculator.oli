import math
import sys

def DeyStvie(id):

    
    if id == 0:
        print("Такого действия нет!")
    if id == 1:
        print("Введите первое число")
        a = int(input())
       
        print("Введите второе число")
        b = int(input())

        print("Ответ:")
        print(a + b)

        print("Введите действие:")
        id = int(input())
        DeyStvie(id)
    if id == 2:
        print("Введите первое число")
        a = int(input())
        print("Введите второе число")
        b = int(input())

        print("Ответ:")
        print(a - b)

        print("Введите действие:")
        id = int(input())
        DeyStvie(id)
    if id == 3:
        print("Введите первое число")
        a = int(input())
                
        print("Введите второе число")
        b = int(input())

        if a <= 0 or b <= 0:
            print("Введите число больше 0 !")
            return
        
        print("Ответ:")
        print(a * b)

        print("Введите действие:")
        id = int(input())
        DeyStvie(id)
    if id == 4:
        print("Введите первое число")
        a = int(input())
        print("Введите второе число")
        b = int(input())

        if a <= 0 or b <= 0:
            print("Введите число больше 0 !")
            return

        print("Ответ:")
        print(a / b)

        print("Введите действие:")
        id = int(input())
        DeyStvie(id)
    if id == 5:
        print("Введите первое число")
        a = int(input())
        print("Введите второе число")
        b = int(input())

        if b <= 0:
            print("Введите число больше 0 !")
            return

        print("Ответ:")
        print(a ** b)

        print("Введите действие:")
        id = int(input())
        DeyStvie(id)
    if id == 6:
        print("Введите первое число")
        a = int(input())

        if a <= 0:
            print("Введите число больше 0 !")
            return

        print("Ответ:")
        print(math.sqrt(a))

        print("Введите действие:")
        id = int(input())
        DeyStvie(id)
    if id == 7:
        print("Введите первое число")
        a = int(input())

        if a <= 0:
            print("Введите число больше 0 !")
            return

        print("Ответ:")
        print(a / 100)   

        print("Введите действие:")
        id = int(input())
        DeyStvie(id) 
    if id == 8:
        print("Введите первое число")
        a = int(input())

        if a <= 0:
            print("Введите число больше 0 !")
            return

        print(math.factorial(a))

        print("Введите действие:")
        id = int(input())
        DeyStvie(id)
    if id == 9:
        print("Введите первое число")
        a = int(input())

        if a <= 0:
            print("Введите число больше 0 !")
            return

        print("Ответ:")
        print(math.cos(a))  

        print("Введите действие:")
        id = int(input())
        DeyStvie(id)
    if id <= 10:
        print("Введите первое число")
        a = int(input())

        if a == 0:
            print("Введите число больше 0 !")
            return

        print("Ответ:")
        print(math.sin(a))  

        print("Введите действие:")
        id = int(input())
        DeyStvie(id)
    if id == 11:
        print("Введите первое число")
        a = int(input())

        if a <= 0:
            print("Введите число больше 0 !")

            return
        
        print(math.tan(a))
        print("Введите действие:")

        id = int(input())
        DeyStvie(id)  
    if id == 12:
        sys.exit()
        

def Start():
    print("1. Сложить 2 числа\n" +
                "2. Вычесть первое из второго\n" +
                "3. Перемножить два числа\n" +
                "4. Разделить первое на второе\n" +
                "5. Возвести в степень N первое число\n" +
                "6. Найти квадратный корень из числа\n" +
                "7. Найти 1 процент от числа\n" +
                "8. Найти факториал из числа\n" +
                "9. Найти косинус\n" +
                "10. Найти Синус\n" +
                "11. Найти тангенс\n" +
                "12. Выйти из программы")

    print("Выберите действие")
    DeyStvie(int(input()))
Start()

