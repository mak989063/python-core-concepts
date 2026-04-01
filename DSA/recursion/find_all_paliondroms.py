"""
Given a string s, find all possible ways to partition it such that every substring in the partition
is a palindrome.

Examples:

Input:  s = "geeks"
Output: [[g, e, e, k, s], [g, ee, k, s]]
Explanation: [g, e, e, k, s] and [g, ee, k, s] are the only partitions of "geeks" where each substring is a palindrome.

Input:  s = "abcba"
Output: [[a, b, c, b, a], [a, bcb, a], [abcba]]
Explanation: [a, b, c, b, a], [a, bcb, a] and [abcba] are the only partitions of "abcba" where each substring is a palindrome.

"""
# Check if the string is a palindrome
def isPalindrome(s):
    return s == s[::-1]

# Backtracking function to generate all palindromic partitions
def backtrack(idx, s, curr, res):
    if idx == len(s):
        # Save the current valid partition
        res.append(curr[:])
        return

    temp = ""
    for i in range(idx, len(s)):
        temp += s[i]
        if isPalindrome(temp):
            # Choose substring
            curr.append(temp)
            # Explore further
            backtrack(i + 1, s, curr, res)
            # Backtrack
            curr.pop()

# Generate all palindromic partitions and sort them
def palinParts(s):
    res = []
    backtrack(0, s, [], res)
    return res

if __name__ == "__main__":
    s = "geeks"
    res = palinParts(s)
    for part in res:
        print(" ".join(part))


