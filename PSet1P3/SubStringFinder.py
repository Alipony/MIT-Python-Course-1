s = list(s)
ss = list('bob')
bobnum = 0
for i in range(len(s) - len(ss) + 1):
    if (s[i:i+len(ss)] == ss):
        bobnum += 1
print('Number of times bob occurs is: ' + str(bobnum))