x = (2, 2, 2, 3 )
res = 'False'
for i in range(len(x)):
    if(x[i]!= x[0]):
        res = 'False'
        break
    else:
        res = 'True'

print(res)

