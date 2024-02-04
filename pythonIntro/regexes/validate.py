import re

def main():
    email = input("What is your email? ").strip()

    if re.search(r"^\w+@\w+\.com$", email, re.IGNORECASE):
        print("Valid email")
    else:
        print("Invalid email")
        

if __name__ == "__main__":
    main()