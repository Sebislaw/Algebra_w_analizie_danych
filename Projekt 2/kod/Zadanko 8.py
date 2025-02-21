import random

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


baza = [[1, 0, 0, 0, 0, 4, 4, 2, 0, 1, 1],
        [0, 1, 0, 0, 0, 3, 0, 2, 2, 1, 0],
        [0, 0, 1, 0, 0, 2, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 0, 0, 0, 4, 3, 0]]
kombinacje = []
mod = 5
for i in range(mod):  # tworzymy wszystkie możliwe kombinacje
    for j in range(mod):
        for d in range(mod):
            for e in range(mod):
                kombinacje.append([i, j, d, e])
slowa = []
for kombinacja in kombinacje:
    slowo = []
    for i in range(11):
        element = 0
        element += baza[0][i] * kombinacja[0]
        element += baza[1][i] * kombinacja[1]
        element += baza[2][i] * kombinacja[2]
        element += baza[3][i] * kombinacja[3]
        element %= mod
        slowo.append(element)
    if slowo not in slowa:  # sprawdzamy, czy dany wektor się nie powatrza
        slowa.append(slowo)
M = [[3, 4, 4, 0, 0, 2, 2, 3, 2, 1, 2],
[3, 4, 1, 0, 0, 1, 2, 0, 4, 3, 4],
[3, 2, 0, 4, 4, 3, 2, 0, 0, 2, 3],
[2, 1, 1, 3, 3, 3, 3, 2, 0, 3, 3],
[4, 1, 1, 3, 3, 1, 1, 1, 3, 0, 0],
[2, 1, 3, 0, 0, 0, 1, 3, 0, 3, 2],
[2, 0, 3, 0, 0, 4, 3, 2, 3, 0, 0],
[0, 1, 4, 4, 4, 1, 0, 1, 2, 2, 4],
[0, 0, 2, 1, 1, 0, 0, 1, 3, 2, 2],
[2, 0, 4, 4, 4, 1, 3, 3, 0, 3, 1]]
for wektor in M:
    print(minimizeHammingDistance(slowa, baza, wektor, mod))
#print(minimizeHammingDistance(slowa, baza, v2, mod))

Oryginal = [[3, 4, 4, 0, 0, 2, 2, 3, 2, 1, 2],
[3, 4, 1, 0, 0, 1, 2, 0, 4, 3, 4],
[3, 2, 0, 4, 4, 3, 2, 0, 0, 2, 3],
[2, 1, 1, 3, 3, 3, 3, 2, 0, 3, 3],
[4, 1, 1, 3, 3, 1, 1, 1, 0, 0, 0],
[4, 1, 3, 0, 0, 0, 1, 3, 0, 3, 2],
[2, 0, 3, 0, 0, 4, 3, 2, 3, 0, 0],
[0, 1, 4, 4, 4, 1, 0, 1, 2, 2, 4],
[0, 2, 2, 1, 1, 0, 0, 1, 0, 2, 2],
[2, 0, 4, 4, 4, 1, 3, 3, 0, 3, 1]]

for i in range(len(M)):
    if M[i] != Oryginal[i]:
        print(M[i], Oryginal[i], i)