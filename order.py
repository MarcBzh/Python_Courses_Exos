class OrderLine :
    """Classe OrderLine"""
    def __init__(self, Product, Quantity):
        self.Product = Product
        self.Quantity = Quantity
        self.Total = self.Product.Price * Quantity

class Order :
      #constructeur
    def __init__(self):
        self.Lines = []
        
    def addLine(self, Product, Quantity):
        self.Lines.append(OrderLine(Product, Quantity))

    def getPreTaxAmount(self):
        amount = 0
        for line in self.Lines:
            amount += line.Total
        return amount

    def getDiscount(self):
        if self.getPreTaxAmount() >= 200:
            return self.getPreTaxAmount() * 0.05
        else:
            return 0

    def getAmountIncludingTaxes(self):
        amount = self.getPreTaxAmount()
        amount = amount - self.getDiscount()
        amount = amount * 1.2
        return amount





    # def __init__(self) :
    #     #lister les champs
    #     self.discount_price = 0.0
    #     self.total_ht = 0.0
    #     self.totalTtc = 0.0

    # def Total_ht(self, totalHt):
    #     self.total_ht = self.total_ht + total_ht
    #     return self

    # def Discount(self,total_ht):
    #     if total_ht > 200:
    #         discount_price = total_ht * 0.05
    #         return discount_price

    # def TotalTtc(self, total_ht):
    #     totalTtc = total_ht * 1.2
    #     return totalTtc