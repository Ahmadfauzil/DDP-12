from Animal import*

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak_sisik, berbisa):
        super().__init__(nama, makanan, hidup, berkembang_biak),
        self.corak_sisik = corak_sisik
        self.berbisa = berbisa

    def info_ular(self):
        super().info_animal()
        print("Corak_Sisik \t\t :",self.corak_sisik,
              "\nBerbisa \t\t :",self.berbisa)
        
ular_piton = ular("Pyhthon","daging","semak-semak","bertelur","kembang-kembang","tidak berbisa",)
ular_piton.info_ular()
print('============================================')
ular_cobra = ular("Cobra","daging / tikus","Rawa - semak","bertelur","Hitam","berbisa")
ular_cobra.info_ular()
print('============================================')