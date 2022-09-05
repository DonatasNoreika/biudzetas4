from modules.pajamu_irasas import PajamuIrasas
from modules.islaidu_irasas import IslaiduIrasas
import pickle

class Biudzetas:
    def __init__(self):
        self._zurnalas = self._gauti_zurnala()

    def _gauti_zurnala(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
                return zurnalas
        except:
            with open("zurnalas.pkl", 'wb') as file:
                zurnalas = []
                pickle.dump(zurnalas, file)
                return zurnalas

    def _irasyti_zurnala(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self._zurnalas, file)

    def prideti_pajamas(self, suma, siuntejas="darbdavys", papildoma_informacija="atlyginimas"):
        irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self._zurnalas.append(irasas)
        self._irasyti_zurnala()

    def prideti_islaidas(self, suma, atsiskaitymo_budas="kortele", isigyta_preke_paslauga="pirkinys"):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self._zurnalas.append(irasas)
        self._irasyti_zurnala()

    def balansas(self):
        bendra = 0
        for irasas in self._zurnalas:
            if type(irasas) is PajamuIrasas:
                bendra += irasas.suma
            if type(irasas) is IslaiduIrasas:
                bendra -= irasas.suma
        print(bendra)
        return bendra

    def ataskaita(self):
        print("Ataskaita:")
        for irasas in self._zurnalas:
            print(irasas)
        print("--------------")

    def isvalyti_biudzeta(self):
        self._zurnalas = []
        self._irasyti_zurnala()
