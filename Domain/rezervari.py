def creeazaRezervare(id, nume, clasa, pret, checkin):
    '''
    creeaza un dictionar care reprezinta o rezervare
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: un dictionar ce reprezinta o rezervare
    '''
    #return [id, nume, clasa, pret, checkin]
    return {
        "id":id,
        "nume":nume,
        "clasa":clasa,
        "pret":pret,
        "checkin":checkin
    }
def getId(rezervare):
    '''
    da id-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return:id-ul rezervarii
    '''
    #return rezervare[0]
    return rezervare["id"]

def getNume(rezervare):
    '''
    da numele unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: numele unei rezervari
    '''
    #return rezervare[1]
    return rezervare["nume"]


def getClasa(rezervare):
    '''
    da clasa unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: clasa unei rezervari:economy, economy plus, business
    '''
    #return rezervare[2]
    return rezervare["clasa"]


def getPret(rezervare):
    '''
    da pretul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: pretul unei rezervari
    '''
    #return rezervare[3]
    return rezervare["pret"]


def getCheckin(rezervare):
    '''
    da checkin-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: checkin-ul unei rezervari: "da" daca este facut , sau "nu" in caz ca nu este facut
    '''
    #return rezervare[4]
    return rezervare["checkin"]


def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {} ".format(

        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )
