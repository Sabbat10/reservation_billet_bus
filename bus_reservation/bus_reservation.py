from bus_reservation.data import bus_disponible
from tabulate import tabulate
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

print("==" * 40)
print("== Voici la liste des voyages disponibles ! ==")

# afficher la liste des voyayes
def afficher_liste_de_voyage_disponible():
    for index, trajet in enumerate(bus_disponible):
        print(f"{index + 1} - {trajet['ville_de_depart'].capitalize()} - {trajet['ville_d_arriver'].capitalize()} : Horaire 1.Matin {trajet['horaire_1']} 2.Midi {trajet['horaire_2']}")
        

# recherher un yoyage disponible
def rechercher_voyage(ville_depart, ville_arriver):
    for index, trajet in enumerate(bus_disponible):
        
        # convertir les ville en minuscule
        ville_depart.strip().lower()
        ville_arriver.strip().lower()
        trajet['ville_de_depart'].strip().lower()
        trajet['ville_d_arriver'].strip().lower()
        
        if ville_depart == trajet['ville_de_depart'] and ville_arriver == trajet['ville_d_arriver']:
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
        rechercher_voyage(ville_depart, ville_arriver)
        print(f"Vous avez choisi de voyager de : {trajet['ville_de_depart'].capitalize()} à {trajet['ville_d_arriver'].capitalize()}")
        return
    print("")
    print("Trajet non disponible pour le moment")
    print("== Voici la liste des voyages disponibles ! ==")
    afficher_liste_de_voyage_disponible()
    
    
# def generer_facture(nom, prenom, age, depart, arriver, choisir_siege):
#     header = {
#         "nom": "Nom",
#         "prenom": "Prenom",
#         "age": "Age",
#         "ville_de_depart": "Ville de depart",
#         "ville_d_arriver": "Ville d'arriver",
#         "siege": "Siege choisit"
#     }
    
#     data = {
#         "nom": nom,
#         "prenom": prenom,
#         "age": age,
#         "ville_de_depart": depart,
#         "ville_d_arriver": arriver,
#         "siege": choisir_siege
#     }
    
#     facture = tabulate(data, headers=header, tablefmt="grid")
#     return facture


from tabulate import tabulate

def generer_facture(nom, prenom, age, depart, arriver, choisir_siege):
    header = ["Nom", "Prénom", "Âge", "Ville de départ", "Ville d'arrivée", "Siège choisi"]
    
    data = [[nom, prenom, age, depart, arriver, choisir_siege]]
    
    facture = tabulate(data, headers=header, tablefmt="grid")
    return facture


# Generer une facture PDF
def generer_facture_pdf(nom, prenom, age, depart, arriver, choisir_siege):
    # Créer un canvas PDF
    c = canvas.Canvas("facture_bus.pdf", pagesize=A4)
    width, height = A4
    y = height - 50

    # Titre
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, y, "🧾 FACTURE DE RÉSERVATION")
    y -= 40

    # Informations du passager
    c.setFont("Helvetica", 12)
    c.drawString(100, y, f"👤 Nom : {nom}")
    y -= 20
    c.drawString(100, y, f"🧒 Prénom : {prenom}")
    y -= 20
    c.drawString(100, y, f"🎂 Âge : {age} ans")
    y -= 20

    # Informations sur le trajet
    c.drawString(100, y, f"🚏 Ville de départ : {depart}")
    y -= 20
    c.drawString(100, y, f"🛬 Ville d'arrivée : {arriver}")
    y -= 20
    c.drawString(100, y, f"🪑 Siège choisi : {choisir_siege}")
    y -= 30

    # Pied de page
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(100, y, "Merci d'avoir voyagé avec nous ! Bon trajet 🚌")
    
    # Enregistrement du PDF
    c.save()
    print("✅ Facture PDF générée avec succès : facture_bus.pdf")
