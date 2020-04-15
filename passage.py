class Passage :
    """Classe Passage"""

    #constructeur
    def __init__(self) :
        #lister les champs
        self.products = []
        self.total_ht = 0.0
        self.discount = 0.0
        self.total_tva = 0.0
        self.total_ttc = 0.0

# #saisie des infos
# def write(self):
#     # self.name = input("Nom : ")
#     # self.country = int(input("Pays : "))
#     # self.prize = float(input("Prix : "))
#     #fin saisie 


# #affichage des infos
# def showProducts(self) :
#     print("Son nom est ", self.name)
#     print("Sa provenance est : ", self.country)
#     print("Son prix est ", self.prize)