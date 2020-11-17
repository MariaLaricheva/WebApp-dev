import math, cmath, sys

print("ИУ5-51б Ларичева М.В. Лаб1")
print("Программа для решения биквадратных уравнений")

a = 0               #коэффициент при x^2
b = 0               #коэффициент при x
c = 0               #свободный коэффициент

param_a = False     #false - переменная не введена или введена некорректно, true - переменная введена
param_b = False     #false - переменная не введена или введена некорректно, true - переменная введена
param_c = False     #false - переменная не введена или введена некорректно, true - переменная введена

#для ввода коэффициентов из командной строки:
if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        if a == 0:
            print("При таком коэффициенте уравнение не является квадратным")
        else:
            param_a = True
    except ValueError:
        print("Введённый параметр неправильного типа")
    try:
        b = float(sys.argv[2])
        param_b = True
    except ValueError:
        print("Введённый параметр неправильного типа")
    try:
        c = float(sys.argv[3])
        param_c = True
    except ValueError:
        print("Введённый параметр неправильного типа")

if len(sys.argv) == 3:
    try:
        a = float(sys.argv[1])
        param_a = True
    except ValueError:
        print("Введённый параметр неправильного типа")
    try:
        b = float(sys.argv[2])
        param_b = True
    except ValueError:
        print("Введённый параметр неправильного типа")

if len(sys.argv) == 2:
    try:
        a = float(sys.argv[1])
        param_a = True
    except ValueError:
        print("Введённый параметр неправильного типа")

#для ввода коэффициентов внутри программы:
while param_a == 0:
    try:
        print("Введите коэффициент при x^2:")
        a=float(input())
        if a == 0:
            print("При таком коэффициенте уравнение не является квадратным")
        else:
            param_a = True
    except ValueError:
        print("Введите число, а не string или char")

while param_b == 0:
    try:
        print("Введите коэффициент при x:")
        b=float(input())
        param_b = True
    except ValueError:
        print("Введите число, а не string или char")

while param_c == 0:
    try:
        print("Введите свободный коэффициент:")
        c=float(input())
        param_c = True
    except ValueError:
        print("Введите число, а не string или char")

print("Вы ввели уравнение: ", a, "x^4 +", b, "x^2 +", c, "= 0")

D = b*b - 4*a*c
print("Дискриминант:", D)

if D == 0:
    x1 = cmath.sqrt(cmath.sqrt(-b/a))
    x2 = -x1
    print("Всего 2 корня: \n1.", x1, "\n2.", x2)

else:
    x1_comp = cmath.sqrt((-b / 2) / a + (cmath.sqrt(D) / 2) / a)
    x2_comp = cmath.sqrt((-b / 2) / a - (cmath.sqrt(D) / 2) / a)
    x3_comp = - x1_comp
    x4_comp = - x2_comp
    print("Всего 4 корня: \n1.", x1_comp, "\n2.", x2_comp, "\n3.", x3_comp, "\n4.", x4_comp)

