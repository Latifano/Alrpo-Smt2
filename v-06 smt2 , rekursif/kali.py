def kali(a,b):
	i = b						# i = 2
	result = 0					# res=0
	while i>0:					# 0 or less
		result = result + a
		i = i - 1
	return result # return 42

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)

mult(5,4)
#   a=5 b=4. b bukan 1, maka false
#   return a + mult(a, b-1)
#   return 5 + mult(5, 4-1)

#   a=5 b=3. b bukan 1, maka false
#   return a + mult(a, b-1)
#   5 + (return a + mult(a, b-1))
#   5 + (return 5 + mult(5, 3-1))

#   a=5 b=2. b belom 1, maka false
#   return return a + mult(a, b-1)
#   5 + 5 + (return a + mult(a, b-1))
#   5 + 5 + (return 5 + mult(5, 2-1))

#   a=5 b=1. b adalah 1, maka true
#   return a = return 5
#   5 + 5 + 5 + (return a)
#   5 + 5 + 5 + (return 5)
#   5 + 5 + 5 + 5 = 20

# mult(5,4) 
# = 5 + mult(5, 4-1) 
# = 5 + mult(5, 5 + mult(5, 3-1))
# = 5 + mult(5, 5 + mult(5, 5 + mult(5, 2-1)))
# = 5 + mult(5, 5 + mult(5, 5 + mult(5, 5 + mult(5, 1))))




mult(3,4)
#   3 + kali(3, 4-1)
#   a = 3, b = 4
#   if: b == 1 false

#   mult(a, b)
#   mult(3, 4-1) = mult(3, 3)

#   a + mult(a, b-1)
#   b=4, return 3 + mult(3, 4-1)
#   b=3, 3 + (return 3 + mult(3, 3-1))
#   b=2, 3 + 3 + (return 3 + mult(3, 2-1))
#   b=1, 3 + 3 + 3 + 3 = 12