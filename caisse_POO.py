import os
from product import Product 
from caisse import Caisse
from order import Order

# Variables globales
cashier = Caisse()

def main():
	# Declaration des variables
	global cashier

	cashier.enterOrder()

	cashier.printReceipt()

# Execution du programme
main()