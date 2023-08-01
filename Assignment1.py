def print_shortest_substrings(s, x):
    v1 = []
    v2 = []
    smallest = ""
    txt = ""
    index=0
    for i in range(len(s)):
        txt += s[i]
        for j in range(i+1, len(s)):
            txt += s[j]
            if s[i] == s[j] and len(txt) < x:
                break
            if len(txt) >= x and txt[-1] == s[i]:
                v1.append(txt)
                break
        txt = ""
    for i in range(len(v1)):
        if len(v1[i]) == x:
            print(v1[i], end=" ")
            index = -1
    if index == 0 and len(v1) == 0:
        print("not-found")
    elif index == 0:
        l = len(v1[0])
        for i in range(1, len(v1)):
            if l > len(v1[i]):
                l = len(v1[i])
        for i in range(len(v1)):
            if len(v1[i]) == l:
                print(v1[i], end=" ")

s = "abccdbacca"
x = 3
print_shortest_substrings(s, x)
