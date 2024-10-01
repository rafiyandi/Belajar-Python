class Mobil:
  def __init__(self, warna, merek, kecepatan):
    self.warna=warna
    self.merek=merek
    self.kecepatan=kecepatan


mobil = Mobil(warna='Hitam', merek='Marcedes', kecepatan='10km')
print(mobil.warna)
