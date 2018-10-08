# Task_1

def hypotenuse(a,b):
    return  'Гипотенуза C = ' + str (((a**2) + (b**2)) ** 0.5)

a =float(input('Введите сторону катета прямоуголного треугольника A: '))
b =float(input('Введите вторую сторону катета прямоуголного треугольника B: '))

res = hypotenuse(a,b)
print(res)
print()

# Task_2

def ball_volume(P):
    return 'V шара = ' + str ((4/3) * P * R**3) + ' кубических сантиметров'

P = 3.14
R = int(input('Введите радиус, для определения объема шара: '))

res = ball_volume(P)
print(res)
print()

# Task_3

def cube_volume(s):
    return 'V куба = ' + str (s**3) + ' кубических сантиметров'

s = int(input('Введите длину ребра куба для определения его объема в куб.см.: '))

res = cube_volume(s)
print(res)
print()

# Task_4

def valum (a,b,h):
    return 'V параллелепипеда = ' + str (a * b *h) + ' кубических сантиметров'

a = float(input('Введите длину грани А: '))
b = float(input('Введите длину грани В: '))
h = float(input('Введите высоту: '))

res = valum (a,b,h)
print(res)
print()

# Task_5

def cylinder_volume(r,h):
    return 'V цилиндра = ' + str ((P * (r**2) * h)) + ' кубических сантиметров'

P = 3.14

r = float(input('Укажите радиус цилиндра: '))
h = float(input('Введите высоту цилиндра: '))

res = cylinder_volume(r,h)
print(res)

