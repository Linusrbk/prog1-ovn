varv = 0 
x=int(input('vad är x:'))
y=2*x**2 - 5*x + 1
for i in range(-10,11,y):# den första är var den startade mitten är där den slutar och sista är hur många steg den tar per loop och i är en variabel
    varv = varv + 1
    
    print(i)
print('gåt', varv, 'varv')