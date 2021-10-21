from Domain.rezervari import getClasa
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitate import trecereRezervari


def testTrecereRezervari():
    lista=[]
    lista = adaugaRezervare("1", "Maria", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Maria", "economy plus", 390, "da", lista)
    lista = adaugaRezervare("3", "Denisa", "business", 550, "nu", lista)

    lista=trecereRezervari("Maria", lista)

    assert getClasa(getById("1", lista)) == "economy plus"
    assert getClasa(getById("2", lista)) == "business"
