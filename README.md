# 🚌 Système de Réservation de Bus

Un **système de réservation de bus** en Python qui permet aux utilisateurs de :

1. 🗺️ **Afficher les trajets disponibles**
2. 🔍 **Rechercher un voyage spécifique**
3. 🪑 **Réserver un trajet et un siège**
4. 🧾 **Générer une facture**
5. ❌ **Quitter l'application**

---

## 📋 Prérequis

Avant de commencer, assure-toi d'avoir :

- **Python 3.x** installé sur ton système.
- Un gestionnaire de packages comme **pip**.

---

## 📦 Installation

### 1. Cloner le dépôt (ou copier les fichiers)

```bash

git clone https://github.com/Sabbat10/reservation_billet_bus.git
cd reservation_billet_bus

```

### 2. Créer et activer un environnement virtuel

- 👉 Sous Linux/MacOS :

```bash
python3 -m venv venv
source venv/bin/activate
```

- 👉 Sous Windows :

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Exécuter l'application

```bash
python main.py
```

🧰 Fonctionnalités

1. 🗺️ Voir les voyages disponibles
   Affiche une liste des trajets disponibles.
2. 🔍 Rechercher un voyage
   Permet de rechercher un voyage en saisissant :
   La ville de départ
   La ville d'arrivée
3. 🪑 Réserver un trajet et un siège
   Sélectionner un trajet parmi ceux disponibles.
   Choisir un siège (entre 1 et 21).
   Saisir les informations du passager (nom, prénom, âge).
   📊 Générer une facture en format tabulaire.
4. 🧾 Imprimer une facture - (une facture est généré dans votre dossier ave le nom de facture_bus.txt)
5. ❌ Quitter le programme
   Arrête l'application proprement.

## 📊 Exemple d'Exécution

```bash
1 - Voir les voyages disponibles
2 - Chercher un voyage
3 - Réserver un trajet
4 - Imprimer la facture
5 - Quitter
choix : 3

== Voici les sièges disponibles ==
1, 2, 3, ..., 21

== Choisissez un trajet ==
Entrer ville de départ : Kinshasa
Entrer ville d'arrivée : Matadi
✅ Vous avez choisit de voyager des Kinshasa - Matadi

== Choisissez un siège ==
choisir un siège : 12
✅ Vous avez choisi le siège : 12 🪑

== Informations du passager ==
Nom : Lumpantshia
Prenom : Sabbat
Age : 32

== Voici votre facture :
+---------+---------+-----+----------------+----------------+---------------+
| Nom     | Prenom  | Age | Ville de depart| Ville d'arriver| Siege choisit |
+---------+---------+-----+----------------+----------------+---------------+
| Lumpantshia | Sabbat  | 32    | Kinshasa       | Matadi        |  12      |
+---------+---------+-----+----------------+----------------+---------------+

```
