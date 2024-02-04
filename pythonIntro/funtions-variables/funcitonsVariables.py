def main():
    x = int(input("Enter a number for X: "))
    print("X squared is", square(x))

def square(n):
    return pow(n, 3)


main()