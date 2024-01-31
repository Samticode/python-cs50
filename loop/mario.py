
def main():
    n = int(input("Please enter a number: "))
    # bricks(n)
    # rows(n)
    blocks(n)
    
def blocks(n):
    for i in range(n):
        print("#   " * n, end="\n\n")

    
def rows(n):
    print("?" * n)

def bricks(n):
    # for _ in range(n):
    #     print("#")
    print("#\n" * n, end="")
        

main()