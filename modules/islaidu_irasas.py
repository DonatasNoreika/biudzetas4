from modules.irasas import Irasas


class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __str__(self):
        return f"Išlaidos: {self.suma} Eur, atsiskaitymo būdas - {self.atsiskaitymo_budas}, įsigyta - {self.isigyta_preke_paslauga}"
