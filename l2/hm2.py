x = int(input('Введіть 4-значне число: '))
a = x // 1000
print(a)
left, right = divmod(x, 100)
b = left % 10
print(b)
left, right = divmod(x,  100)
c = right // 10
print(c)
left, d = divmod(x, 10)
print(d)