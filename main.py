
from modules.biudzetas import Biudzetas
from modules.my_enums import AtsiskaitymoBudas, Siuntejas

biudzetas1 = Biudzetas()

while True:
    veiksmas = int(
        input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - balansas \n4 - ataskaita \n5 - išvalyti biudžetą \n6 - išeiti iš programos"))
    if veiksmas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        for budas in Siuntejas:
            print(f"{budas.value} - {budas.name}")
        siuntejas = Siuntejas(int(input("Pasirinkite siuntėją")))
        papildoma = input("Įveskite papildomą informaciją")
        biudzetas1.prideti_pajamas(suma, siuntejas=siuntejas, papildoma_informacija=papildoma)
    if veiksmas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        for budas in AtsiskaitymoBudas:
            print(f"{budas.value} - {budas.name}")
        atsiskaitymo_budas = AtsiskaitymoBudas(int(input("Pasirinkite atsiskaitymo būdą")))
        isigyta = input("Įveskite įsigytą prekę/paslaugą")
        biudzetas1.prideti_islaidas(suma, atsiskaitymo_budas=atsiskaitymo_budas, isigyta_preke_paslauga=isigyta)
    if veiksmas == 3:
        biudzetas1.balansas()
    if veiksmas == 4:
        biudzetas1.ataskaita()
    if veiksmas == 5:
        biudzetas1.isvalyti_biudzeta()
    if veiksmas == 6:
        print("Viso gero")
        break
