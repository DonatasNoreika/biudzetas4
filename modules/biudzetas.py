from modules.pajamu_irasas import PajamuIrasas
from modules.islaidu_irasas import IslaiduIrasas
import pickle

class Biudzetas:
    def __init__(self):
        self.zurnalas = self._gauti_zurnala()

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

    def irasyti_zurnala(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamas(self, suma, siuntejas="darbdavys", papildoma_informacija="atlyginimas"):
        irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala()

    def prideti_islaidas(self, suma, atsiskaitymo_budas="kortele", isigyta_preke_paslauga="pirkinys"):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)
        self.irasyti_zurnala()

    def balansas(self):
        bendra = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                bendra += irasas.suma
            if type(irasas) is IslaiduIrasas:
                bendra -= irasas.suma
        print(bendra)
        return bendra

    def ataskaita(self):
        print("Ataskaita:")
        for irasas in self.zurnalas:
            print(irasas)
        print("--------------")

    def isvalyti_biudzeta(self):
        self.zurnalas = []
        self.irasyti_zurnala()
