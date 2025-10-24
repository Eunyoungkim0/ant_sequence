from itertools import groupby

#-------------------------------------------
# 첫 번째 풀이 시도
#-------------------------------------------
def find_ant_sequence(n):
    if n == 1:
        return "1"
    elif n == 2:
        return "11"

    prev = find_ant_sequence(n-1)
    curr = []

    for s in prev:
        if curr and curr[-1] == s:
            curr[-2] += 1
        else:
            curr.append(1)
            curr.append(s)

    return ''.join(map(str, curr))


def find_middle_two_1(n):
    answer = find_ant_sequence(n)
    return answer[len(answer)//2-1:len(answer)//2+1]


#-------------------------------------------
# 두 번째 풀이 시도
#-------------------------------------------
def find_middle_two(n):
    s = "1"

    for _ in range(1, n):
        next = ""
        for key, group in groupby(s):
            g = list(group)
            next += f"{len(g)}{key}"
        s = next

    return s[len(s)//2 - 1 : len(s)//2 + 1]
