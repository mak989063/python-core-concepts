def check_palindrome(string, start, end):
    # Ensure 'end' isn't bigger than the last valid index
    end = min(end, len(string) - 1)

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

print(check_palindrome("malayalam",0,9))
print(check_palindrome("anamadamspe",3,7))