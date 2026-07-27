string = input("Enter a string: ")

reverse = string[::-1]

if string == reverse:
    print("Palindrome String")
else:
    print("Not a Palindrome String")
