from Domain.rezervari import toString, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare, getById
from Logic.functionalitate import trecereRezervari, maxPretPerClasa, ordonareDescrescatorDupaPret, \
    afisareSumaPretPentruFiecareNume, ieftinirePret


def printMenu():
    print("1.Adaugare rezervare")
    print("2.Stergere rezervare")
    print("3.Modifica rezervare")
    print("4.Trecerea tuturor rezervarilor facute pe un nume citit la o clasa superioara")
    print("5.Ieftinirea tuturor rezervarilor cu checkin ul facut cu un procentaj citit de la tastatura")
    print("6.Determinarea pretului maxim pentru fiecare clasa")
    print("7.Ordonarea rezervarilor descrescator dupa pret")
    print("8.Afisarea sumelor preturilor pentru fiecare nume")
    print("u.Undo")
    print("r.Redo")
    print("a.Afisarea rezervarilor")
    print("x.Iesire")


def uiAdaugaRezervare(lista, undoOperations, redoOperations):
    try:
        id = int(input("dati id-ul:"))
        nume = str(input("dati nume:"))
        clasa = str(input("dati clasa:"))
        pret = float(input("dati pretul:"))
        checkin = str(input("dati checkin:"))

        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undoOperations.append([
            lambda: stergeRezervare(id, rezultat),
            lambda: adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        ])
        redoOperations.clear()
        return rezultat

    except ValueError as ve:
        print ("Eroare: {}". format(ve))
        return lista


def uiStergeRezervare(lista, undoOperations, redoOperations):
    try:
        id = input("dati id-ul functiei pe care vreti sa o stergeti:")

        rezultat = stergeRezervare(id, lista)
        rezervareDeSters = getById(id, lista)
        undoOperations.append([
            lambda: adaugaRezervare(
                id,
                getNume(rezervareDeSters),
                getClasa(rezervareDeSters),
                getPret(rezervareDeSters),
                getCheckin(rezervareDeSters),
                rezultat
            ),
            lambda: stergeRezervare(id, lista)
        ])
        redoOperations.clear()

        return rezultat
    except ValueError as ve:
        print ("Eroare :{}". format(ve))
        return lista


def uiModificaRezervare(lista, undoOperations, redoOperations):
    try:
        id = input("dati id-ul:")
        nume = str(input("dati nume:"))
        clasa = str(input("dati clasa:"))
        pret = float(input("dati pretul:"))
        checkin = str(input("dati checkin:"))

        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
        rezervareVeche = getById(id, lista)
        undoOperations.append([
            lambda: modificaRezervare(
                id,
                getNume(rezervareVeche),
                getClasa(rezervareVeche),
                getPret(rezervareVeche),
                getCheckin(rezervareVeche),
                rezultat
            ),
            lambda: modificaRezervare(id, nume, clasa, pret, checkin, lista)
        ])
        redoOperations.clear()

        return rezultat
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiTrecereRezervari(lista, undoOperations, redoOperations):
    try:
        substringNume = input("dati numele persoanei care are rezervare pentru a o trece la o clasa superioara: ")
        rezultat = trecereRezervari(substringNume, lista)
        showAll(rezultat)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiMaxPretPerClasa(lista):
    try:
        rezultat = maxPretPerClasa(lista)
        for clasa in rezultat:
            print ("Clasa {} are pretul maxim de {} lei". format(clasa, rezultat[clasa]))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiOrdonareDescarescatorDupaPret(lista):
    try:
        showAll(ordonareDescrescatorDupaPret(lista))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiAfisareSumaPretPentruFiecareNume(lista):
    try:
        rezultat = afisareSumaPretPentruFiecareNume(lista)
        for nume in rezultat:
            print("Numele {} are suma preturilor de {}". format(nume, rezultat[nume]))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiIeftinirePret(lista):
    procentaj = int(input("dati procentul cu care se va iefini pretul rezervarii :"))
    rezultat = ieftinirePret(procentaj, lista)
    showAll(rezultat)


def runMenu(lista):
    undoOperations = []
    redoOperations = []
    while True:
        printMenu()
        optiune = input("dati optiunea :")

        if optiune == "1":
            lista = uiAdaugaRezervare(lista, undoOperations, redoOperations)
        elif optiune == "2":
            lista = uiStergeRezervare(lista, undoOperations, redoOperations)
        elif optiune == "3":
            lista = uiModificaRezervare(lista, undoOperations, redoOperations)
        elif optiune == "4":
            lista = uiTrecereRezervari(lista)
        elif optiune == "5":
            lista = uiIeftinirePret(lista)
        elif optiune == "6":
            lista = uiMaxPretPerClasa(lista)
        elif optiune == "7":
            lista = uiOrdonareDescarescatorDupaPret(lista)
        elif optiune == "8":
            lista = uiAfisareSumaPretPentruFiecareNume(lista)
        elif optiune == "u":
            if len(undoOperations) > 0:
                operations = undoOperations.pop()
                redoOperations.append(operations)
                lista = operations[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoOperations) > 0:
                operations = redoOperations.pop()
                undoOperations.append(operations)
                lista = operations[1]()
            else:
                print("Nu se poate face redo!!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")
