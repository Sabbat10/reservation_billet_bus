from bus_reservation.bus_reservation import afficher_liste_de_voyage_disponible, rechercher_voyage, reservation_bus, reservation_siege, generer_facture, generer_facture_pdf

while True:
   print("")
   choix_operation = input("🚌 1 - Voir les voyages disponibles\n🔍 2 - Chercher un voyage\n📝 3 - Réserver un trajet\n🧾 4 - Imprimer la facture\n❌ 5 - Quitter\n👉 Choix : ")

   print("")
   
   if choix_operation == "1":
       print("== Voici les siege disponible ==")
       afficher_liste_de_voyage_disponible()
       
   elif choix_operation == "2":
       
    
    depart = input("Entrer ville de depart : ")
    arriver = input("Entrer ville d'arriver : ")
    
    if depart == "" or arriver == "":
        print("")
        print("❌Veuillez entrer une ville de depart et une ville d'arriver")
    else:
        rechercher_voyage(depart, arriver)
    
   elif choix_operation == "3":
    
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
    
       facture = generer_facture(nom, prenom, age, depart, arriver, choisir_siege)
       print(facture)
       
   elif choix_operation == "4":
    try:
        facture = generer_facture_pdf(nom, prenom, age, depart, arriver, choisir_siege)
        print("Facture généré ave succès !")
    except NameError:
        print("Aucune réservation trouvée. Veuillez d'abord réserver un trajet.")
       
     
     
   elif choix_operation == "5":
       print("Fin du programme !")
       break