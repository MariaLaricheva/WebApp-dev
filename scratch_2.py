import math, cmath, sys

print("ИУ5-51б Ларичева М.В. Лаб1")
print("Программа для решения биквадратных уравнений")

a = 0
b = 0
c = 0

param_a = False
param_b = False
param_c = False

if len(sys.argv) == 4:
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

while param_a == 0:
    try:
        print("Введите коэффициент при x^2:")
        a=float(input())
        param_a = True
    except ValueError:
        print("Введите число, а не string или char")
    if a == 0:
        print("При таком коэффициенте уравнение не является квадратным")
        param_a = False

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

x1 = ""
x2 = ""
x3 = ""
x4 = ""
y = 0

x1_comp = cmath.sqrt((-b/2)/a + (cmath.sqrt(D)/2)/a)
x2_comp = cmath.sqrt((-b/2)/a - (cmath.sqrt(D)/2)/a)
x3_comp = - x1_comp
x4_comp = - x2_comp

print(x1_comp, x3_comp, x2_comp, x4_comp)

if D == 0:
    if b*a < 0:
        x1 = str(math.sqrt(math.sqrt(-b/a)))
    else:
        x1 = str(math.sqrt(math.sqrt(abs(-b / a)))) + " j"

    x2 = "-" + x1
    print("Всего 2 корня: \n1.", x1, "\n2.", x2)

else:
    if D > 0:
        y1 = ((-b + math.sqrt(D)) /a)/2
        y2 = ((-b - math.sqrt(D)) /a)/2
        if y1 > 0:
            x1 = str(math.sqrt(y1))
            x2 = str(-math.sqrt(y1))
        else:
            x1 = str(math.sqrt(-y1)) + "j"
            x2 = str(-math.sqrt(-y1)) + "j"
        if y2 > 0:
            x3 = str(math.sqrt(y2))
            x4 = str(-math.sqrt(y2))
        else:
            x3 = str(math.sqrt(-y2)) + "j"
            x4 = str(-math.sqrt(-y2)) + "j"
    else:
        x1 = "sqrt(" + str((-b/2)/a) + " + " + str (math.sqrt(-D)) + "j)"
        x3 = "sqrt(" + str((-b / 2) / a) + " - " + str(math.sqrt(-D)) + "j)"
        x2 = "-sqrt(" + str((-b / 2) / a) + " + " + str(math.sqrt(-D)) + "j)"
        x4 = "-sqrt(" + str((-b / 2) / a) + " - " + str(math.sqrt(-D)) + "j)"

    print("Всего 4 корня: \n1.", x1, "\n2.", x2, "\n3.", x3, "\n4.", x4)
