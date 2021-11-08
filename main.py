from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.commandLine import mainCommand

from UI.console import runMenu

def printOptions():
    print("1. Utilizati interfata cu comenzi .")
    print("2. Utilizati interfata cu optiuni .")
    print("x.Iesire")


def main():
    runAllTests()
    lista=[]
    lista = adaugaRezervare("1", "Maria", "economy", 200.00, "da", lista)
    lista = adaugaRezervare("2", "Maria", "economy plus", 390.00, "da", lista)
    lista = adaugaRezervare("3", "Marian", "economy", 250.50, "nu", lista)
    lista = adaugaRezervare("4", "Denisa", "business", 550.00, "nu", lista)
    lista = adaugaRezervare("5", "Ariana", "economy plus", 800.00, "da", lista)


    runMenu(lista)


main()