def solution(s):
    answer = ''
    alpha = ''
    alpha_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for c in s:
        if c.isdigit():
            answer += c
            alpha = ''
        else:
            alpha += c
            if alpha in alpha_list:
                answer += str(alpha_list.index(alpha))
                alpha = ''

    return int(answer)
