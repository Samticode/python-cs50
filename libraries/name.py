import sys

if len(sys.argv) < 2:
    sys.exit("For Få cuh")
    
for arg in sys.argv[1:]:
    print("Hello", arg)