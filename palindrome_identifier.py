s = input("Zadaj slovo :")

def is_palindrome(s):
    x = list(s)
    x.reverse()
    reversed_s = "".join(x)
    return s == reversed_s

result = is_palindrome(s)
print(result)
