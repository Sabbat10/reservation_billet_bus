from bus_reservation import afficher_liste_de_voyage_disponible, rechercher_voyage

while True:
   print("")
   choix_operation = input("1 - Voir les voyages disponibles \n2 - Chercher un voyages\n4 - quitter \nchoix  : ")
   print("")
   
   if choix_operation == "1":
       afficher_liste_de_voyage_disponible()
       
   elif choix_operation == "2":
       depart = input("Entrer ville de depart : ")
       arriver = input("Entrer ville d'arriver : ")
       
       rechercher_voyage(depart, arriver)
       
   elif choix_operation == "4":
       print("Fin du programme !")
       break