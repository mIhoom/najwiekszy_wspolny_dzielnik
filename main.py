a = int(input('Proszę podać pierwszą liczbę: '))
b = int(input('Proszę podać druga liczbę: '))
while b!=0:
    c = a % b
    a = b
    b = c
print('Największy wspólny dzielnik to: ', a)
