from bus_reservation import afficher_liste_de_voyage_disponible, rechercher_voyage, reservation_siege

while True:
   print("")
   choix_operation = input("1 - Voir les voyages disponibles \n2 - Chercher un voyages\n3 - Reserver un siege\n4 - quitter \nchoix  : ")
   print("")
   
   if choix_operation == "1":
       afficher_liste_de_voyage_disponible()
       
   elif choix_operation == "2":
       depart = input("Entrer ville de depart : ")
       arriver = input("Entrer ville d'arriver : ")
       
       rechercher_voyage(depart, arriver)
    
   elif choix_operation == "3":
       
       print("== Voici les siege disponible ==")
       reservation_siege()
       
       
       print("")
       choisir_siege = input("choisir un siege : ")
       
       if choisir_siege.isdigit() and 1 <= int(choisir_siege) <= 21:
           print(f"vous avez choisit le siege : {choisir_siege}🪑 ", )
       else:
           print("La siege n'est pas disponible !")
       
    
   elif choix_operation == "4":
       print("Fin du programme !")
       break