from bus_reservation.data import bus_disponible
from tabulate import tabulate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

print("==" * 40)
print("== Voici la liste des voyages disponibles ! ==")

# afficher la liste des voyayes
def afficher_liste_de_voyage_disponible():
    for index, trajet in enumerate(bus_disponible):
        print(f"{index + 1} - {trajet['ville_de_depart'].capitalize()} - {trajet['ville_d_arriver'].capitalize()} : Horaire 1.Matin {trajet['horaire_1']} 2.Midi {trajet['horaire_2']}")
        

# recherher un yoyage disponible
def rechercher_voyage(ville_depart, ville_arriver):
    for trajet in bus_disponible:
        
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
    
# Generation de facture
def generer_facture(nom, prenom, age, depart, arriver, choisir_siege):
    header = ["Nom", "Prénom", "Âge", "Ville de départ", "Ville d'arrivée", "Siège choisi"]
    
    data = [[nom, prenom, age, depart, arriver, choisir_siege]]
    
    facture = tabulate(data, headers=header, tablefmt="grid")
    return facture

# Generation de facture
def generer_facture_pdf(nom, prenom, age, depart, arriver, choisir_siege):
    doc = SimpleDocTemplate("facture_bus.pdf", pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("🧾 <b>FACTURE DE RÉSERVATION</b>", styles["Title"])
    elements.append(title)

    # Données de la facture sous forme de tableau
    data = [
        ["👤 Nom", nom.capitalize()],
        ["🧒 Prénom", prenom.capitalize()],
        ["🎂 Âge", f"{age} ans"],
        ["🚏 Ville de départ", depart.capitalize()],
        ["🛬 Ville d'arrivée", arriver.capitalize()],
        ["🪑 Siège choisi", choisir_siege]
    ]

    table = Table(data, colWidths=[150, 250])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkblue),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))

    elements.append(table)

    # Note de bas de page
    elements.append(Paragraph("🚍 Merci d'avoir voyagé avec nous !", styles["Normal"]))

    doc.build(elements)
    print("✅ Facture PDF générée avec succès : facture_bus.pdf")
