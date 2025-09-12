# 1

# print("Привет, мир!")
# print(5, 10, 15)
# print(10 + 25)

# 2

# print(1, 2, 3,sep='&')
# print("Python",end=' ')
# print("лучший язык")

# 3

# x = 3.14
# y = -8
# print(f"Координаты точки: x = {x}; y = {y}")
# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# print(f"Имя: {name}, Возраст: {age}")

# 4
# name = input("Введите имя: ")
# print(f"Привет, {name}")

# 5

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)
#
# print(num1**2)

#  1 (Булевые значения)

print(5 > 3)
print(10 < 2)
print(7 == 7)
print(6 != 8)
print(4 >= 4)
print(9 <= 3)
res = 8 > 12
print(res,type(res))

# 2

x = 15
print(x % 2 == 0)
print(x // 5)
print((x % 3 == 0) and (x % 5 == 0))

# 3

y = 4.5
print(y >= 1 and y <= 10)
print((y >= 0 and y <= 5) or (y >= 10 and y <= 15))
print(not (y < 5))

# 4

print(True or False and False)
print(not False and True)
print(False or not True and True)
print(not (10 > 5 or 3 < 1))

# 5

print(bool(0))
print(bool(-5))
print(bool(3.14))
print(bool(""))
print(bool("Python"))
print(bool(" "))

# 6

n = 6
print(n > 0)
print(n % 2 == 0)
print(n % 3 == 0)


# 1  ( Срезы строк )

s = "Программирование"
print(s[0])
print(s[-1])
print(s[2], s[-2])


# 2
s = "Программирование"
# print(s[100])      # Ошибка string index out of range
print(s[len(s) - 1])

# 3

s = "Программирование"
s6 = s[0:6]
print(s6)
s5 = s[-5:]
print(s5)
print(s[::2])

# 4

s = "Программирование"
print(s[::3])
print(s[::-2])

# 5
s = "Программирование"
# s[0] = "п"  # ошибка строка не изменяемый тип данных
s2 = 'п' + s[1:]
print(s2)

# 6

word = "abcdefgh"
print(word[2:5])
print(word[::-1])
print(word[1:-1])
