def liczby(licz1,licz2,licz3,licz4):
    lista=[licz1,licz2,licz3,licz4]
    
    suma=0
    for i in range(3):
        maxv=max(lista)
        lista.remove(maxv)
        suma+=maxv
 
    print ("Średnia arytmetyczna wynosi: ",suma/3)
    
