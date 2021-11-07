def isPrime(x):
    '''
    determina daca un nr. este prim
    :param x: un numar intreg
    :return: True, daca x este prim sau False in caz contrar
    '''
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def testIsPrime():
    assert isPrime(-1) is False
    assert isPrime(0) is False
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(3) is True
    assert isPrime(4) is False
    assert isPrime(5) is True

def elementePrimeDinLista(l):
    '''
    determina elementele prime dintr-o lista
    :param l: lista de nr. intregi
    :return: o lista continand elementele prime din l
    '''
    rezultat = []
    for x in l:
        if isPrime(x):
            rezultat.append(x)
    return rezultat

def testElementePrimeDinLista():
    assert elementePrimeDinLista([]) == []
    assert elementePrimeDinLista([4,6,9]) == []
    assert elementePrimeDinLista([3,4,5]) == [3,5]

def printMenu():
    print("1. Citire lista")
    print("2. Afisare nr. prime")
    print("3. Iesire")

def citireLista():
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l

def main():
    testIsPrime()
    testElementePrimeDinLista()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(elementePrimeDinLista(l))
        elif optiune == "3":
            break
        else:
            print("Optiune gresita! Reincercati!")
main()