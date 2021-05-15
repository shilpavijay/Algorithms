
def palindrome(a):
    a=a.lower()
    b=a[::-1]
    if a==b:
        print("palindrome")
    else:
        print("Not a Palindrome")