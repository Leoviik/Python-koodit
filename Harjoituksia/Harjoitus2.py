Nimi = input("Hei tervetuloa. Mikä on nimenne? : ").lower()

if Nimi != "matti":
    annokset = int(input("Montako keittoannosta? : "))
    print(f"Kokonaishinta on {annokset * 5.90}€")
    print("Seuraava, kiitos!")

else:
    print("Haista vittu matti.")


