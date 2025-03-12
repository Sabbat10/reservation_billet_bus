from bus_reservation import afficher_liste_de_voyage_disponible

while True:
   choix_operation = input("1 - Voir les voyages disponibles \n2 - Chercher un voyages\n4 - quitter \nchoix  : ")
   
   if choix_operation == "1":
       afficher_liste_de_voyage_disponible()
       
   elif choix_operation == "4":
       print("Fin du programme !")
       break