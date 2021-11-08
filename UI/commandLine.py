from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from UI.console import showAll


def printMenu():
    print("Add,id , nume, clasa, pret, checkin --> adauga o noua rezervare")
    print("Delete, id -->Sterge o rezervare")
    print("Update, id, nume, clasa, pret, checkin -->modifica o rezervare")
    print("ShowAll -->afiseaza toate rezervarile")
    print("Stop -->opreste programul")


def mainCommand(lista):

    while True:
        printMenu()
        option = input()
        if option == "help":
            printMenu()
        else:
            string = option.split(";")
            if string[0] == "Stop":
                break
            else:
                for elements in string:
                    elem = elements.split(",")
                    if elem[0] == "Add":
                        lista = adaugaRezervare(elem[1], elem[2], elem[3], float(elem[4]), elem[5], lista)
                    elif elem[0] == "Delete":
                        try:
                            lista = stergeRezervare(elem[1], lista)
                        except ValueError:
                            print("Nu exista rezervarea cu id-ul dat pentru a o sterge!")
                    elif elem[0] == "Update":
                        try:
                            lista = modificaRezervare(elem[1], elem[2], elem[3], float(elem[4]), elem[5], lista)
                        except ValueError:
                            print("Nu exista rezervarea cu id-ul dat pentru a o modifica!")
                    elif elem[0] == "ShowAll":
                        showAll(lista)
                    else:
                        print("optiune gresita! reincercati!!!")


lista = []
mainCommand(lista)
