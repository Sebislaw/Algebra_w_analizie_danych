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
    for i in range(len(B)):
        wspolczynnik = w[i] / B[i][i]
        for j in range(len(w)):
            w[j] -= wspolczynnik * B[i][j]
            w[j] += mod * mod
            w[j] = w[j] % mod
        r.append(int(wspolczynnik))
    return r