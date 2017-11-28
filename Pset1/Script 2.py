"""Substring finder"""
s = input("String to search through: ")
s = list(s)
ss = list(input("Sub String to search for: "))
SSnum = 0
for i in range(len(s) - len(ss) + 1):
    if (s[i:i+len(ss)] == ss):
        SSnum += 1
print('Number of times bob occurs is: ' + str(bobnum))
