def licz(slowo):
    listax=[]
    slownik={}
    slownikodwrocony={}
 
    for i in range(len(slowo)):
        if (slowo[i] not in listax):
            listax.append(slowo[i])
 
    for i in range(len(listax)):
        slowo3=slowo.count(listax[i])
        print(type(slowo3))
        slownik[listax[i]]=slowo3
        print (listax[i]," --> ",slowo3)
 
    print ("Słownik:\n",slownik)
 
    slownikodwrocony = dict([(value, [key for key,v in slownik.items() if v==value]) for value in set(slownik.values())])
    
    print ("Odwrócony słownik:\n",slownikodwrocony)

