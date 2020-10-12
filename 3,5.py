a = int(input('ett blevs längd i mm:'))
b = int(input('ett blevs bredd i mm:'))
c = int(input('ett blevs tjocklek i mm:'))
if a<601 and a>139 and c<101 and b>89 and a + b + c <901:
    d = a + b + c
    print('ditt brev är inom dom tillåtna måtten ',d,'mm')
else:
    print('ditt brev är inte inom dom tillåtna gränserna')
