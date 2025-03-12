# ville disponible
bus_disponible = [
    {
        "ville_de_depart" : "kinshasa",
        "ville_d_arriver": "matadi",
        "horaire_1":  "08h00",
        "horaire_2": "14h00"
    },
    
     {
        "ville_de_depart" : "matadi",
        "ville_d_arriver": "Kinshasa",
        "horaire_1":  "08h00",
        "horaire_2": "14h00"
    },
     
      {
        "ville_de_depart" : "kinshasa",
        "ville_d_arriver": "bandundu",
        "horaire_1":  "08h00",
        "horaire_2": "14h00"
    },
    {
        "ville_de_depart" : "bandundu",
        "ville_d_arriver": "kinshasa ",
        "horaire_1":  "08h00",
        "horaire_2": "14h00"
    }
      
]

print("==" * 40)
print("== Voici la liste des voyages disponibles ! ==")

def afficher_liste_de_voyage_disponible():
    for index, trajet in enumerate(bus_disponible):
        print(f"{index + 1} - {trajet['ville_de_depart'].capitalize()} - {trajet['ville_d_arriver'].capitalize()} : Horaire 1.Matin {trajet['horaire_1']} 2.Midi {trajet['horaire_2']}")
        