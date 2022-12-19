#                              ДОМАШНЕЕ ЗАДАНИЕ К СЕМИНАРУ 1                           
# 
# ЗАДАЧА 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#           и проверяет, является ли этот день выходным
# 
# dayWeek = int(input('Enter the number indicating the day of the week: '))
# if dayWeek < 1 or dayWeek > 7:
#     print('Incorrect value entered')
# else:
#     print(dayWeek == 6 or dayWeek == 7)

# ЗАДАЧА 2. Напишите программу для проверки истинности утверждения 
#           ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             print(x, y, z, end = ' ')
#             print(not(x or y or z) == ((not x) and (not y) and (not z)))
# отрицание суммы равно умножению отрицаний, как-то так вроде. Могу ошибаться
    
# ЗАДАЧА 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
#           причем Х <> 0 и Y <> 0 и выдает номер четверти плоскости, 
#           в которой находится эта точка

# x = int(input('Enter the X value: '))
# y = int(input('Enter the Y value: '))
# if x == 0 and y == 0:
#     print('The point is at the origin of the coordinates')
# elif x == 0:
#     print('The point is in axis Y')
# elif y == 0:
#     print('The point is in axis X')
# elif x > 0 and y > 0:
#     print('The point is in the first quarter of the plane')
# elif x > 0 and y < 0:
#     print('The point is in the second quarter of the plane')
# elif x < 0 and y < 0:
#     print('The point is in the third quarter of the plane')
# elif x < 0 and y > 0:
#     print('The point is in the fourth quarter of the plane')


# ЗАДАЧА 4. Напишите программу, которая по заданному номеру четверти, 
#           показывает диапазон возможных координат точек в этой четверти (x и y)

# quartNum = int(input('Enter the quarter number: '))
# if quartNum == 1:
#     print('X > 0, Y > 0')
# elif quartNum == 2:
#     print('X > 0, Y < 0')
# elif quartNum == 3:
#     print('X < 0, Y < 0')
# elif quartNum == 4:
#     print('X < 0, Y > 0')

# ЗАДАЧА 5. Напишите программу, которая принимает на вход координаты двух точек 
#           и находит расстояние между ними в 2D пространстве

# x1 = int(input('Enter the X value of the first point: '))
# y1 = int(input('Enter the Y value of the first point: '))
# x2 = int(input('Enter the X value of the second point: '))
# y2 = int(input('Enter the Y value of the second point: '))

# import math
# result = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
# print (round(result, 2))

        
    
# 
# 
# 
# 
# 
# 
# 
#                                   ЗАДАЧИ СЕМИНАРА 1

# ЗАДАЧА 1. Напишите программу, которая принимает на вход два числа и проверяет, 
#           является ли одно из них квадратом другого

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))

# print((a == b*b) ^ (b == a*a))

# ЗАДАЧА 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
# c = int(input('Enter the third number: '))
# d = int(input('Enter the fourth number: '))
# e = int(input('Enter the fifth number: '))

# max = a

# for i in a, b, c, d, e:
#     if max < i:
#         max = i
# print(max)

# Или вот так: print(max(int(input()), int(input()), int(input()), int(input()), int(input())))

# a = int(input())
# max = a
# for i in range(4):
#     a = int(input())
#     if a > max:
#         max = a
# print(max)

# a = [7, 9, 3, 2, 5]
# print(len(a))
# for i in range(0, len(a)):
#     print(i, a[i])

# ЗАДАЧА 3. Напишите программу, которая принимает на вход число и проверяет,
#           кратно ли оно 5 и 10 или 15, но не 30

# a = int(input('Enter an integer: '))
# print(((a % 5 == 0) and (a % 10 == 0) or (a % 15 == 0)) and (a % 30 != 0))

# ЗАДАЧА 4. Напишите программу, которая будет на вход принимать число N 
#           и выводить числа от - N до N

# N = int(input('Enter an integer: '))
# for i in range(-N, N + 1):
#     #print(i)
#     print(i, end = ' ') # Если нужно вывести в строку

# ЗАДАЧА 5. Напишите программу, которая будет принимать на вход дробь
#           и показывать первую цифру дробной части числа

# a = float(input('Enter a fractional number: '))
# if round((a * 10 % 10) // 1) > 0:
#     print(round((a * 10 % 10) // 1))
# else:
#     print('No')
# или:
# a = input(3.54341)
# b = a.split(".")
# print(b[1][0])
