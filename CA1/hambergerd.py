def solve(text):
    max_length = 0
    current_length = 0
    char_ind = {}

    for i in range(len(text)):
        if text[i] in char_ind and char_ind[text[i]] >= i - current_length:
            current_length = i - char_ind[text[i]]
        else:
            current_length += 1
        char_ind[text[i]] = i
        max_length = max(max_length, current_length)

    return max_length

inp = input()
result = solve(inp)
print(result)