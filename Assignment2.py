def find_ascii(s):
    v1 = []
    for i in range(len(s)):
        a = ord(s[i])
        v1.append(a)
    v2 = [0] * len(v1)
    for i in range(len(v1)):
        if v1[i] % 2 == 0:
            if i + 1 <= len(v1) - 1 and v2[i + 1] == 0:
                r = v1[i] % 7
                v1[i + 1] = v1[i + 1] + r
                v2[i + 1] = -1
                if not (v1[i + 1] >= 0 and v1[i + 1] <= 127):
                    v1[i + 1] = 83
        elif v1[i] % 2 != 0:
            if i - 1 >= 0 and v2[i - 1] == 0:
                r = v1[i] % 5
                v1[i - 1] = v1[i - 1] - r
                v2[i - 1] = -1
                if not (v1[i - 1] >= 0 and v1[i - 1] <= 127):
                    v1[i - 1] = 83
    for i in range(len(v1)):
        print(chr(v1[i]),end="")

s = "sHQen}"
find_ascii(s)
