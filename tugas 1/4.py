def is_palindrome(word):
    palindrome = str()
    for i in word[::-1]:
        palindrome += i
    if palindrome == word:
        return "True"
    else:
        return "False"
        
print(is_palindrome("rotator"))