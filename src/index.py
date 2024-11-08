from varasto import Varasto

def tulosta_varastojen_alkutila(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def testaa_olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def testaa_mehu_setterit(mehua):
    print("Mehu setterit:")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def testaa_virhetilanteet():
    print("Virhetilanteita:")
    huono1 = Varasto(-100.0)
    print(huono1)
    huono2 = Varasto(100.0, -50.7)
    print(huono2)

def testaa_lisays_ja_otto(olutta, mehua):
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    saatiin_olutta = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin_olutta}")
    print(f"Olutvarasto: {olutta}")

    saatiin_mehua = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin_mehua}")
    print(f"Mehuvarasto: {mehua}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    tulosta_varastojen_alkutila(mehua, olutta)
    testaa_olut_getterit(olutta)
    testaa_mehu_setterit(mehua)
    testaa_virhetilanteet()
    testaa_lisays_ja_otto(olutta, mehua)

if __name__ == "__main__":
    main()
    