import random
import string

#DEFINE POSSIBLE CHARACTER FOR THE PASSWORD
def generate_password(length):
    character= string.ascii_letters + string.digits + string.punctuation

#GENERATE RANDOM PASSWORD
    password="".join(random.choice(character)  for _ in 
    range(length))
    return password

#PROMPT USER TO DEFINE THE LENGTH OF PASSWORD
def main():
    print("---password generator---")
    try:
        length=int(input("Enter the length of the password:"))
        if length<=0:
                print("Password length must be a positive value")
        else:
            password = generate_password(length)
            print("Generated_Password:",password)
    except ValueError:
        print("invalid input! please enter a valid number.")
main()