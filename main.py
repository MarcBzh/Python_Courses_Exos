#4.1
from product import Product 
from caisse import Caisse
from passage import Passage


products = {
    1: {
        'nom': "Banane",
        "prix": 4,
    },
    2: {
        'nom': "Pomme",
        "prix": 2,
    },
    3: {
        'nom': "Orange",
        "prix": 1.5,
    },
    4: {
        'nom': "Poire",
        "prix": 3,
    },
}

product_list = [
    Product(1,"banane","afrique",4),
    Product(2,"pomme","france",2),
    Product(3,"orange","espagne",1.5),
    Product(4,"poire","france",3),
]

for product in product_list :
    product.display()


def showProducts(products) :
    i = 0
    print("ID ", "Nom ", "Prix")
    print("-------------------")

    for product in products.values():
        i += 1
        print(i, " ", product['nom'], " ", product['prix'])

    print("-------------------")


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
