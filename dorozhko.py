import math

s = None

print('здравствуйте,что вы хотите вычислить? 1 - НОД,2 - НОК,3 - синус,'
      '4 - косинус,5 - факториал,6 - тангенс,7 - логарифм числа,8 - гипатенуза,9 - корень')
val = int(input(' - '))
if val == 1:
    print('Напишите числа ')
    while True:
        a = int(input())
        b = int(input())
        num = math.gcd(a,b)
        print(num)
        c = int(input('продолжить(1 - да ,2 - нет)'))
        if c == 2:
            print('Пока')
            break
elif val == 2:
    print('Напишите числа ')
    while True:
        a = int(input())
        b = int(input())
        num = math.lcm(a,b)
        print(num)
        c = int(input('продолжить?(1 - да ,2 - нет)'))
        if c == 2:
            print('Пока')
            break
elif val == 3:
    print('Напишите угол ')
    while True:
        a = int(input())
        num = math.sin(a)
        print(num)
        c = int(input('продолжить?(1 - да ,2 - нет)'))
        if c == 2:
            print('Пока')
            break
elif val == 4:
    print('Напишите угол  ')
    while True:
        a = int(input())
        num = math.cos(a)
        print(num)
        c = int(input('продолжить?(1 - да ,2 - нет)'))
        if c == 2:
            print('Пока')
            break
elif val == 5:
    print('Напишите число ')
    while True:
        a = int(input())
        num = math.factorial(a)
        print(num)
        c = int(input('продолжить?(1 - да ,2 - нет)'))
        if c == 2:
            print('Пока')
            break
elif val == 6:
    print('Напишите число ')
    while True:
        a = int(input())
        num = math.tan(a)
        print(num)
        c = int(input('продолжить?(1 - да ,2 - нет)'))
        if c == 2:
            print('Пока')
            break
elif val == 7:
    while True:
        print('Первое число')
        a = int(input())
        print('Второе число')
        b = int(input())
        num = math.log(a,b)
        print(num)
        c = int(input('продолжить?(1 - да ,2 - нет)'))
        if c == 2:
            print('Пока')
            break
elif val == 8:
    print('Введите катеты')
    while True:
        a = int(input())
        b = int(input())
        num = math.hypot(a,b)
        print(num)
        c = int(input('продолжить?(1 - да ,2 - нет)'))
        if c == 2:
            print('Пока')
            break
else:
    print('Напишите число ')
    while True:
        a = int(input())
        num = math.sqrt(a)
        print(num)
        c = int(input('продолжить?(1 - да ,2 - нет)'))
        if c == 2:
            print('Пока')
            break
