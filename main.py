from Logic.CRUD import adaugaRezervare
from Tests.testAll import runAllTests
from UI.commandLine import commandMenu
from UI.console import runMenu


def main():
    runAllTests()
    lista=[]
    commandMenu([])
    #runMenu(lista)

main()