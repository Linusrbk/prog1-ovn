import random
y=float #rullar en tärning sen frågar om man vill rulla igen tills man svarar n
while y == float :

    n = random.randint(1,6)
    
    print(n)
    y=input('stoppa j = [ja] eller n = [nej]?')
    if y == 'j': 
        y = str
    elif y == 'n':
        y=float
print('äntligen')