def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print (fib(5))
# x == 0 or x == 1: False
# return fib(x-1) + fib(x-2)
# return fib(5-1) + fib(5-2)

# fib(4) + fib(3): semua false
# return fib(4-1) + fib(4-2) 
# + return fib(4-1) + fib(4-2)

# fib(4-1) + fib(4-2) + fib(3-1):False + fib(3-2): True
# return fib(3-1) + fib(3-2)
# + return fib(2-1) + fib(2-2)
# + return fib(3-1) + fib(3-2)
# + return fib(1-1) + return 1

# return fib(3-1):False + fib(3-2):True + return fib(2-1):True + fib(2-2):True + return fib(3-1):False + fib(3-2):True + return fib(1-1):True + return 1
# return fib(2-1) + fib (2-2)
# + return 1
# + return 1
# + return 1
# return fib(2-1) + fib (2-2)
# + return 1
# + return 1
# + return 1

# return fib(2-1): true + fib (2-2):true + return 1 + return 1 + return 1 return fib(2-1):true + fib (2-2):true + return 1 + return 1 + return 1
# return  1
# return  1
# return  1
# return  1

# return  1
# return  1
# return  1
# return  1