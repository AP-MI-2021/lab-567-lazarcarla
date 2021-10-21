from Domain.rezervari import creeazaRezervare, getId


def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    '''
    adauga o rezervare intr-o lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: int
    :param checkin: string
    :param lista: lista de rezervari
    :return: o lista continand atat elementele vechi cat si noua rezervare
    '''
    rezervare=creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]

def getById( id , lista):
    '''
    returneaza rezervarea data cu id-ul dintr-o lista
    :param id: string
    :param lista: lista de rezervari
    :return: rezervarea data cu id-ul dintr-o lista, in caz contrat None
    '''
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None

def stergeRezervare(id, lista):
    '''
    sterge o rezervare dupa un id dat
    :param id:id-ul rezervarii care se va sterge
    :param lista:lista de rezervari
    :return:lista dupa ce s-a sters rezervarea cu id-ul specificat
    '''
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id , nume, clasa, pret, checkin, lista):
    '''
    modifica o rezervare dupa id
    :param id: id-ul rezervarii
    :param nume:numele rezervarii
    :param clasa:clasa rezervarii
    :param pret:pretul rezervarii
    :param checkin:checkin ul rezervarii
    :param lista:lista de rezervari
    :return:lista modificata
    '''
    listaNoua=[]
    for rezervare in lista:
        if getId(rezervare)== id:
            rezervareNoua=creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

