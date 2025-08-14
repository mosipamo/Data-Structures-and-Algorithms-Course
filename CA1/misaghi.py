def solve(a, b, s):
    if not s:
        return True
    
    c = a + b
    c_str = str(c)
    
    if s.startswith(c_str):
        return solve(b, c, s[len(c_str):])
    
    return False

def is_misagh_sequence(s):
    for i in range(1, len(s)):
        for j in range(i + 1, len(s)):
            a_str = s[:i]
            b_str = s[i:j]
            
            if (b_str[0] == '0' and len(b_str) > 1):
                continue
            
            a = int(a_str)
            b = int(b_str)
            
            if solve(a, b, s[j:]):
                return "YES"
    return "NO"

inp = input()
result = is_misagh_sequence(inp)
print(result)
