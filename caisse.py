import os
from product import Product 
from order import Order
from order import OrderLine

Catalog = (Product("Banane","Guadeloupe", 4), Product("Pomme","France", 2), Product("Orange", "Espagne", 1.5), Product("Poire", "Italie", 3))

class Caisse :
    """Classe Caisse"""

    def __init__(self):
        self.Order = Order()

    def displayCatalog(self):
        os.system("cls")

        # Affichage de la liste de choix
        print("Liste de produits : ")
        i = 0
        while i < (len(Catalog)):
            product = Catalog[i]
            print("\n" + str(i) + ". " + product.name)
            i = i + 1
        print("\n" + str(i) + ". " + "Fin de saisie")

    def selectProduct(self):
        self.displayCatalog()

        # Gestion de la sélection
        selection = int(input("\nSelectionner un produit : "))
        if ((selection >= 0) and (selection < (len(Catalog)))):
            quantity = float(input("\nQuantité : "))
            self.Order.addLine(Catalog[selection], quantity)
            return True
        elif selection == len(Catalog):
            return False
        else:
            raise EnvironmentError("Invalid selection")
    
    def enterOrder(self):
        selectionEnd = False
        # Saisie des produits et quantités
        while not selectionEnd:
            selectionEnd = not self.selectProduct()

    def printReceipt(self):
        os.system("cls")
        # Entete de ticket
        receipt = "+".ljust(13, '-') + "+".ljust(14, '-') + "+".ljust(14, '-') + "+".ljust(14, '-') + "+" 
        receipt = receipt + "\n|Produit".ljust(14) + "|" + "Prix".ljust(13) + "|" + "Quantité".ljust(13) + "|"  + "Total".ljust(13) + "|" 
        receipt = receipt + "\n+".ljust(14, '-') + "+".ljust(14, '-') + "+".ljust(14, '-') + "+".ljust(14, '-') + "+" 

        # Ligne du ticket
        for orderLine in self.Order.Lines:
            receiptLine = "\n|" + orderLine.Product.Name.ljust(12) + "|"
            receiptLine = receiptLine + str(orderLine.Product.Price).ljust(13) + "|"
            receiptLine = receiptLine + str(orderLine.Quantity).ljust(13) + "|"
            receiptLine = receiptLine + str(orderLine.Total).ljust(13) + "|"
            receipt = receipt + receiptLine

        # Pieds de ticket
        receipt = receipt + "\n+".ljust(14, '-') + "+".ljust(14, '-') + "+".ljust(14, '-') + "+".ljust(14, '-') + "+" 
        receipt = receipt + "\nTotal        : " + str(self.Order.getPreTaxAmount())
        receipt = receipt + "\nRemise       : " + str(self.Order.getDiscount())
        receipt = receipt + "\nTotal HT     : " + str(self.Order.getPreTaxAmount() - self.Order.getDiscount())
        receipt = receipt + "\nTotal TTC    : " + str(self.Order.getAmountIncludingTaxes())
        
        #Affichage du ticket
        print(receipt)