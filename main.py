from tabulate import tabulate
from bus_reservation import afficher_liste_de_voyage_disponible, rechercher_voyage, reservation_bus, reservation_siege

while True:
   print("")
   choix_operation = input("1 - Voir les voyages disponibles \n2 - Chercher un voyages\n3 - Reserver un trajet\n4 - quitter \nchoix  : ")
   print("")
   
   if choix_operation == "1":
       afficher_liste_de_voyage_disponible()
       
   elif choix_operation == "2":
       depart = input("Entrer ville de depart : ")
       arriver = input("Entrer ville d'arriver : ")
       
       rechercher_voyage(depart, arriver)
    
   elif choix_operation == "3":
       
    #    print("== Voici les siege disponible ==")
    #    reservation_siege()
       
       
    #    print("")
    #    choisir_siege = input("choisir un siege : ")
       
    #    if choisir_siege.isdigit() and 1 <= int(choisir_siege) <= 21:
    #        print(f"vous avez choisit le siege : {choisir_siege}🪑 ", )
    #    else:
    #        print("La siege n'est pas disponible !")
    
       print("== Voici les siege disponible ==")
       afficher_liste_de_voyage_disponible()
       
       print("")
       print("== Choissez trajet ==")
       depart = input("Entrer ville de depart : ")
       arriver = input("Entrer ville d'arriver : ")
       reservation_bus(depart, arriver)
       
       print("")
       
       print("== Choissez un  siege ==")
       print("== Voici les siege disponible ==")
       reservation_siege()
       
       
       print("")
       choisir_siege = input("choisir un siege : ")
       
       if choisir_siege.isdigit() and 1 <= int(choisir_siege) <= 21:
           print(f"vous avez choisit le siege : {choisir_siege}🪑 ", )
       else:
           print("La siege n'est pas disponible !")
           
       print("")
       print("== Informations du passager ==")
       nom = input("Nom : ")
       prenom = input("Prenom : ")
       age = input("Age : ")
       
       print("== Voici votre facture :")
    #    print(f"Nom : {nom}")
    #    print(f"Prenom : {prenom}")
    #    print(f"Age : {age}")
    #    print(f"Ville de depart : {depart}")
    #    print(f"Ville d'arriver : {arriver}")
    #    print(f"Siege choisit : {choisir_siege}")
    
       header = {
            "nom" : "Nom",
            "prenom" : "Prenom",
            "age" : "Age",
            "ville_de_depart" : "Ville de depart",
            "ville_d_arriver" : "Ville d'arriver",
            "siege" : "Siege choisit"
        }
       print(tabulate([{"nom" : nom, "prenom" : prenom, "age" : age, "ville_de_depart" : depart, "ville_d_arriver" : arriver, "siege" : choisir_siege}], headers=header, tablefmt="grid"))
    
   elif choix_operation == "4":
       print("Fin du programme !")
       break