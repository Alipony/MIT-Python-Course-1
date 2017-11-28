vowels = ['a', 'e', 'i', 'o', 'u']
vowelnum = 0
for sletter in range(0, len(s)):
    for vletter in range(0, len(vowels)):
        if s[sletter] == vowels[vletter]:
            vowelnum = vowelnum + 1
print(vowelnum)