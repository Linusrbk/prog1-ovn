tid=float(input('hur många minuter per månader:'))
pengar=float(input('hur mycket det kostar i minuten:'))
y= tid*pengar
if y> 300:
    y=y*0.9
    print(f'så här mycket kostar det {y:.1f}')
else:
    print(f'så här mycket kostar det {y:.1f}')