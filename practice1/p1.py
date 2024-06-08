ls = [1,2,3,4]
max = ls[0]
for i in range(1,len(ls)+1):
    if max < i:
        max = i
print(max)