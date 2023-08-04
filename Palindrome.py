def Palindrome(val):
    val = input("enter the word")
    if val == val[::-1]:
        print("Yes")
    else:
        print("No")
Palindrome("")