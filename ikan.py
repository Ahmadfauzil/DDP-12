from Animal import  *

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, bisa_konsumsi):
        super().__init__(nama, makanan, hidup, berkembang_biak),
        self.habitat = habitat
        self.bisa_konsumsi = bisa_konsumsi

    def info_ikan(self):
        super().info_animal()
        print("Habitat \t\t :",self.habitat,
              "\nKonsumsi \t\t :",self.bisa_konsumsi)
        
ikan_nila = ikan("Nila","Pelet","Air","Bertelur","Tawar","Untuk dikonsumsi")
ikan_nila.info_ikan()
print('============================================')
ikan_hiu = ikan("Hiu Biru","Ikan Kecil/Cumi","Air","beranak","Air Laut","Tidak untuk dikonsumsi")
ikan_hiu.info_ikan()
print('============================================')