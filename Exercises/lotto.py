losowania=[]
 
def read_data():
    file = open('dl.txt', 'r')
    linia = file.readlines()
   
    for x in linia:
        a,b,c=x.split(" ")
        losowania.append(c.rstrip('\n'))
        
 
def check():
    print("Wprowadź 6 liczb z przedziału 1-49 oddzielonych spacją :")
    while True:
        liczby = input("--> ")
        numer=liczby.split(" ") 
        sprawdz_liczbe=0
        for l in range(len(numer)):
            if numer[l].isdecimal() and int(min(numer))>=1 and int(max(numer))<50:
                sprawdz_liczbe+=1
                continue
            else:
                break
       
        if len(numer)==6 and sprawdz_liczbe==6:
            break
        elif len(numer)<6:
            print("Wpowadziłeś za mało liczb")
            continue
        elif len(numer)>6:
            print("Wpowadziłeś za dużo liczb")
            continue
        elif sprawdz_liczbe<6:
            print("Musisz podać tylko liczby z przedziału od 1 do 49")
            continue
        else:
            print("Liczby zostały wpowadzone niepawidłowo")
            continue
       
       
    trafienia = {"0" : 0, "1" : 0,"2" : 0,"3" : 0, "4" : 0, "5" : 0, "6" : 0}
    for k in range(len(losowania)):
        set1=set(numer) 
        set2=set(losowania[k].split(",")) 
        set3=set1&(set2) 
        if len(set3) == 0:
            trafienia["0"] += 1
        elif len(set3) == 1:
            trafienia["1"] += 1
        elif len(set3) == 2:
            trafienia["2"] += 1
        elif len(set3) == 3:
            trafienia["3"] += 1
        elif len(set3) == 4:
            trafienia["4"] += 1
        elif len(set3) == 5:
            trafienia["5"] += 1
        elif len(set3) == 6:
            trafienia["6"] += 1
    print ("RAPORT TRAFIEŃ".center(20, '-'))
    print("(0) trafiono".ljust(16, '.'),str(trafienia["0"]).rjust(4, ' '))
    print("(1) trafiono".ljust(16, '.'),str(trafienia["1"]).rjust(4, ' '))
    print("(2) trafiono".ljust(16, '.'),str(trafienia["2"]).rjust(4, ' '))
    print("(3) trafiono".ljust(16, '.'),str(trafienia["3"]).rjust(4, ' '))
    print("(4) trafiono".ljust(16, '.'),str(trafienia["4"]).rjust(4, ' '))
    print("(5) trafiono".ljust(16, '.'),str(trafienia["5"]).rjust(4, ' '))
    print("(6) trafiono".ljust(16, '.'),str(trafienia["6"]).rjust(4, ' '))
    if trafienia["6"] == 0:
        print("\nNiestety nie trafiłeś 6 liczb, spróbuj ponownie:")
        check()
    else:
        print("\nWYGRAŁEŚ 2.000.000 zł!!!\n")
        print("Spóbuj ponowanie wygrać:")
        check()
   

read_data()
check()
