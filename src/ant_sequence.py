from itertools import groupby

def find_middle_two(n):
    s = "1"

    for _ in range(1, n):
        next = ""
        for key, group in groupby(s):
            g = list(group)
            next += f"{len(g)}{key}"
        s = next

    return s[len(s)//2 - 1 : len(s)//2 + 1]