
sukupuoli = input("Oletko mies vai nainen? :").lower()
if sukupuoli == "mies":
    marvo = int(input("Mikä on hemoglobiiniarvosi? : "))
    if marvo < 134:
        print("Arvosi ovat alhaiset")
    elif marvo > 195:
        print("Arvosi ovat korkeat")
    else:
        print("Arvosi ovat normaalit")

elif sukupuoli == "nainen":
    narvo = int(input("Mikä on hemoglobiiniarvosi? : "))
    if narvo < 117:
        print("Arvosi ovat alhaiset")
    elif narvo > 175:
        print("Arvosi ovat korkeat")
    else:
        print("Arvosi ovat normaalit")
else:
    print("Virheellinen sukupuoli.")
