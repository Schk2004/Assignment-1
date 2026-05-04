def max_cyclic_substring_sum(s):
    s2 = s + s
    n = len(s)

    char_set = set()
    left = 0
    curr_sum = 0
    max_sum = 0

    for right in range(len(s2)):
        while s2[right] in char_set or (right - left) >= n:
            char_set.remove(s2[left])
            curr_sum -= (ord(s2[left]) - ord('a') + 1)
            left += 1

        char_set.add(s2[right])
        curr_sum += (ord(s2[right]) - ord('a') + 1)

        max_sum = max(max_sum, curr_sum)

    return max_sum


# Taking user input
s = input("Enter string: ")
print(max_cyclic_substring_sum(s))