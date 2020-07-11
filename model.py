import random

MINA = "*"
ZASTAVICA = "#"
ODKRITO_POLJE = "-"

ZMAGA = "W"
PORAZ = "L"

ZAČETEK = "S"


class Celica(x):
    def __init__(self, mina, vrstica, stolpec):
        self.mina = mina
        self.odkrita = False
        self.z_zastavico = False
        self.vrstica = vrstica
        self.stolpec = stolpec
        # se koordinate mogoce

    def odkrij_celico(self):
        self.odkrita = not self.odkrita

    def postavi_zastavico(self):
        self.z_zastavico = not self.z_zastavico

    def je_mina(self):
        self.mina = True


class Polje():
    def __init__(self, st_vrstic, st_stolpcev, st_min, polja):
        self.st_vrstic = st_vrstic
        self.st_stolpcev = st_stolpcev
        self.st_min = st_min
        self.polja = polja


    def st_min_v_okolici(self, x0, y0, mine):
        #mine je mnozica koordinat z minami
        #tuki moram se dodat sploh notr mine
        st = 0
        for x in (x0 - 1, x0, x0 + 1):
            for y in (y0 - 1, y0, y0 + 1):
                if (x, y) in mine and (x != x0 or y != y0):
                    st += 1
        return st

    def polje_brez_min(self, x0, y0):
        st = st_min_v_okolici(self, x0, y0, mine)
        if st == 0:
            return True
        else:
            return False

    #ko odkriješ vsa polja, kjer ni min
    def zmaga(self):
        for vrstica in self.polja:
            for celica in vrstica:
                if not celica.odkrita and not celica.je_mina:
                    return False
        return True
        
    #odkriješ polje z mino
    def poraz(self):
        #if self.odkrij_celico() and self.je_mina():
         #   return True
        pass


    #ce celica nima min v okolici, odpre tudi vse sosednje celice
    def odpri_polja_v_okolici(self):
        pass
    

    #spremeni stanje igre glede na uporabnikovo ugibanje
    def ugibaj(self, vrstica, stolpec):
        celica = self[vrstica][stolpec]
        #stanje po ugibu
        if celica.je_mina():
            return PORAZ
        
        elif self.zmaga():
            return ZMAGA
        
        else:
            return ODKRITO_POLJE

    #ta funkcija se ni v redu
    def pokazi_vse_mine(self):
        for vrstica in polja:
            for celica in vrstica:
                if celica.je_mina:
                    if not celica.odkrij_celico():
                        celica.odkrita == True
                    else:
                        return celica.odkrita == False