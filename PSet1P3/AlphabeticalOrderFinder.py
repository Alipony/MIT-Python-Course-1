s = list(s)
bignum = [0,0]
for i in range(len(s)+1):
    for x in range(i, len(s)+1,1):
        clones = s[i:x]
        clones.sort()
        if s[i:x] == clones:
            if x - i > bignum[1] - bignum[0]:
                bignum = [i, x]
        else:
            break
print("Longest substring in alphabetical order is: " + ''.join(s[bignum[0]:bignum[1]]))