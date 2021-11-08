
from Domain.rezervari import getId
from Logic.CRUD import adaugaRezervare, stergeRezervare, getById


def testUndoRedo():

    lista = []
    undoList = []
    redoList = []
    #2 adauga o rezervare
    rezultat = adaugaRezervare("1", "Adrian", "business", 450.0, "da", lista)
    undoList.append(lista)
    lista = rezultat
    #3 adauga o rezervare
    rezultat = adaugaRezervare("2", "Mariana", "economy", 245.0, "da", lista)
    undoList.append(lista)
    lista = rezultat
    #4 adauga o rezervare
    rezultat = adaugaRezervare("3", "Denisa", "economy plus", 50.5, "nu", lista)
    undoList.append(lista)
    lista=rezultat
    #5 undo scote ultina rezervare
    redoList.append(lista)
    lista=undoList.pop()
    assert len(lista) == 2
    print(getId(lista[1]))
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"
    #6 undo scoate penultima rezervare
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]
    #7 undo scoate prima rezervare
    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert undoList == []
    #8 undo care nu face nimic
    if len(undoList) > 0:
        redoList.append(lista)
        lista=undoList
    assert len(lista) == 0
    assert undoList == []
    #9 adaugam 3 rezervari
    rezultat = adaugaRezervare("1", "Mihai", "business", 4300.0, "nu", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    rezultat = adaugaRezervare("2", "Denis", "economy plus", 300.0, "da", lista)
    undoList.append(lista)
    lista = rezultat

    rezultat = adaugaRezervare("3", "Ioana", "economy", 500.0, "da", lista)
    undoList.append(lista)
    lista = rezultat
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3
    #10 facem redo
    if len(redoList) > 0:
        undoList.append(lista)
        lista=redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3
    #11 2 undo
    redoList.append(lista)
    lista=undoList.pop()

    assert len(lista) == 2
    assert getId(lista[1]) == "2"
    assert getId(lista[0]) == "1"

    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    #12 redo
    undoList.append(lista)
    lista=redoList.pop()
    assert len(redoList) ==1
    assert len(undoList) == 2
    assert len(lista) == 2

    #13 redo
    undoList.append(lista)
    lista=redoList.pop()
    assert len(redoList) == 0
    assert len(undoList) == 3
    assert len(lista) == 3

    #14 se fac 2 undo

    redoList.append(lista)
    lista=undoList.pop()
    assert len(lista) == 2
    assert getId(lista[1]) =="2"
    assert getId(lista[0]) == "1"


    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert getId(lista[0]) == "1"
    assert undoList == [[]]

    #15 adaugam a 4 a rezervare
    rezultat = adaugaRezervare("4", "Cristian", "business", 1000.0, "da", lista)
    undoList.append(lista)
    lista = rezultat
    redoList.clear()

    #16 redo

    if len(redoList) > 0:
        undoList.append(lista)
        lista=redoList.pop()
    assert len(lista)==2
    assert len(undoList)==2

    #17 se face undo

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 1
    assert len(redoList) == 1
    assert len(undoList) == 1

    #18 undo

    redoList.append(lista)
    lista = undoList.pop()
    assert len(lista) == 0
    assert len(redoList) == 2
    assert len(undoList) == 0

    #19 2 redo

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 1

    undoList.append(lista)
    lista = redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0

    #20 ultimul redo care nu face nimic

    if len(redoList) >0:
        undoList.append(lista)
        lista=redoList.pop()
    assert len(lista) == 2
    assert len(redoList) == 0
    assert len(undoList) == 2
