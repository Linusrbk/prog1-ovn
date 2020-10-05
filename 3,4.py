t = float(input('temp?'))
if t < 18:
    print('det är kallt')
    print('sätt på värmen')
    if t < 12:
        print('sätt på jackan')
        if t < 4:
            print('ta på dig din varmsta jacka')
else:
    print('det är varmt')
    if t >= 22:
        print('stäng av värmen')
        if t >= 30:
            print('dags att ta av sig kläderna')
print(f'Det är {t:.1f} grader')