"""
By Michał Matuszyk
on 03/05/2023
"""

baza = [[1, 0, 0, 2, 4],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 5, 6]
        ]


def wygenerujPrzestrzen(baza, mod, C):
    wektory = []
    wymiar = len(baza)
    wymiarWektora = len(baza[0])
    for i in range(mod**wymiar):
        wektor = []
        liczba = i
        for d in range(wymiar):
            potega = (wymiar-d-1)
            mianownik = (mod**potega)
            wektor.append(liczba//mianownik)
            liczba = liczba % mianownik
        wektory.append(wektor)
    wynik = []
    for i in range(len(wektory)):
        wektorWynikowy = [0] * wymiarWektora
        wspolrzedne = wektory[i]
        for d in range(wymiar):
            for z in range(wymiarWektora):
                wektorWynikowy[z] += baza[d][z]
        for d in range(wymiarWektora):
            wektorWynikowy[d] = wektorWynikowy[d] % mod
        wynik.append(wektorWynikowy)

    return wynik


def wygenerujSlowaKodowe(baza, mod):
    kombinacje = []
    # mod = 7
    for i in range(mod):  # tworzymy wszystkie możliwe kombinacje
        for j in range(mod):
            for d in range(mod):
                kombinacje.append([i, j, d])

    slowa = []
    for kombinacja in kombinacje:
        slowo = []
        for i in range(5):
            element = 0
            element += baza[0][i] * kombinacja[0]
            element += baza[1][i] * kombinacja[1]
            element += baza[2][i] * kombinacja[2]
            element %= mod
            slowo.append(element)
        if slowo not in slowa:  # sprawdzamy, czy dany wektor się nie powatrza
            slowa.append(slowo)
    return slowa

def odkodujWektor(baza, wektor, mod):
    wspolczynniki = []
    for i in range(len(baza)):
        # if baza[i][i] == 0:
        wspolczynnik = wektor[i]/baza[i][i]
        # print("Wektor:", wektor, "Baza:", baza, "Wspolczynnik:", wspolczynnik)
        for d in range(len(wektor)):
            wektor[d] -= wspolczynnik * baza[i][d]
            wektor[d] += mod*mod
            wektor[d] = wektor[d] % mod
        wspolczynniki.append(int(wspolczynnik))
    return wspolczynniki


# print(slowa)
# print(len(slowa))
#print(len(wygenerujSlowaKodowe(baza, 7)))

#print(int(int(str(5 * 5 * 5 - 1), 10), 5))
