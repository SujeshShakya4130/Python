# Checking if the string is palindrome or not.

string_check = input("Enter a String: ")
string_check = string_check.lower()
if string_check == string_check[::-1]:
    print("It is a Palindrome.")

else:
    print("It is not a palindrome.")
