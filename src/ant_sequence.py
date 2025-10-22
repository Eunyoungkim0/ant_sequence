def find_ant_sequence(n):
    pass


def find_middle_two(n):
    answer = find_ant_sequence(n)
    return answer[len(answer)//2-1:len(answer)//2+1]

