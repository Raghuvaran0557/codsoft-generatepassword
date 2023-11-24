import random
import string
def create_password(length, complexity):
    if complexity == "1":
        characters = string.ascii_letters + string.digits
    elif complexity == "2":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "3":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation
    else:
        print("Invalid complexity level. Using default: 'medium'")
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Password Generator")
    print("------------------")
    while True:
        try:
            size = int(input("Enter the desired size of the password: "))
            if size <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    complexity = input("1->easy\n2-> medium\n3->hard\nEnter the complexity level:").lower()
    password = create_password(size, complexity)
    print("\nGenerated Password:")
    print(password)
if __name__ == "__main__":
    main()
