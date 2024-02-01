import random

tails = 0
heads = 0
testes = 0

while True:
    testes += 1
    for i in range(2):
        coin = random.choice(['head', 'tail'])
        
        if coin == 'head':
            heads += 1
        else:
            tails += 1
            
    if heads == tails and testes > 100:
        break
    else:
        heads = 0
        tails = 0
        continue
        
print(f'Heads: {heads}, Tails: {tails}')
print(f'Testes: {testes}')