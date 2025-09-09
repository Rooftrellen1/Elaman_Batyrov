# 1
name = 'Еламан'
age = 27
height = 1.87
print(f"Меня зовут {name}, мне {age} лет, мой рост составляет {height} ")

# 2
x = 10
print(type(x))
x = 25.5
print(type(x))
x = "Python"
print(type(x))

# 3

a = 7
b = a
print(a)
print(b)
a = 10
print(b) # Переменная a начала ссылаться на объект 10, но переменная b все еще ссылается на старый объект (7)

# 4

x = y = z = 100
print(x, y, z)
print(id(x), id(y), id(z)) # id будут одинаковые
x,y,z = 121,228,100
print(x,y,z)
print(id(x),id(y),id(z)) # id будут разные

#5

a = 5
b = 10
a,b = b,a
print(a,b)

#6

# True = 2
# print = 12
# if = 231  # невозможно создать зарезервированные слова, в качестве переменных

import keyword
print(keyword.kwlist)

# 7
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1),type(var2),type(var3))
var1 = "World"
print(type(var1))

# 8

cpu = 'i7-7700k'
gpu = 'GTX 1080'
ram = 8
SSD = 1000
HDD = 2000
print(cpu,gpu,ram,SSD,HDD)

переменная = 10
print(переменная)  # работает


