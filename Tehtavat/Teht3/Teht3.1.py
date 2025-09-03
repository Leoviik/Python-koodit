Kuha = int(input("Kuinka suuri kuha tuli? (Kerro pituus kokonaislukuna sentteinä) : "))

if Kuha >=37:
    print("Laitappas pannu kuumaksi!")
elif Kuha <0:
    print("Nyt narraat.")

else:
    Puuttuu = 37 - Kuha
    print(F"Äh se on {Puuttuu} senttiä alle rajan.")
    print("Heitä takasin kasvamaan.")

