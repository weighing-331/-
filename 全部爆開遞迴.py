
def valid(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1  
    valid_perms = 0
    

    def backtrack(prev_char, length):
        nonlocal valid_perms
        if length == len(s):
            valid_perms += 1
            return
        for char in char_count:
            if char_count[char] > 0 and char != prev_char:
                char_count[char] -= 1
                backtrack(char, length + 1)
                char_count[char] += 1

    backtrack('', 0)
    return valid_perms

def nei(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1  
    neig = 1
    for i in range(1, len(char_count)+1):
        neig *= i
    return neig
    

s = input()
print(f"同字不相鄰：{valid(s)}")

print(f"同字相鄰：{nei(s)}")