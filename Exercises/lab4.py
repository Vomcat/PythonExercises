print ("Wprowadz 2 napisy:")
tab = []
 
while len(tab) < 2:
    s = input("--> ")
    tab.append(s)

listnapis1=list(tab[0])
listnapis2=list(tab[1])
 
A = set(listnapis1)
B = set(listnapis2)
 
print ("Wszystkie znaki:\n",A|B)
print ("Wszystkie znaki osobno:")
print (A)
print (B)
print ("Znaki które się znajdują w dwóch napisach:\n",A&B)

