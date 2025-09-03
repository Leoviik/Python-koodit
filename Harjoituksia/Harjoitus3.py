n = int(input("Anna kokonaisluku: "))

if n % 3 == 0 and n % 5 == 0:
    print("BoomBuzz")
elif n % 3 == 0:
    print("Boom")
elif n % 5 == 0:
    print("Buzz")

if n > 0:
    if n % 2 == 0:
        print("Numero on parillinen")
    else:
        print("Numero on pariton")
else:
    print("Numero oli negatiivinen tai nolla.")
