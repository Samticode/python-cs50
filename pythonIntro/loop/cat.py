
i = 0

# while i < 3:
#     print(i)
#     i += 1 
    
# for i in [0, 1, 2]:
#     print(i)

# for _ in range(5):
#     print(_)
    
    
def main(): 
    number = get_number()
    meow(number)
    
    
    
def get_number(): 
    while True:
        n = int(input("Please enter a number: "))
        if n > 0:
            break
    return n


    
    
def meow(n):
    for _ in range(n):
        print("Meow")


    
main()