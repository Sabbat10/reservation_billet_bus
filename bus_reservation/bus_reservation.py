from bus_reservation.data import bus_disponible

print("==" * 40)
print("== Voici la liste des voyages disponibles ! ==")

# afficher la liste des voyayes
def afficher_liste_de_voyage_disponible():
    for index, trajet in enumerate(bus_disponible):
        print(f"{index + 1} - {trajet['ville_de_depart'].capitalize()} - {trajet['ville_d_arriver'].capitalize()} : Horaire 1.Matin {trajet['horaire_1']} 2.Midi {trajet['horaire_2']}")
        

# recherher un yoyage disponible
def rechercher_voyage(ville_depart, ville_arriver):
    for index, trajet in enumerate(bus_disponible):
        if ville_depart.strip().lower() == trajet['ville_de_depart'].strip().lower() and ville_arriver.strip().lower() == trajet['ville_d_arriver'].strip().lower():
            print("")
            print(f"Trajet : {trajet['ville_de_depart'].capitalize()} - {trajet['ville_d_arriver'].capitalize()} est disponible")
            print(f"Horaires disponibles : Matin {trajet['horaire_1']} - Midi {trajet['horaire_2']}"  )
            return
    print("")
    print("Trajet non disponible pour le moment")
    

# reservation de siege

def reservation_siege():
    for i in range(1, 22):
        print(f"{i}🪑", end=' ')
        if i % 5 == 0:
            print()  # Revenir à la ligne après chaque groupe de 5 nombres

# reservation bus

def reservation_bus(ville_depart, ville_arriver):
    for index, trajet in enumerate(bus_disponible):
        if ville_depart.strip().lower() == trajet['ville_de_depart'].strip().lower() and ville_arriver.strip().lower() == trajet['ville_d_arriver'].strip().lower():
            print("")
            print(f"Vous avez choisi de voyager de : {trajet['ville_de_depart'].capitalize()} à {trajet['ville_d_arriver'].capitalize()}")
            return
    print("")
    print("Trajet non disponible pour le moment")
    print("== Voici la liste des voyages disponibles ! ==")
    afficher_liste_de_voyage_disponible()
    
    
# def facture(nom, prenom, age, ville_de_depart, ville_d_arriver, choisir_siege):
