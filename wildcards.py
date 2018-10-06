def Wildcards(s):
    output = True

    s.replace('}', '')

    special_char = ['+', '*', '{', '}', '$']

    # code goes here
    # last_ind = 0
    # for _ in range(len(s)):
    #     val = s[_]
    #     if val in special_char:
    #         last_ind = _
    #
    # wildcard = s[:last_ind + 1]
    # exp_str = s[last_ind + 1:]

    substr = s.split(' ')

    wildcard = substr[0]
    exp_str = substr[1]

    rep_char = ''

    rep_hold = 0
    temp_hold = 0

    for _ in range(len(wildcard)):
        print(output)
        print(wildcard[_])
        if temp_hold:
            rep_hold = int(wildcard[_])

            step = 0
            while rep_hold - 1:
                output = output and exp_str[_ + step] == rep_char
                step += 1
                rep_hold -= 1

            exp_str.replace(rep_char * rep_hold, rep_char, 1)
            temp_hold -= 1
            continue

        card = wildcard[_]
        if card == '+':
            output = output and exp_str[_].isalpha()
        elif card == '$':
            output = output and exp_str[_].isdigit()
        elif card == '{':
            rep_char = exp_str[_]
            temp_hold += 1
            continue

    return str_bool(output)


def str_bool(x):
    if x:
        return 'true'

    return 'false'


# keep this function call here
print(Wildcards("$**+*{2} 9mmmrrrkbb"))
















