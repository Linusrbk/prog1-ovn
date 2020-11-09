varv = 0 
x=int(input('vad är x:'))
y=2*x**2 - 5*x + 1
for i in range(-10,11,y):
    i=float(i/10)
    varv = varv+1
    print(i)

print('gåt', varv, 'varv')