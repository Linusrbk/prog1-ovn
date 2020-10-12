print('skriv ja eller nåt annat på frågorna! man ska inte använda stora bokstäver för ja')
m = input('Vill du vakna? ')
if m == 'ja':
    j = input('Vill du äta något? ')
    if j == 'ja':
        i = input('Vill du fara iväg till skolan? ')
        if i == 'ja':
            print('Grattis du är ett vanligt barn!')
        else:
            print('Du är ett barn som alltid misslyckar på det tu tänker göra och kommer alltid vara')
    else: 
        print('Du dör av hunger och kommer inte fram till skolan')
    
else:
    print('Du blir sen till skolan och är ett dåligt exempel ')