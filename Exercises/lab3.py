inventory={'lina': 1, 'pochodnia': 6, 'złota moneta': 142,'sztylet' : 1, 'strzała': 12}
 
def printInventory(invDict,leftw,rightw):
   
   
    sumap=leftw+rightw
    print ("PRZEDMIOTY".center(sumap, '-'))
   
    for i in invDict:
        print("klucz",invDict[i])
        zrobstr=str(invDict[i])
        print(i.ljust(leftw, '.'),zrobstr.rjust(rightw, ' '))

