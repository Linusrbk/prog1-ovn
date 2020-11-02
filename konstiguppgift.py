import random
gissa = 0
number= 0
rando=random.randint(1,10)
while gissa!=rando:
    number+=1
    gissa = int(input ('skriv gissning'))
    
    if gissa < rando:
        print('för litet')
    
    elif gissa>rando:
        print('för mycket')
        
    elif gissa==rando:
        print('bra svar', number,'gissningar gjorda')
        