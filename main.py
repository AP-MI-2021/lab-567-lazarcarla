from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista=[]
    lista = adaugaRezervare("1", "Maria", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Maria", "economy plus", 390, "da", lista)
    lista = adaugaRezervare("3", "Marian", "economy", 250, "nu", lista)
    lista = adaugaRezervare("4", "Denisa", "business", 550, "nu", lista)
    runMenu(lista)

main()