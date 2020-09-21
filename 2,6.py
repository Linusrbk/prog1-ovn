svar = input('skriv in antalet sekunder:')
sek = int(svar)# svaret kan bara vara heltal
dag = sek // 86400
sek = sek % 86400
print ('rest från dagar:', sek)
tim = sek // 3600 # konverterar sitt svar fån sekunder till timmar om det går och ger tillbaka det som är över för att fortsätta uträkningarna 
sek = sek % 3600 # konverterat vad som är kvar efter timmarna är inräknade i sekunder
print ('rest från timmar:', sek)
min = sek // 60 # gör de sekunder som finns till minuter 
sek = sek % 60 # konverterat vad som är kvar efter minuterna är inräknade i sekunder
print ('rest från minuter:', sek)
print('dagar:',dag)
print('timmar:', tim)
print('minuter: ', min)
print('sekunder:', sek)