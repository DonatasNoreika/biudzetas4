
from modules.biudzetas import Biudzetas

biudzetas1 = Biudzetas()

while True:
    veiksmas = int(
        input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - balansas \n4 - ataskaita \n5 - išvalyti biudžetą \n6 - išeiti iš programos"))
    if veiksmas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        biudzetas1.prideti_pajamas(suma)
    if veiksmas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        biudzetas1.prideti_islaidas(suma)
    if veiksmas == 3:
        biudzetas1.balansas()
    if veiksmas == 4:
        biudzetas1.ataskaita()
    if veiksmas == 5:
        biudzetas1.isvalyti_biudzeta()
    if veiksmas == 6:
        print("Viso gero")
        break
