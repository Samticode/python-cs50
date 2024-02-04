import re

name = input("Enter your name: ").strip()
re.search(r'^[A-Za-z]+$', name)
    
