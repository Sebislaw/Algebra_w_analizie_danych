# B = {e1, e2, e3}
# e1 = [1, 0, 0, 2, 4]
# e1 = [0, 1, 0, 1, 0]
# e1 = [0, 0, 1, 5, 6]
# Tworzę macierz A = [e1 e2 e3]
A = [[1, 0, 0, 2, 4],
     [0, 1, 0, 1, 0],
     [0, 0, 1, 5, 6]]
# G = A transpononowane
G = []
for i in range(len(A[0])):
    wiersz = []
    for j in range(len(A)):
        wiersz.append(A[j][i])
    G.append(wiersz)


import random
baza = [[1, 0, 0, 2, 4],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 5, 6]]
kombinacje = []
mod = 7
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


def odlegloscHaminga(v, w):
    odleglosc = 0
    for i in range(len(v)):
        if (v[i] != w[i]):
            odleglosc += 1
    return odleglosc

def minimizeHammingDistance(C, B, v, mod):
    # m = min{d(v, w): wEC}
    m = float("inf")
    for slowo in C:
        odl = odlegloscHaminga(slowo, v)
        if odl < m:
            m = odl
    # L = {wEC: d(v, w) = m}
    L = []
    for slowo in C:
        if odlegloscHaminga(slowo, v) == m:
            L.append(slowo)
    # w - losowo wybrany wektor należący do L
    w = L[random.randint(0, len(L) - 1)]
    # r = wektor współczynników wektora w w bazie B
    r = []
    for i in range(len(baza)):
        wspolczynnik = w[i] / B[i][i]
        for j in range(len(w)):
            w[j] -= wspolczynnik * B[i][j]
            w[j] += mod * mod
            w[j] = w[j] % mod
        r.append(int(wspolczynnik))
    return r

v = [5, 2, 5, 2, 0]
print(minimizeHammingDistance(slowa, baza, v, mod))