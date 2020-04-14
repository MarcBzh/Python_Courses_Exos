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



#4.1
def showProducts(products) :
    i = 0
    print("ID ", "Nom ", "Prix")
    print("-------------------")

    for product in products.values():
        i += 1
        print(i, " ", product['nom'], " ", product['prix'])

    print("-------------------")


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

# Affichage des produits disponibles
showProducts(products)

subTotalHt = 0
discount = 0
totalHt = 0
total = 0
print("Tapez 0 pour finir la selection")
print("--------------------------------")

while(True):
    # Selection de l'article
    try:
        selectedItem = int(input("Quel article voulez-vous ? (Utiliser l'ID) "))

        # Verification de l'article choisi (si 0, arrêt de la selection)
        if selectedItem == 0:
            break
        else:
            print("Vous avez selectionné : ", products[selectedItem]['nom'])
        product = products[selectedItem]
    except TypeError:
        print("Vous devez indiquer un chiffre !")
        break
    except KeyError:
        print("Cet article n'existe pas !")
        break


    # Selection de la quantité d'article
    quantity = float(input("Quantité: "))

    productPrice = float(product['prix'])

    # Sous-total HT
    subTotalHt += productPrice * quantity

if subTotalHt > 200:
    discount += subTotalHt * 0.05

totalHt = subTotalHt - discount
totalTtc = totalHt + totalHt * 0.2

print()
print()
print("-----------------")
print("Sous-total HT = ", subTotalHt, " €")
if discount > 0:
    print("Remise 5% = ", discount, " €")
print("Total HT = ", totalHt, " €")
print("Total TTC = ", totalTtc, " €")
