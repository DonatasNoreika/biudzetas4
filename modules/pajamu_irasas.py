from modules.irasas import Irasas
from modules.my_enums import Siuntejas

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas: Siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

    def __str__(self):
        return f"Pajamos: {self.suma} Eur, siuntėjas - {self.siuntejas}, info - {self.papildoma_informacija}"
