def main():
    x = int(input("Whats your number? "))

    if is_even(x) == True:
        print("even")
    else:
        print("odd")
        
        
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


        
main()