import random
import string

def Password_gen(len):
    character = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(character) for _ in range(len))

def main():
    while True:
        try:
            len = int(input("Enter the desired length of the password: "))
            if len <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as error:
            print(f"Invalid input: {error}. Please enter a positive integer.")

    pword = Password_gen(len)
    print("Generated password:", pword)
5
if __name__ == "__main__":
    main()
