x = int(input('Введіть ціле позитивне 5-значне число: '))
a = x % 10
b = (x // 10) % 10
c = (x // 100) % 10
d = (x // 1000) % 10
e = (x // 10000) % 10
print(a,b,c,d,e)