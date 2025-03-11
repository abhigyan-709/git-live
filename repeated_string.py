# Write a function  to find the longest substring without repeating characters.

"abcdabcaba"

"abcd"

# time complexity = O(n) range = 10 r = 
"thisisourstring"
def longest_unique_string(s):
    new_set = set() # empty set creating
    l = 0
    maximum_length = 0

    for r in range(len(s)): # for r in range(10):
        while s[r] in new_set:
            new_set.remove(s[l])
            l += 1
        new_set.add(s[r])
        maximum_length = max(maximum_length, r - l + 1)

    return maximum_length

print(longest_unique_string("abc-abcd-abcd-abcd-a-bcasxyzqrt"))

# s = "thisisourstring"
# s[r] index 0 t, h
# set() - t, add
# set() - index 10 - t