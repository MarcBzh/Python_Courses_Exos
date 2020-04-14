# -*- coding: utf-8 -*-
# # #3.1

# # prixHt=float(input("Entrez un prix HT :"))

# # qte=float(input("Entrez une quantité svp :"))

# # prixTotalHt=(prixHt * qte)

# # prixTotalTTC=(prixTotalHt * 1.2)

# # if prixTotalTTC > 200:
# #     prixTotalTTC -= prixTotalTTC * 0.05

# # print ('le total est de', prixTotalTTC)

# # "3.2"
# # total = 0
# # products = int(input("Nombre de produits:"))

# # for i in range(0, products):
# #     prixHt = float(input("prix hors taxe: "))
# #     qte = float(input("Quantité: "))

# #     prix =  prixHt + (prixHt * 1.2)
# #     sousTotal = prix * qte

# #     if sousTotal > 200:
# #         sousTotal -= sousTotal * 0.05

# #     total += sousTotal

# # print ("Le total est de", total)



"4.1"

products = {
    1: {
        'nom': "Banane",
        "prix": 4
    },
    2: {
        'nom': "Pomme",
        "prix": 2
    },
    3: {
        'nom': "Orange",
        "prix": 1.5
    },
    4: {
        'nom': "Poire",
        "prix": 3
    }
}

def showProducts(products) :
    i = 0
    print("ID ", "Nom ", "Prix")
    print("-------------------")

    for product in products.values():
        i += 1
        print(i, " ", product['nom'], " ", product['prix'])

    print("-------------------")


showProducts(products)

try:
    for id in range (products):
except expression:
    print("Une erreur est survenue")
else:
    print("Bloc exécuté en l’absence d’erreur")
finally:
    print("Bloc toujours exécuté")


