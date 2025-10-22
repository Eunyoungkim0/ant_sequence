def find_ant_sequence(n):
    if n == 1:
        return "1"
    elif n == 2:
        return "11"

    prev = find_ant_sequence(n-1)
    curr = []
    stack = []

    for s in prev:
        if not stack:
            stack.append(s)
        else:
            if s == stack[-1]:
                stack.append(s)
            else:
                curr.append(str(len(stack)))
                curr.append(stack[-1])
                stack.clear()
                stack.append(s)

    if stack:
        curr.append(str(len(stack)))
        curr.append(stack[-1])

    return ''.join(curr)


def find_middle_two(n):
    answer = find_ant_sequence(n)
    return answer[len(answer)//2-1:len(answer)//2+1]

