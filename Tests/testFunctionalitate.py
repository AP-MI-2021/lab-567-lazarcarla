from Domain.rezervari import getClasa, getId, getPret
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitate import trecereRezervari, maxPretPerClasa, ordonareDescrescatorDupaPret, \
    afisareSumaPretPentruFiecareNume, ieftinirePret


def testTrecereRezervari():
    lista = []
    lista = adaugaRezervare("1", "Maria", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Maria", "economy plus", 390, "da", lista)
    lista = adaugaRezervare("3", "Denisa", "business", 550, "nu", lista)

    lista = trecereRezervari("Maria", lista)

    assert getClasa(getById("1", lista)) == "economy plus"
    assert getClasa(getById("2", lista)) == "business"


def testIeftinirePret():
    lista = []
    lista = adaugaRezervare("1", "Maria", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Maria", "economy plus", 390, "da", lista)
    lista = adaugaRezervare("3", "Denisa", "business", 550, "nu", lista)

    lista = ieftinirePret(30, lista)

    assert getPret(getById("1", lista)) == 140
    assert getPret(getById("2", lista)) == 273
    assert getPret(getById("3", lista)) == 385


def testMaxPretPerClasa():
    lista = []
    lista = adaugaRezervare("1", "Maria", "economy", 200.00, "da", lista)
    lista = adaugaRezervare("2", "Adriana", "economy plus", 390.00, "da", lista)
    lista = adaugaRezervare("3", "Marian", "economy", 250.50, "nu", lista)
    lista = adaugaRezervare("4", "Denisa", "business", 550.00, "nu", lista)

    rezultat = maxPretPerClasa(lista)

    assert len(rezultat) == 3

    assert rezultat["economy"] == 250.50
    assert rezultat["economy plus"] == 390.00
    assert rezultat["business"] == 550.00


def testOrdonareDescrescatorDupaPret():
    lista = []
    lista = adaugaRezervare("1", "Maria", "economy", 200.00, "da", lista)
    lista = adaugaRezervare("2", "Adriana", "economy plus", 390.00, "da", lista)
    lista = adaugaRezervare("3", "Denisa", "business", 550.00, "nu", lista)

    rezultat = ordonareDescrescatorDupaPret(lista)

    assert getId(rezultat[0]) == "3"
    assert getId(rezultat[1]) == "2"
    assert getId(rezultat[2]) == "1"


def testAfisareSumaPretPentruFiecareNume():
    lista = []
    lista = adaugaRezervare("1", "Maria", "economy", 200.00, "da", lista)
    lista = adaugaRezervare("2", "Maria", "economy plus", 390.00, "da", lista)
    lista = adaugaRezervare("3", "Denisa", "business", 550.00, "nu", lista)
    lista = adaugaRezervare("4", "Denisa", "economy", 200.00, "nu", lista)

    rezultat = afisareSumaPretPentruFiecareNume(lista)

    assert rezultat["Maria"] == 590.00
    assert rezultat["Denisa"] == 750.00
