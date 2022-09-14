def is_palindrome(word):
    word = ''.join(i for i in word.lower() if i.isalnum())
    palindrome = word[::-1]
    if palindrome == word:
        return "True"
    else:
        return "False"
        
print(is_palindrome("rotator"))