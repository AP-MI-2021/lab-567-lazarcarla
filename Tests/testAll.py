from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervarea
from Tests.testDomain import testRezervare
from Tests.testFunctionalitate import testTrecereRezervari, testMaxPretPerClasa, testOrdonareDescrescatorDupaPret, \
    testAfisareSumaPretPentruFiecareNume


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervarea()
    testTrecereRezervari()
    testMaxPretPerClasa()
    testOrdonareDescrescatorDupaPret()
    testAfisareSumaPretPentruFiecareNume()