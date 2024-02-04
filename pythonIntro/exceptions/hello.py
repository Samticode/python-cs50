def main():
    x = get_int()
    print(f"Hello, {x}!")
        

def get_int():
    while True:        
        try:
            return(int(input('Enter the first number: ')))
        except ValueError:
            print('Oops! That was no valid number. Try again...')

        
        
main()

