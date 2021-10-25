from Domain.rezervari import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Logic.functionalitate import trecereRezervari


def printMenu():
    print("1.Adaugare rezervare")
    print("2.Stergere rezervare")
    print("3.Modifica rezervare")
    print("4.Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("a.Afisarea rezervarilor")
    print("x.Iesire")


def uiAdaugaRezervare(lista):
    id=input("dati id-ul:")
    nume=input("dati nume:")
    clasa= input("dati clasa:")
    pret=float(input("dati pretul:"))
    checkin=input("dati checkin:")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)


def uiStergeRezervare(lista):
    id=input("dati id-ul functiei pe care vreti sa o stergeti:")
    return stergeRezervare(id, lista)


def uiModificaRezervare(lista):
    id = input("dati id-ul:")
    nume = input("dati nume:")
    clasa = input("dati clasa:")
    pret = float(input("dati pretul:"))
    checkin = input("dati checkin:")
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiTrecereRezervari(lista):
    substringNume=input("dati numele persoanei care are rezervare pentru a o trece la o clasa superioara: ")
    return trecereRezervari(substringNume,lista)


def runMenu(lista):
    while True:
        printMenu()
        optiune=input("dati optiunea :")

        if optiune=="1":
            lista=uiAdaugaRezervare(lista)
        elif optiune=="2":
            lista=uiStergeRezervare(lista)
        elif optiune=="3":
            lista=uiModificaRezervare(lista)
        elif optiune=="4":
            lista=uiTrecereRezervari(lista)
        elif optiune=="a":
            showAll(lista)
        elif optiune=="x":
            break
        else:
            print("Optiune gresita! Reincercati!")

