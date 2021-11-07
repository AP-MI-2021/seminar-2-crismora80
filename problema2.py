def toateElementeleDivizbileCu10(l):
    '''
    determina daca toate nr. dintr-o lista sunt diviziile cu 10
    :param l: lista de nr. intregi
    :return: True, daca toate nr. din l sunt divizibile cu 10 sau False, in caz contrar
    '''
    for x in l:
        if x % 10 != 0:
            return False
    return True

def testToateElementeleDivizbileCu10():
    assert toateElementeleDivizbileCu10([]) is True
    assert toateElementeleDivizbileCu10([10,4,5]) is False
    assert toateElementeleDivizbileCu10([10,20]) is True

def subsecventaMaxELmenteDivizibileCu10(l):
    '''
    determina cea mai lunga subsecventa de nr. divizibile cu 10
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. divizibile cu 10 din l
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toateElementeleDivizbileCu10(l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j+1]
    return subsecventaMax

def testSubsecventaMaxELmenteDivizibileCu10():
    assert subsecventaMaxELmenteDivizibileCu10([]) == []
    assert subsecventaMaxELmenteDivizibileCu10([1,2,3]) == []
    assert subsecventaMaxELmenteDivizibileCu10([11,10,12]) == [10]
    assert subsecventaMaxELmenteDivizibileCu10([10,20,3,10]) == [10,20]

def printMenu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa de nr. divizibile cu 10")
    print("3. Iesire")

def citireLista():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def main():
    testSubsecventaMaxELmenteDivizibileCu10()
    testToateElementeleDivizbileCu10()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(subsecventaMaxELmenteDivizibileCu10(l))
        elif optiune == "3":
            break
        else:
            print("Optiune gresita! Reincercati!")
main()

'''
l = [1,2,3,4]

[1]
[1,2]
[1,2,3]
[1,2,3,4]

[2]
[2,3]
[2,3,4]

[3]
[3,4]

[4]

l[i:j+1]
'''