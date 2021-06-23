def rek_faktorial(x):
    if x == 1:
        return 1
    else:
        return x * rek_faktorial(x - 1)


print(rek_faktorial(5))
'''
x = 5
x == 1 ? False
return x * faktorial(x - 1)
return 5 * faktorial(5 - 1)

x = 4
x == 1 ? False
return x * faktorial(x - 1)
return 5 * 4 * faktorial(4 - 1)

x = 3
x == 1 ? False
return x * faktorial(x - 1)
return 5 * 4 * 3 * faktorial(3 - 1)

x = 2
x == 1 ? False
return x * faktorial(x - 1)
return 5 * 4 * 3 * 2 * faktorial(2 - 1)

x = 1
x == 1 ? True
return x * faktorial(1)
return 5 * 4 * 3 * 2 * return 1
return 5 * 4 * 3 * 2 * 1 = 120

Jadi, 5! adalah 120
'''


def rek_faktorial2(x):
    if x == 1:
        return 1
    else:
        return x * rek_faktorial2(x - 1)


print(rek_faktorial2(4))

'''
x = 4
x == 1 ? False
return x * faktorial(x - 1)
return 4 * faktorial(4 - 1)

x = 3
x == 1 ? False
return x * faktorial(x - 1)
return 4 * 3 * faktorial(3 - 1)

x = 2
x == 1 ? False
return x * faktorial(x - 1)
return 4 * 3 * 2 * faktorial(2 - 1)

x = 1
x == 1 ? True
return x * faktorial(1)
return 4 * 3 * 2 * return 1
return 4 * 3 * 2 * 1 = 24

Jadi, 4! adalah 24
'''
