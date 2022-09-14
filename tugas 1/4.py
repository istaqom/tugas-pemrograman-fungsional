def is_palindrome(word):
    palindrome = word[::-1]
    if palindrome == word:
        return "True"
    else:
        return "False"
        
print(is_palindrome("rotator"))