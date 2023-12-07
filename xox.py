"""
@author: Deniz Uku
"""

class XOX:
    def __init__(self):
        self.tahta = [[' '] * 3 for _ in range(3)]
        self.mevcut_oyuncu = "X"

    def oyun_tahtasi_ekran(self):
        for x in self.tahta:
            print("|".join(x))
            print('-' * 4)

    def oyunun_kazanani(self):
        for i in range(3):
            if self.tahta[i][0] == self.tahta[i][1] == self.tahta[i][2] != ' ':
                return True
            if self.tahta[0][i] == self.tahta[1][i] == self.tahta[2][i] != ' ':
                return True
        if self.tahta[0][0] == self.tahta[1][1] == self.tahta[2][2] != ' ' or self.tahta[0][2] == self.tahta[0][1] == self.tahta[2][0] != ' ':
            return True
    def hareket(self,satir,sutun):
        if self.tahta[satir][sutun] == ' ':
            self.tahta[satir][sutun] = self.mevcut_oyuncu
            return True
        return False
    def oyuncu_degis(self):
        self.mevcut_oyuncu = '0' if self.mevcut_oyuncu == 'X' else 'X'

def main():
    oyun = XOX()
    while True:
        oyun.oyun_tahtasi_ekran()
        try:
            satir = int(input('Satırı giriniz (0, 1, 2): '))
            sutun = int(input('Sütunu giriniz (0, 1, 2): '))

            if satir not in (0, 1, 2) or sutun not in (0, 1, 2):
                raise ValueError('Geçersiz değer, lütfen 0, 1 veya 2 girin.')

            if not oyun.hareket(satir, sutun):
                print('Bu hücre zaten dolu, lütfen başka bir hücre seçin.')
                continue

            if oyun.oyunun_kazanani():
                oyun.oyun_tahtasi_ekran()
                print(f'Oyuncu {oyun.mevcut_oyuncu} kazandı!')
                break
            elif all(cell != ' ' for A in oyun.tahta for cell in A):
                oyun.oyun_tahtasi_ekran()
                print('Berabere!')
                break
            else:
                oyun.oyuncu_degis()
        
        except ValueError as e:
            print("Hata: (0,1,2) sayılarından herhangi birini giriniz!")

if __name__ == "__main__":
    main()