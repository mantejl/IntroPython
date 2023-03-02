# NAME: Mantej Lamba
# ID: 2259394598
# DATE: 2022-09-19
# DESCRIPTION: practicing working with string methods

def check_string(str_check: str):
    # checking if the string only has alphabetic characters
    alpha = str_check.isalpha()
    print ("Only alphabetic characters? " + str(alpha))
    # checking if the string only has numbers
    numbers = str_check.isnumeric()
    print ("Only numbers? " + str(numbers))
    # checking if the string only has lowercase letters
    lowercase = str_check.islower()
    print("Only lowercase? " + str(lowercase))
    # checking if the string only has uppercase letters
    uppercase = str_check.isupper()
    print("Only uppercase? " + str(uppercase))

def check_palindrome(str_check: str):
        # reversing reversing the string
        s = str_check[::-1]
        # checking if the reversed string is equal to the input string
        if ( str_check == s):
            print("The string " + str_check + " IS a palindrome!")
        else:
            print("The string " + str_check + " is NOT a palindrome!")



def main():
    input_string = input("Enter a string: ")
    check_string(input_string)
    check_palindrome(input_string)


if __name__ == "__main__":
    main()