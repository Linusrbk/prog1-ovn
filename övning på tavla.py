#ett program son tar heltals input och skriver ut jämnt eller ojämnt
inmatning = int(input('skriv in ett heltal:' ))
svar = inmatning % 2 
if svar == 1:
    print(f'talet {inmatning} är ojämnt. ')
else : 
    print (f'talet {inmatning} är jämnt')