from Logic.CRUD import adaugaRezervare, stergeRezervare, getById


def testUndoRedo():
    lista = []
    undoOperations = []
    redoOperations = []

    rezultat = adaugaRezervare("1", "Adrian", "business", 450.0, "da", lista)
    undoOperations.append([
        lambda:stergeRezervare("1", lista),
        lambda:adaugaRezervare("1", "Adrian", "bussines", 450.0, "da", lista)
    ])
    redoOperations.clear()
    lista = rezultat

    lista = adaugaRezervare("2", "Mariana", "economy", 245.0, "da", lista)
    undoOperations.append([
        lambda:stergeRezervare("2", lista),
        lambda:adaugaRezervare("2", "Mariana", "economy", 245.0, "da", lista)
    ])
    redoOperations.clear()
    lista = rezultat

    lista = adaugaRezervare("3", "Denisa", "economy plus", 50.5, "nu", lista)
    undoOperations.append([
        lambda:stergeRezervare("3", lista),
        lambda:adaugaRezervare("3", "Denisa", "economy plus", 50.5, "nu", lista)
    ])
    redoOperations.clear()
    lista=rezultat

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 1
    assert getById("1", lista) is not None

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 0

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 0

    rezultat = adaugaRezervare("1", "Mihai", "business", 4300.0, "nu", lista)
    undoOperations.append([
        lambda:stergeRezervare("1", lista),
        lambda:adaugaRezervare("1", "Mihai", "business", 4300.0, "nu", lista)
    ])
    redoOperations.clear()
    lista = rezultat

    rezultat = adaugaRezervare("2", "Denis", "economy plus", 300.0, "da", lista)
    undoOperations.append([
        lambda:stergeRezervare("2", lista),
        lambda:adaugaRezervare("2", "Denis", "economy plus", 300.0, "da", lista)
    ])
    redoOperations.clear()
    lista = rezultat

    rezultat = adaugaRezervare("3", "Ioana", "economy", 500.0, "da", lista)
    undoOperations.append([
        lambda:stergeRezervare("3", lista),
        lambda:adaugaRezervare("3", "Ioana", "economy", 500.0, "da", lista)
    ])
    redoOperations.clear()
    lista = rezultat

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 3

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista=operations[0]()

    assert len(lista) == 1
    assert getById("1", lista) is not None

    rezultat = adaugaRezervare("4", "Cristian", "economy", 200.0, "da", lista)
    undoOperations.append([
        lambda:stergeRezervare("4", lista),
        lambda:adaugaRezervare("4", "Cristian", "economy", 200.0, "da", lista)
    ])
    redoOperations.clear()
    lista = rezultat

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("4", lista) is not None

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("4", lista) is None

    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()

    assert len(lista) == 0
    assert getById("1", lista) is None

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("4", lista) is not None

    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()

    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("4", lista) is not None






