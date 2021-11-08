from Domain.rezervari import getId
from Logic.CRUD import adaugaRezervare, stergeRezervare, getById


def testUndoRedo():
    #1 adauga o rezervare
    lista = []
    undoList = []
    redoList = []
    #2 adauga o rezervare
    rezultat = adaugaRezervare("1", "Adrian", "business", 450.0, "da", lista)
    undoList.append(lista)
    lista = rezultat
    #3 adauga o rezervare
    lista = adaugaRezervare("2", "Mariana", "economy", 245.0, "da", lista)
    undoList.append(lista)
    lista = rezultat
    #4 adauga o rezervare
    lista = adaugaRezervare("3", "Denisa", "economy plus", 50.5, "nu", lista)
    undoList.append(lista)
    lista=rezultat
    #5
    redoList.append(lista)
    lista=undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"
    #6
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]
    #7
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert undoList == [[]]
    #8
    if len(undoList) > 0:
        redoList.append(lista)
        lista=undoList
    assert len(lista) == 0
    assert undoList == [[]]
    #9
    rezultat = adaugaRezervare("1", "Mihai", "business", 4300.0, "nu", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("2", "Denis", "economy plus", 300.0, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("3", "Ioana", "economy", 500.0, "da", lista)
    undoList.append(lista)
    lista = rezultat
    assert len(redoList) == 0
    assert len(UndoList) == 3
    assert len(lista) == 3
    #10
    if len(redoList) > 0:
        undoList.append(lista)
        lista=redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3
    #11
    redoList.append(lista)
    lista=undoList.pop

    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop

    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    #12
    undoList.append(lista)
    lista=redoList.pop()
    assert len(redoList) ==1
    assert len(undoList) == 2
    assert len(lista) == 2

    #13
    undoList.append(lista)
    lista=redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    #14

    redoList.append(lista)
    lista=undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) =="2"
    assert getId(lista[0]) == "1"
    assert undoList== [[]]

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    #15
    rezultat = adaugaRezervare("4", "Cristian", "business", 1000.0, "da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    #16

    if len(redoList) > 0:
        undoList.append(lista)
        lista=redoList.pop()
    assert len(lista)==2
    assert len(undoList)==2

    #17

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert len(redoList) == 1
    assert len(undoList) == 1

    #18

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert len(redoList) == 2
    assert len(undoList) == 0

    #19

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 1

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0

    #20

    if len(redoList) >0:
        undoList.append(lista)
        lista=redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0
    assert len(undoList) == 2
