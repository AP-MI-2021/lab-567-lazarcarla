from Domain.rezervari import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))

def meniu_help():
    print("Add, id, nume, clasa, pret, checkin  ->Adauga rezervarea")
    print("Delete, id ->Sterge rezervarea")
    print("Update, id, nume, clasa, pret, checkin ->Modifica rezervarea")
    print("ShowAll ->Afiseaza toate rezervarile din lista")
    print("Stop ->Oprire program")

def commandMenu(lista):
    while True:
        command=input()
        if command=='Help':
            meniu_help()
        else:
            string = command.split(";")
            if string[0]=='Stop':
                break
            else:
                for elemente in string:
                    comenzi=elemente.split(',')
                        if comenzi[0]=='Add':
                            try:
                                lista=adaugaRezervare(comenzi[1], comenzi[2], comenzi[3], float(comenzi[4]), comenzi[5], lista)
                            except ValueError as ve:
                                print("Eroare : {}". format(ve))
                        elif comenzi[0]=='Delete':
                            lista=stergeRezervare(comenzi[1], lista)
                        elif comenzi[0]=='Update':
                            lista=modificaRezervare(comenzi[1], comenzi[2], comenzi[3], float(comenzi[4]), comenzi[5], lista)
                        elif comenzi[0]=='ShowAll':
                            showAll(lista)
                        else:
                            print("Optiune gresita, tastati Help pentru a vedea optiunuile disponibile!!")

lista=[]
commandMenu(lista)

