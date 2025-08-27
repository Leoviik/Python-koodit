import math

kanta = float(input("Kerro haluamasi kanta: "))
korkeus = float(input("Kerro haluamasi korkeus: "))
pintaala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

print(f"Suorakulmion pinta-ala on: {pintaala:.1f}")
print(f"Suorakulmion piiri on: {piiri:.1f}")
