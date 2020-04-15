class Product :
    """Classe Product"""

    #constructeur
    def __init__(self, id=None, name="", country="", price=0.0) :
        #lister les champs
        self.id = id
        self.name = name
        self.country = country
        self.price = price
        self.quantity = 0

    #saisie des infos
    def write(self):
        self.name = input("Nom : ")
        self.country = input("Pays : ")
        self.price = float(input("Prix : "))
    #fin saisie 


    #affichage des infos
    def display(self) :
        print("Son nom est :", self.name)
        print("Sa provenance est : ", self.country)
        print("Son prix est de :", self.price,"€")


        