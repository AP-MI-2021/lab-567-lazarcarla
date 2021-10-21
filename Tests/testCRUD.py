from Domain.rezervari import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaRezervare, getById, stergeRezervare, modificaRezervare


def testAdaugaRezervare():
    lista=[]
    lista=adaugaRezervare("1", "Marian", "economy", 200, "da",lista)

    assert len(lista)==1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "Marian"
    assert getClasa(getById("1", lista)) == "economy"
    assert getPret(getById("1", lista)) == 200
    assert getCheckin(getById("1", lista)) == "da"


def testStergeRezervare():
    lista=[]
    lista = adaugaRezervare("1", "Marian", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Maria", "economy plus", 300, "nu", lista)

    lista=stergeRezervare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

def testModificaRezervarea():
    lista=[]
    lista = adaugaRezervare("1", "Marian", "economy", 200, "da", lista)
    lista = adaugaRezervare("2", "Maria", "economy plus", 300, "nu", lista)

    lista=modificaRezervare("1", "Denisa", "business", 450, "nu", lista)

    rezervareUpdatata=getById("1", lista)
    assert getId(rezervareUpdatata)=="1"
    assert getNume(rezervareUpdatata)=="Denisa"
    assert getClasa(rezervareUpdatata)=="business"
    assert getPret(rezervareUpdatata)==450
    assert getCheckin(rezervareUpdatata)=="nu"
