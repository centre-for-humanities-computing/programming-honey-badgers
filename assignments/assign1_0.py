j = 0
while j < 2:
    i = 10
    for i in range(1, i, 1):
        print('*'*i)
    for i in range(i-1, 0, -1):
        print('*'*i)
    j += 1