# X-O-X Oynunun algoritması

BOŞ = " "
OYUNCU = "X"
BILGISAYAR = "O"

# Boş bir tahta oluştur
def bos_tahta():
    return [[BOŞ, BOŞ, BOŞ],
            [BOŞ, BOŞ, BOŞ],
            [BOŞ, BOŞ, BOŞ]]

# Oyun tahtasını ekrana yazdır
def tahta_yazdir(tahta):
    for row in tahta:
        print(" | ".join(row))
        print("-----------")

# Oyunun bitip bitmediğini kontrol et
def kazanan_kontrol(tahta, oyuncu):
    # Satırları kontrol et
    for row in tahta:
        if all([cell == oyuncu for cell in row]):
            return True

    # Sütunları kontrol et
    for col in range(3):
        if all([tahta[row][col] == oyuncu for row in range(3)]):
            return True

    # Çaprazları kontrol et
    if all([tahta[i][i] == oyuncu for i in range(3)]) or all([tahta[i][2 - i] == oyuncu for i in range(3)]):
        return True

    return False

# Oynanabilir hamleleri listele
def oynanabilir_hamleler(tahta):
    hamleler = []
    for i in range(3):
        for j in range(3):
            if tahta[i][j] == BOŞ:
                hamleler.append((i, j))
    return hamleler

# Min-max algoritması
def minmax(tahta, derinlik, maksimum):
    if kazanan_kontrol(tahta, BILGISAYAR):
        return 1
    if kazanan_kontrol(tahta, OYUNCU):
        return -1
    if len(oynanabilir_hamleler(tahta)) == 0:
        return 0

    if maksimum:
        en_iyi_deger = float("-inf")
        for hamle in oynanabilir_hamleler(tahta):
            satir, sutun = hamle
            tahta[satir][sutun] = BILGISAYAR
            deger = minmax(tahta, derinlik + 1, False)
            tahta[satir][sutun] = BOŞ
            en_iyi_deger = max(en_iyi_deger, deger)
        return en_iyi_deger
    else:
        en_iyi_deger = float("inf")
        for hamle in oynanabilir_hamleler(tahta):
            satir, sutun = hamle
            tahta[satir][sutun] = OYUNCU
            deger = minmax(tahta, derinlik + 1, True)
            tahta[satir][sutun] = BOŞ
            en_iyi_deger = min(en_iyi_deger, deger)
        return en_iyi_deger

# Bilgisayarın en iyi hamlesini bul
def bilgisayarin_hamlesi(tahta):
    en_iyi_deger = float("-inf")
    en_iyi_hamle = None
    for hamle in oynanabilir_hamleler(tahta):
        satir, sutun = hamle
        tahta[satir][sutun] = BILGISAYAR
        deger = minmax(tahta, 0, False)
        tahta[satir][sutun] = BOŞ
        if deger > en_iyi_deger:
            en_iyi_deger = deger
            en_iyi_hamle = hamle
    return en_iyi_hamle

# Oyun fonksiyonu
def x_o_oyunu():
    tahta = bos_tahta()
    oyun_devam_ediyor = True

    while oyun_devam_ediyor:
        tahta_yazdir(tahta)

        # Oyuncunun hamlesi
        satir = int(input("Satır seçin (0, 1, 2): "))
        sutun = int(input("Sütun seçin (0, 1, 2): "))
        if tahta[satir][sutun] != BOŞ:
            print("Bu hücre dolu, lütfen başka bir hücre seçin.")
            continue
        tahta[satir][sutun] = OYUNCU

        # Oyuncunun kazanıp kazanmadığını kontrol et
        if kazanan_kontrol(tahta, OYUNCU):
            tahta_yazdir(tahta)
            print("Tebrikler! Oyuncu kazandı!")
            break

        # Beraberlik kontrolü
        if len(oynanabilir_hamleler(tahta)) == 0:
            tahta_yazdir(tahta)
            print("Oyun berabere!")
            break

        # Bilgisayarın hamlesi
        satir, sutun = bilgisayarin_hamlesi(tahta)
        tahta[satir][sutun] = BILGISAYAR

        # Bilgisayarın kazanıp kazanmadığını kontrol et
        if kazanan_kontrol(tahta, BILGISAYAR):
            tahta_yazdir(tahta)
            print("Üzgünüm, bilgisayar kazandı!")
            break

        # Beraberlik kontrolü
        if len(oynanabilir_hamleler(tahta)) == 0:
            tahta_yazdir(tahta)
            print("Oyun berabere!")
            break

# Oyunu başlat
x_o_oyunu()



