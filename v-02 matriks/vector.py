def Add2Vectors(v1, v2):
    v3 = []
    if len(v1) != len(v2):
        return -1
    else:
        for i in range(len(v1)):
            v3.append(v1[i]+v2[i])
    return v3


print(Add2Vectors([3, 4, 5], [10, 20, 30]))
