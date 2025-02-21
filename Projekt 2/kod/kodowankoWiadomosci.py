"""
By Michał Matuszyk
on 03/05/2023
"""

import random

from matplotlib import pyplot as plt

from generatorSlowKodowych import wygenerujPrzestrzen, odkodujWektor

random.seed(2023)

macierzG = [[1, 0, 0, 0, 0, 4, 4, 2, 0, 1, 1],
            [0, 1, 0, 0, 0, 3, 0, 2, 2, 1, 0],
            [0, 0, 1, 0, 0, 2, 0, 1, 1, 1, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 4, 3, 0]]

macierzWylosowana = [[3, 3, 3, 2, 4, 4, 2, 0, 0, 2],
                     [4, 4, 2, 1, 1, 1, 0, 1, 2, 0],
                     [4, 1, 0, 1, 1, 3, 3, 4, 2, 4],
                     [0, 0, 4, 3, 3, 0, 0, 4, 1, 4]]  # macierz użyta w Wordzie

wektorDoZakodowania = [
    4, 1, 1, 3
]


#seed(2023) #aby dostać wynik jak w wordzie, trzeba ustawić takie ziarno


def wygenerujMacierz(lWierszy, lKolumn,
                     modCiala):  # Generuje macierz z odpowiednia liczba wierszy i kolumn, w odpowiednim ciele Z mod x
    macierz = []
    for y in range(lWierszy):
        wiersz = []
        for x in range(lKolumn):
            wiersz.append(random.randint(0, modCiala - 1))
        macierz.append(wiersz)
    return macierz


def wypiszMacierz(m):  # ladnie wypisuje macierz na ekran
    for wiersz in m:
        print(wiersz)


def unormujMacierz(m):  # normuje macierz
    unormowana = []
    for wiersz in m:
        nowy_wiersz = []
        for i in range(len(wiersz)):
            nowy_wiersz.append(wiersz[i] / 4)
        unormowana.append(nowy_wiersz)
    return unormowana


def transponujMacierz(m):  # transponuje macierz
    nowaMacierz = []
    y = len(m)
    x = len(m[0])
    for i in range(x):
        nowyWiersz = []
        for d in range(y):
            nowyWiersz.append(m[d][i])
        nowaMacierz.append(nowyWiersz)
    return nowaMacierz


def zakodujWektor(wektor, macierz):  # koduje wektor
    zakodowany = []
    macierzTransponowana = transponujMacierz(macierz)
    for i in range(len(macierz[0])):
        suma = 0
        for d in range(len(wektor)):
            suma += wektor[d] * macierzTransponowana[i][d]
        suma = suma % 5
        zakodowany.append(suma)
    return zakodowany


def zasymulujZaklocenia(wekt):  # symuluje zaklocenia wedlug polecenia
    nowyWektor = []
    for i in range(len(wekt)):
        losowaLiczba = random.randint(0, 99)
        skladowaWekt = wekt[i]
        if losowaLiczba < 5:  # aby prawdop. wynosilo 5%
            skladowaWekt += 3
        skladowaWekt = skladowaWekt % 5
        nowyWektor.append(skladowaWekt)
    return nowyWektor


def odlegloscHaminga(v, w):  # wylicza odleglosc Hamminga wg algoryrtmu
    odleglosc = 0
    for i in range(len(v)):
        if (v[i] != w[i]):
            odleglosc += 1
    return odleglosc


def minimizeHammingDistance(C, B, v):
    mozliweSlowa = wygenerujPrzestrzen(B, 5, C)
    m = float("inf")
    for slowo in mozliweSlowa:
        odl = odlegloscHaminga(slowo, v)
        if odl < m:
            m = odl
    L = []
    for slowo in mozliweSlowa:
        if odlegloscHaminga(slowo, v) == m:
            L.append(slowo)
    w = L[random.randint(0, len(L) - 1)]
    return odkodujWektor(B, w, 5)


macierz = wygenerujMacierz(4, 10, 5) #generuje macierz 4x10 w ciele Z5
wypiszMacierz(macierz)               # wypisuje macierz ww. na konsole
unormowanaMacierz = unormujMacierz(macierz) #normuje macierz
#wypiszMacierz(unormowanaMacierz) #wypisuje macierz unormowana
im = plt.imshow(unormowanaMacierz, cmap='Greys') # tworzy obraz ww. macierzy
# plt.show() #wyswietla ten obraz


wektoryDoZakodowania = transponujMacierz(macierzWylosowana) #transponuje macierz - w ten sposob dostajemy wszystkie kolumny jako liste
#wypiszMacierz(wektoryDoZakodowania)
zakodowaneWektory = []
for wektor in wektoryDoZakodowania: # koduje wektory
    print(wektor)
    zakodowanyWektor = zakodujWektor(wektor, macierzG)
    zakodowaneWektory.append(zakodowanyWektor)
print('Zakodowane')
wypiszMacierz(zakodowaneWektory)
#print(zakodowaneWektory)
wyslaneWektory = []
for wektor in zakodowaneWektory:
    wyslaneWektory.append(zasymulujZaklocenia(wektor))
print('Wyslane')
wypiszMacierz(wyslaneWektory)
#print(wyslaneWektory)
# for i in range(len(zakodowaneWektory)):
#     print(zakodowaneWektory[i], wyslaneWektory[i], odlegloscHaminga(zakodowaneWektory[i], wyslaneWektory[i])) #wypisuje wektor zakodowany, wyslany (z zakloceniami), odleglosc hamminga

#for i in range(len(wyslaneWektory)):
    #odkodowanyWektor = minimizeHammingDistance((11,4), macierzG, wyslaneWektory[i])
    #print("Odkodowany", odkodowanyWektor, zakodowaneWektory[i])
    # print(zakodowaneWektory[i], odkodowanyWektor, wyslaneWektory[i], odlegloscHaminga(odkodowanyWektor, wyslaneWektory[i])) # wypisuje wektor odebrany, otrzymany po uzyciu minimizeHammingDistance oraz oryginalny wektor, odlegloscHamminga od oryginalnego


