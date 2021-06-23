def rek_pangkat(x, y):
    if y == 1:
        return x
    else:
        return x * rek_pangkat(x, y - 1)


print(rek_pangkat(2, 5))

'''
x = 2 , y = 5
y == 1 ? False
return x * rek_pangkat(x, y-1)
return 2 * rek_pangkat(2, 5-1) 

x = 2, y = 4
y == 1 ? False
return x * rek_pangkat(x, y-1)
return 2 * 2 * (rek_pangkat(2, 4-1))

x = 2, y = 3
y == 1 ? False
return x * rek_pangkat(x, y-1)
return 2 * 2 * 2 *(rek_pangkat(2, 3-1))

x = 2, y = 2
y == 1 ? False
return x * rek_pangkat(x, y-1)
return 2 * 2 * 2 * 2 (rek_pangkat(2, 2-1))

x = 2, y = 1
y == 1 ? True
return 2 * 2 * 2 * 2 * (return x)
return 2 * 2 * 2 * 2 * (return 2)
return 2 * 2 * 2 * 2 * 2 = 32
Jadi, 2 pangkat 5 adalah 32

'''


def rek_pangkat2(x, y):
    if y == 1:
        return x
    else:
        return x * rek_pangkat2(x, y-1)


print(rek_pangkat2(5, 4))
'''
x = 5 , y = 4
y == 1 ? False
return x * rek_pangkat2(x, y-1)
return 5 * rek_pangkat2(5, 4-1) 

x = 5, y = 3
y == 1 ? False
return x * rek_pangkat2(x, y-1)
return 5 * 5 * (rek_pangkat2(5, 3-1))

x = 5, y = 2
y == 1 ? False
return x * rek_pangkat2(x, y-1)
return 5 * 5 * 5 * (rek_pangkat2(5, 2-1))

x = 5, y = 1
y == 1 ? True
return 5 * 5 * 5 * (return x)
return 5 * 5 * 5 * (return 5)
return 5 * 5 * 5 * 5 = 625

Jadi, 5 pangkat 4 adalah 625
'''
