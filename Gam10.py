import random
import time
while True:
    #Codigo Hadooken :V
    #Gambling
    #RNG = input()
    a = random.randint(1,5)
    if (a != 1):
        print("")
        b = random.randint(1,20)
        if (b != 1):
            print("")
            c = random.randint(1,50)
            if (c != 1):
                print("")
                d = random.randint(1,75)
                if (d != 1):
                    print("")
                    e = random.randint(1,150)
                    if (e != 1):
                        print("")
                        f = random.randint(1,500)
                        if (f != 1):
                            print ("")
                            g = random.randint(1,750)
                            if (g != 1):
                                print("")
                                h = random.randint(1,1000)
                                if (h != 1):
                                    print("")
                                    i = random.randint(1,2000)
                                    if (i != 1):
                                        j = random.randint(1,5000)
                                        if (j != 1):
                                            print("")
                                        else:
                                            print("Celestial 1 em 5000")
					    time.sleep(1)
                                    else:
                                        print("Divino 1 em 2000")
                                else:
                                    print("Exótico 1 em 1000")
                            else:
                                print("Arcano 1 em 750")
                        else:
                            print("Mìtico 1 em 500")
                    else:
                        print("Lendário 1 em 150")
                else:
                    print("Épico 1 em 75")
            else:
                print("Raro 1 em 50")
        else:
            print("Incomum 1 de 10")
    else:
        print("Comum 1 de 3")
