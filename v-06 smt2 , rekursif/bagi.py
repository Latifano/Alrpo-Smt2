''' IKROMI LATIFANO | A11.2020.12667 | 4209 '''


def rek_bagi(x, y):
    i = x
    result = 0
    while i > 0:
        i = i - y
        result = result + 1  # result ++
    return result


print(rek_bagi(48, 6))
'''
    i = 48
    while i > 0:
        True
    --> i = 48 - 6 = 42 True
        result = 0 + 1 = 1

    --> i = 42 - 6 = 36 True
        result = 1 + 1 = 2

    --> i = 36 - 6 = 30 True
        result = 2 + 1 = 3

    --> i = 30 - 6 = 24 True
        result = 3 + 1 = 4

    --> i = 24 - 6 = 18 True
        result = 4 + 1 = 5

    --> i = 18 - 6 = 12 True
        result = 5 + 1 = 6

    --> i = 12 - 6 = 6 True
        result = 6 + 1 = 7

    --> i = 6 - 6 = 0 False
        result = 7 + 1 = 8
        
    --> return result // return 8
        '''


def rek_bagi2(x, y):
    i = x
    result = 0
    while i > 0:
        i = i - y
        result = result + 1  # result ++
    return result


print(rek_bagi2(20, 10))

'''
    i = 20
    while i > 0:
        True
    --> i = 20 - 10 = 10 True
        result = 0 + 1 = 1

    --> i = 10 - 10 = 0 False
        result = 1 + 1 = 2

    --> return result // return 2
    '''
