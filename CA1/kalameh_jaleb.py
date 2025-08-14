def solve(substring):
    letter_count = [0] * 10
    odd_count = 0

    for char in substring:
        letter_count[ord(char) - ord('a')] += 1
        

    for count in letter_count:
        if count % 2 == 1:
            odd_count += 1

    if odd_count <= 1:
        return True
    return False

def count_interesting_subsets(word):
    cnt = 0

    for i in range(len(word)):
        for j in range(i, len(word)):
            if solve(word[i:j+1]):
                cnt += 1

    return cnt

word = input()
result = count_interesting_subsets(word)
print(result)