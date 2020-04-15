class Caisse :
    """Classe Caisse"""

      #constructeur
    def __init__(self) :
        #lister les champs
        self.discount_price = 0.0
        self.total_ht = 0.0
        self.totalTtc = 0.0

    def Total_ht(self, totalHt):
        self.total_ht = self.total_ht + total_ht
        return self

    def Discount(self,total_ht):
        if total_ht > 200:
            discount_price = total_ht * 0.05
            return discount_price

    def TotalTtc(self, total_ht):
        totalTtc = total_ht * 1.2
        return totalTtc