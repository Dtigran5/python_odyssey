ls = [1,2,3,4]
max = ls[0]
index = 0
for i in range(1,len(ls)):
    if ls[i] < max:
        max = ls[i]
        index = i
print(max)
print(index)
