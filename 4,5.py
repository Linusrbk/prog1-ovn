höjd=float(input('hur långt ifråll golvet är din boll i meter?'))
varv = 0
while höjd >= 0.01:
    höjd = höjd * 0.7
    varv = varv+1
    print('din boll har stutsat ',varv ,'gånger ')
