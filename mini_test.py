num = list(reversed(range(1, 101)))

for n in num:
    if n % 3 == 0 & n % 5 == 0:
        print('FooBar', end=' ')
    elif n % 3 == 0:
        print('Foo', end=' ')
    elif n % 5 == 0:
        print('Bar', end=' ')
    else:
        print(n, end=' ')