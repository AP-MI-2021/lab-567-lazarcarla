from Domain.rezervari import creeazaRezervare, getNume, getClasa, getId, getPret, getCheckin


def trecereRezervari(stringNume, lista):
    '''
    Trecerea tuturor rezervarilor facute pe un nume citit la o clasa superioara
    :param stringNume: string
    :param lista: lista de rezervari
    :return: lista cu rezervarile dupa modificarea claselor
    '''
    listaNoua = []
    for rezervare in lista:
        if getNume(rezervare) == stringNume and getClasa(rezervare) == "economy":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                "economy plus",
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        elif getNume(rezervare) == stringNume and getClasa(rezervare) == "economy plus":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                "business",
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        elif getNume(rezervare) == stringNume and getClasa(rezervare) == "business":
            listaNoua.append(rezervare)
    return listaNoua


def ieftinirePret(procentaj, lista):
    '''
    determina ieftinirea tuturor rezervarilor cu checkin facut cu un procentaj citit
    :param procentaj: procentajul cu care se ieftineste rezervarea
    :param lista:lista de rezervari
    :return: preturile ieftinite
    '''
    if procentaj < 0:
        raise ValueError("Procentajul trebuie sa fie un numar pozitiv!!!")
    listaNoua = []
    for rezervare in lista:
        if getCheckin(rezervare) == "da":
            reducere = procentaj/100*getPret(rezervare)
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare)-reducere,
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        elif getCheckin(rezervare) == "nu":
            listaNoua.append(rezervare)
    return listaNoua


def maxPretPerClasa(lista):
    '''
    determina pentru fiecare clasa pretul maxim
    :param lista: lista de rezervari
    :return: pretul maxim pentru fiecare clasa
    '''

    rezultat = {}
    for rezervare in lista:
        pret = getPret(rezervare)
        clasa = getClasa(rezervare)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
            rezultat[clasa] = pret
    return rezultat


def ordonareDescrescatorDupaPret(lista):
    '''
    ordonarea rezervarilor in ordine descrescatoare dupa pret
    :param lista: lista de rezervari
    :return: rezervarile in ordine descrescatoare ordonate dupa pret
    '''

    return sorted(lista, key=lambda rezervare: getPret(rezervare), reverse=True)


def afisareSumaPretPentruFiecareNume(lista):
    '''
    determina afisarea sumei preturilor pentru fiecare nume
    :param lista:lista de rezervari
    :return:suma preturilor pentru fiecare nume
    '''
    rezultat = {}
    for rezervare in lista:
        pret = getPret(rezervare)
        nume = getNume(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat
