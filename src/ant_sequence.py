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


def find_middle_two(n):
    answer = find_ant_sequence(n)
    return answer[len(answer)//2-1:len(answer)//2+1]

