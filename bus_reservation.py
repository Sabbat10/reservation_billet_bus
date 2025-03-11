# Fonction : Afficher les villes disponibles et valider le choix
def ville_disponible():
    villes = ["Kinshasa", "Lubumbashi", "Goma", "Kisangani", "Mbandaka", 
              "Kananga", "Bukavu", "Matadi", "Kolwezi", "Likasi"]
    
    print("=" * 40)
    print("📍 Voici les villes disponibles :")
    for index, ville in enumerate(villes, start=1):
        print(f"{index}. {ville}")
    
    # Saisie de la ville de départ et d'arrivée avec validation
    depart = input("Veuillez choisir une ville de départ : ").strip()
    arrivee = input("Veuillez choisir une ville d'arrivée : ").strip()
    
    # Vérifier si les villes sont valides (indépendamment de la casse)
    if depart.capitalize() in villes and arrivee.capitalize() in villes:
        print(f"✅ Vous avez choisi de voyager de {depart.capitalize()} à {arrivee.capitalize()}.")
        return depart.capitalize(), arrivee.capitalize()
    else:
        print("❌ Veuillez choisir des villes valides.")
        return ville_disponible()  # Redemander jusqu'à ce que ce soit correct

depart, arrivee = ville_disponible()


# Fonction : Réserver un bus
def reserver_bus():
    print("=" * 40)
    choix_bus = input("Voulez-vous réserver un bus ? (O/N) : ").strip().upper()
    if choix_bus == "O":
        print("🚌 Bus réservé avec succès !")
        return True
    else:
        print("🚫 Annulation de la réservation.")
        return False

bus_reserve = reserver_bus()


# Fonction : Afficher les places disponibles et valider le choix
def seats():
    print("=" * 40)
    print("💺 Voici les places disponibles :")
    for i in range(1, 21):
        print(f"{i}. Place {i}", end="  ")
        if i % 5 == 0:  # Nouvelle ligne tous les 5 sièges pour la lisibilité
            print()
    
    # Validation de l'entrée utilisateur
    while True:
        try:
            choix_place = int(input("Veuillez choisir une place (1-20) : "))
            if 1 <= choix_place <= 20:
                print(f"✅ Vous avez choisi la place {choix_place}.")
                return choix_place
            else:
                print("❌ Choix invalide. Veuillez choisir un numéro entre 1 et 20.")
        except ValueError:
            print("❌ Entrée invalide. Veuillez entrer un nombre.")

choix_place = seats()


# Les informations du passager
def information_passager():
    print("=" * 40)
    print("🧍 Informations du passager :")
    nom = input("Veuillez entrer votre nom : ").strip()
    prenom = input("Veuillez entrer votre prénom : ").strip()
    
    # Validation de l'âge
    while True:
        try:
            age = int(input("Veuillez entrer votre âge : "))
            if age > 0:
                break
            else:
                print("❌ L'âge doit être supérieur à 0.")
        except ValueError:
            print("❌ Entrée invalide. Veuillez entrer un nombre pour l'âge.")
    
    return nom, prenom, age

nom, prenom, age = information_passager()


# Résumé de la réservation
print("=" * 40)
print("🎫 Merci pour votre réservation ! 🎫")
print(f"🔹 Passager : {prenom.capitalize()} {nom.capitalize()}")
print(f"🔹 Âge : {age} ans")
print(f"🔹 Départ : {depart}")
print(f"🔹 Arrivée : {arrivee}")
print(f"🔹 Place : {choix_place}")
if bus_reserve:
    print("🔹 Statut : Bus réservé 🚌")
else:
    print("🔹 Statut : Pas de réservation 🚫")
