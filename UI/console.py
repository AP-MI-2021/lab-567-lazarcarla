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


def uiAdaugaRezervare(lista, undoList, redoList):
    try:
        id = int(input("dati id-ul:"))
        nume = str(input("dati nume:"))
        clasa = str(input("dati clasa:"))
        pret = float(input("dati pretul:"))
        checkin = str(input("dati checkin:"))

        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat

    except ValueError as ve:
        print ("Eroare: {}". format(ve))
        return lista


def uiStergeRezervare(lista, undoList, redoList):
    try:
        id = input("dati id-ul functiei pe care vreti sa o stergeti:")

        rezultat = stergeRezervare(id, lista)
        undoList.append(lista)
        redoList.clear()

        return rezultat
    except ValueError as ve:
        print ("Eroare :{}". format(ve))
        return lista


def uiModificaRezervare(lista, undoList, redoList):
    try:
        id = input("dati id-ul:")
        nume = str(input("dati nume:"))
        clasa = str(input("dati clasa:"))
        pret = float(input("dati pretul:"))
        checkin = str(input("dati checkin:"))

        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()

        return rezultat
    except ValueError as ve:
        print("Eroare: {}". format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiTrecereRezervari(lista, undoList, redoList):
    try:
        substringNume = input("dati numele persoanei care are rezervare pentru a o trece la o clasa superioara: ")
        rezultat = trecereRezervari(substringNume, lista)
        undoList.append(lista)
        redoList.clear()
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


def uiIeftinirePret(lista, undoList, redoList):
    procentaj = int(input("dati procentul cu care se va iefini pretul rezervarii :"))
    rezultat = ieftinirePret(procentaj, lista)
    undoList.append(lista)
    redoList.clear()
    showAll(rezultat)


def runMenu(lista):
    undoList=[]
    redoList=[]
    while True:
        printMenu()
        optiune = input("dati optiunea :")

        if optiune == "1":
            lista = uiAdaugaRezervare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeRezervare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaRezervare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiTrecereRezervari(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiIeftinirePret(lista, undoList, redoList)
        elif optiune == "6":
            lista = uiMaxPretPerClasa(lista)
        elif optiune == "7":
            lista = uiOrdonareDescarescatorDupaPret(lista)
        elif optiune == "8":
            lista = uiAfisareSumaPretPentruFiecareNume(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista=undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista=redoList.pop()
            else:
                print("Nu se poate face redo!!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati!")
