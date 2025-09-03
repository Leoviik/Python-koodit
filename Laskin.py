print("-----Tervetuloa käyttämään laskinta!-----")

print("Valitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku"
      "\n C: Kertolasku \n D: Jakolasku")

valinta = input("Valintasi (A - D): ").upper()

if valinta == "A":
    A = float(input("Anna luku:"))
    B = float(input("Anna toinen luku:"))
    print("yhteenlasku:",A + B)
elif valinta == "B":
    A = float(input("Anna luku:"))
    B = float(input("Anna toinen luku:"))
    print("vähennyslasku:",A - B)
elif valinta == "C":
    A = float(input("Anna luku:"))
    B = float(input("Anna toinen luku:"))
    print("kertolasku:",A * B)
elif valinta == "D":
    A = float(input("Anna luku:"))
    B = float(input("Anna toinen luku:"))
    print("jakolasku:",A / B)
else:
    print("Valintasi oli virheellinen.")

