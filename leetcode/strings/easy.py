# reverse string
my_str = ["h", "e", "l", "l", "o"]

my_str.reverse()

idx = 0
mid = len(my_str) // 2
while idx != mid:
    tmp = my_str[idx]
    my_str[idx] = my_str[-(idx+1)]
    my_str[-(idx + 1)] = tmp
    idx += 1

# reverse integer
x = 123
multiplier = -1 if x < 0 else 1
int(''.join(reversed(str(abs(x))))) * multiplier


# first unique character
s = "loveleetcode"
s = "aadadaad"

dct = {'unique': {}, 'double': {}}
last_non_repeating = None
for i in range(0, len(s)):
    if s[i] not in dct:
        dct['unique'][s[i]] = i
    else:
        dct.pop(s[i])

    list(dct.items())[0][1]
