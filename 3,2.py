ars=float(input('hur mycket kostar ett gyms årskort:'))
biljett=float(input('hur mycket ett gyms biljett kostar:'))
antal=int(input('hur många gånger du tänker gå på gym på ett år:'))
x=biljett*antal
if ars<x:
    print('det lönar det sig med att ta årskort') 
else:
    print('det lönar det sig inte med årskort')
