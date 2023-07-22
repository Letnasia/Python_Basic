x = int(input('Введіть 4-значне число: '))
a = x // 1000
left, right = divmod(x, 100)
b = left % 10
left, right = divmod(x,  100)
c = right // 10
left, d = divmod(x, 10)
print(a)
print(b)
print(c)
print(d)