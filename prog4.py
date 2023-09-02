
input_string = str(input("Enter a string to check: "))
rev = input_string[::-1]
if input_string == rev:
    print(rev + " is Palindrome")
else:
    print(rev + " is not Palindrome")
