import os
import math
import numpy
from PIL import Image

# Zapisanie obrazu
def png_write(img, filepath):
    img = Image.fromarray((numpy.array(img) * 255).astype(numpy.uint8), 'L')
    img.save(filepath)


# zwraca listę z najmniejszą i największą wartością z macierzy
def min_max(A):
    minimum = A[0][0]
    maksimum = A[0][0]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > maksimum:
                maksimum = A[i][j]
            if A[i][j] < minimum:
                minimum = A[i][j]
    return [minimum, maksimum]
# zmienia obraz na czarno-biały, piksele o intensywności > p zamienia na 1, a resztę na 0
# def czarno_bialy(A, p):
#     n = len(A)
#     m = len(A[0])
#     wynik = [[0] * m for i in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if A[i][j] > p:
#                 wynik[i][j] = 1
#    return wynik
# wersja 2
def czarno_bialy(A):
    n = len(A)
    m = len(A[0])
    minimum_maksimum = min_max(A)
    p = (minimum_maksimum[0] + minimum_maksimum[1]) / 2
    wynik = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if A[i][j] > p:
                wynik[i][j] = 1
    return wynik

def srednia_odleglosc_od_wzorca(pismo, wzorzec):
    rozmiar = len(wzorzec)
    piksel_z_kolei = 0
    lista_minimalnych_odleglosci = [0 for i in range(len(wzorzec)*len(wzorzec))]
    # biorę każdy piksel z danej macierzy
    for i in range(rozmiar):
        for j in range(rozmiar):
            # porównuję go z każdym pikselem ze wzorca i liczę odległość
            if pismo[i][j] == 0:
                min_odleglosc = 2 * rozmiar
                for i2 in range(rozmiar):
                    for j2 in range(rozmiar):
                        if wzorzec[i2][j2] == 0:
                            odleglosc = abs(i - i2) + abs(j - j2) # metryka miejska
                            # odleglosc = ((i - i2)**2 + (j-j2)**2)**(1/2) # euklidesowa jest wolniejsza
                            if min_odleglosc > odleglosc:
                                min_odleglosc = odleglosc
                                if min_odleglosc == 0:
                                    break
                    if min_odleglosc == 0:
                        break
                lista_minimalnych_odleglosci[piksel_z_kolei] = min_odleglosc
                piksel_z_kolei += 1
    usredniona_odleglosc = 0
    for i in range(len(lista_minimalnych_odleglosci)):
        usredniona_odleglosc += lista_minimalnych_odleglosci[i]
    return usredniona_odleglosc / piksel_z_kolei

def wycentrowanie_obrazu(oryginal_img):
    # otrzymuje typ image i próg_przerzucenia
    # usuwa z obrazu brzegi, gdzie nie ma cyfry (w osi y)
    # przywraca pierwotny rozmiar obrazu rozciągając go, aby cyfra dotykała ścianek
    # zwraca typ image
    img = czarno_bialy((numpy.array(oryginal_img) / 255).reshape(oryginal_img.size[1], oryginal_img.size[0]).tolist())
    rozmiar = len(img)
    pusta_przestrzen_lewo_x = 0
    pusta_przestrzen_prawo_x = 0
    pusta_przestrzen_dol_y = 0
    pusta_przestrzen_gora_y = 0
    for i in range(rozmiar):
        for j in range(rozmiar):
            if img[i][j] == 0:
                if pusta_przestrzen_gora_y == 0:
                    pusta_przestrzen_gora_y = i
                pusta_przestrzen_dol_y = rozmiar - i - 1
                if pusta_przestrzen_lewo_x > j or pusta_przestrzen_lewo_x == 0:
                    pusta_przestrzen_lewo_x = j
                if pusta_przestrzen_prawo_x < j or pusta_przestrzen_prawo_x == 0:
                    pusta_przestrzen_prawo_x = j
    pusta_przestrzen_prawo_x = rozmiar - pusta_przestrzen_prawo_x - 1
    oryginal_img = oryginal_img.crop((0, pusta_przestrzen_gora_y,
                                      rozmiar, rozmiar - pusta_przestrzen_dol_y))
    return oryginal_img.resize((rozmiar, rozmiar))

# Wczytanie obrazu
def png_read(filepath):
    # operuje na typie PIL.Image.image
    # zwraca macierz
    img = Image.open(filepath).convert('L')
    return (numpy.array(img) / 255).reshape(img.size[1], img.size[0]).tolist()
# wersja 2
def png_read_normalised(filepath):
    # operuje na typie PIL.Image.image
    # wyśrodkowuje, przerzuca kolory na czarny i biały
    # zwraca znormalizowaną macierz
    img = Image.open(filepath).convert('L')
    img = wycentrowanie_obrazu(img)
    return czarno_bialy((numpy.array(img) / 255).reshape(img.size[1], img.size[0]).tolist())


def main():
    # lista zawiera pola, ktore są postaci [obraz, indeks serii, indeks cyfry]
    znormalizowane_obrazy_do_testowania = [[png_read_normalised(f'./pismo/pismo_seria{j}_{i}.png'), j, i] for j in range(1, 3) for i in range(0, 10)]
    znormalizowane_wzorce = [[png_read_normalised(f'./wzorce/wzorzec_seria{j}_{i}.png'), j, i] for j in range(1, 4) for i in range(0, 10)]

    dobrze_odgadniete = 0
    zle_odgadniete = 0
    for pismo in znormalizowane_obrazy_do_testowania:
        predykcje = [] # lista zawierająca [cyfra ze wzorca, odległość od tego wzorca, zgodność ze wzorcem w %]
        minimalna_odleglosc_od_wzorca = float('inf')
        for wzorzec in znormalizowane_wzorce:
            temp = srednia_odleglosc_od_wzorca(pismo[0], wzorzec[0])
            zgodność = round(100 - temp * 100 / 27)
            predykcje.append([wzorzec[2], temp, zgodność])
            if minimalna_odleglosc_od_wzorca > temp:
                minimalna_odleglosc_od_wzorca = temp
                odczytana_cyfra = wzorzec[2]
        predykcje.sort(key=lambda x: x[1])

        # KNN
        k = 3
        # głosowanie = [cyfra, ilość głosów]
        glosowanie = [[i, 0] for i in range(10)]
        for i in range(k):
            glosowanie[predykcje[i][0]][1] += 1
        glosowanie.sort(reverse=True, key=lambda x: x[1])

        # klasyfikacja
        if (glosowanie[0][1] == glosowanie[1][1]):
            klasyfikacja = predykcje[0][0]
        else:
            klasyfikacja = glosowanie[0][0]

        print(f"Obraz z cyfrą {pismo[2]} odczytano jako cyfra {klasyfikacja}.\t", end = '')
        if pismo[2] == klasyfikacja:
            dobrze_odgadniete += 1
            print("DOBRZE")
        else:
            zle_odgadniete += 1
            print("ŹLE")
    print(f"Odczytano poprawnie {dobrze_odgadniete} z {dobrze_odgadniete + zle_odgadniete}, czyli {round((dobrze_odgadniete*100)/(dobrze_odgadniete + zle_odgadniete))}%")

if __name__ == "__main__":
    main()
