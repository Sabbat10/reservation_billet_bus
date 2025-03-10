def ville_disponible():
    villes = ["Kinshasa", "Lubumbashi", "Goma", "Kisangani", "Mbandaka", "Kananga", "Bukavu", "Matadi", "Kolwezi", "Likasi"]
    
    print("== Voici les villes disponibles: ==")
    for index, ville in enumerate(villes):
        print(f"{index + 1}. {ville}")
        
    # Saisie de la ville de départ et de la ville d'arrivée
    depart = input("Veuillez choisir une ville de départ: ")
    arriver = input("Veuillez choisir uneville d'arrivée: ")

    # Vérifier si la ville est dans la liste (en ignorant la casse)
    if depart.capitalize() in villes and arriver.capitalize() in villes:
        print(f"Vous avez choisi de voyager de {depart.capitalize()} à {arriver.capitalize()}.")
    else:
        print("❌ Veuillez choisir une ville disponible.")

ville_disponible()