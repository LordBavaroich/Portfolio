import random
import matplotlib.pyplot as plt
import pickle
import math


class Entreprise:
    def __init__(self, nom, secteur):
        self.nom = nom
        self.secteur = secteur
        self.cours_actuel = random.uniform(10, 100)
        self.historique_cours = [self.cours_actuel]

    def mettre_a_jour_cours(self):
        # Mouvement brownien géométrique pour simuler les fluctuations des prix
        drift = 0.1  # Drift, qui représente la tendance générale du marché
        volatilite = 0.2  # Volatilité, qui représente l'ampleur des fluctuations

        dt = 1  # Écart de temps, ici chaque jour
        brownien = random.gauss(0, math.sqrt(dt))  # Processus de Brownien

        increment = drift * dt + volatilite * brownien
        self.cours_actuel *= math.exp(increment)
        self.historique_cours.append(self.cours_actuel)


class Bourse:
    def __init__(self, duree_jeu=10, capital_initial=None):
        self.entreprises = {"TECHCORP": Entreprise("TechCorp", "Technologie"),
                            "GALAXYTRADE": Entreprise("GalaxyTrade", "Commerce"),
                            "STAREXPLORERS": Entreprise("StarExplorers", "Exploration")}
        self.portefeuille = {nom.upper(): {"Quantite": 0, "Cours": entreprise.cours_actuel} for nom, entreprise in
                             self.entreprises.items()}
        self.solde = capital_initial or 1000  # Utilisez le capital initial fourni ou 1000 par défaut
        self.duree_jeu = duree_jeu

    def acheter_action(self, entreprise, quantite):
        entreprise_upper = entreprise.upper()
        try:
            quantite = int(quantite)
        except ValueError:
            print("Veuillez entrer un nombre valide pour la quantité.")
            return

        if quantite <= 0:
            print("Veuillez acheter au moins une action.")
            return

        cout_total = self.entreprises.get(entreprise_upper, None)
        if not cout_total:
            print(f"L'entreprise {entreprise_upper} n'existe pas.")
            return

        cout_total = cout_total.cours_actuel * quantite
        if cout_total > self.solde:
            print("Vous n'avez pas assez de crédits pour acheter ces actions.")
        else:
            self.solde -= cout_total
            self.portefeuille[entreprise_upper]["Quantite"] += quantite
            self.portefeuille[entreprise_upper]["Cours"] = self.entreprises[entreprise_upper].cours_actuel
            print(f"Vous avez acheté {quantite} actions de {entreprise_upper} pour {cout_total} crédits.")

    def vendre_action(self, entreprise, quantite):
        entreprise_upper = entreprise.upper()
        try:
            quantite = int(quantite)
        except ValueError:
            print("Veuillez entrer un nombre valide pour la quantité.")
            return

        if quantite <= 0:
            print("Veuillez vendre au moins une action.")
            return

        if entreprise_upper not in self.portefeuille:
            print(f"Vous ne possédez pas d'actions de {entreprise_upper}.")
            return

        if self.portefeuille[entreprise_upper]["Quantite"] < quantite:
            print(f"Vous ne possédez pas suffisamment d'actions de {entreprise_upper}.")
        else:
            gain_total = self.entreprises[entreprise_upper].cours_actuel * quantite
            self.solde += gain_total
            self.portefeuille[entreprise_upper]["Quantite"] -= quantite
            self.portefeuille[entreprise_upper]["Cours"] = self.entreprises[entreprise_upper].cours_actuel
            print(f"Vous avez vendu {quantite} actions de {entreprise_upper} pour {gain_total} crédits.")

    def simuler_journee(self):
        for entreprise in self.entreprises.values():
            entreprise.mettre_a_jour_cours()

    def afficher_portefeuille(self):
        print("Votre portefeuille:")
        for nom, details in self.portefeuille.items():
            quantite = details["Quantite"]
            cours = details["Cours"]
            print(f"{nom}: {quantite} actions (Cours actuel: {cours})")
        print(f"Solde: {self.solde} crédits")

    def afficher_cours(self):
        for entreprise in self.entreprises.values():
            print(f"{entreprise.nom} ({entreprise.secteur}): {entreprise.cours_actuel}")

    def afficher_graphique(self):
        fig, ax = plt.subplots()

        for entreprise in self.entreprises.values():
            ax.plot(entreprise.historique_cours, label=f"{entreprise.nom} ({entreprise.secteur})")

        ax.set(xlabel='Jours', ylabel='Cours de l\'action',
               title='Évolution du marché interstellaire')
        ax.legend()
        ax.grid()

        plt.show()

    def interaction_utilisateur(self):
        choix = input("Que souhaitez-vous faire aujourd'hui? (Acheter/A, Vendre/V, Attendre/Enter): ").lower()
        if choix == 'a':
            entreprise = input("Quelle entreprise souhaitez-vous acheter? ").upper()
            quantite = input(f"Combien d'actions de {entreprise} souhaitez-vous acheter? ")
            self.acheter_action(entreprise, quantite)
        elif choix == 'v':
            entreprise = input("Quelle entreprise souhaitez-vous vendre? ").upper()
            quantite = input(f"Combien d'actions de {entreprise} souhaitez-vous vendre? ")
            self.vendre_action(entreprise, quantite)
        elif choix != '':
            print("Choix invalide. Attendez simplement demain.")

    def sauvegarder_partie(self, nom_fichier="sauvegarde_bourse.pkl"):
        with open(nom_fichier, 'wb') as fichier:
            pickle.dump(self, fichier)
        print(f"La partie a été sauvegardée dans {nom_fichier}.")

    def charger_partie(self, nom_fichier="sauvegarde_bourse.pkl"):
        try:
            with open(nom_fichier, 'rb') as fichier:
                obj = pickle.load(fichier)
                self.__dict__.update(obj.__dict__)
            print(f"La partie a été chargée depuis {nom_fichier}.")
        except FileNotFoundError:
            print(f"Aucune sauvegarde trouvée avec le nom {nom_fichier}.")

    def afficher_statistiques(self):
        for jour in range(1, len(self.entreprises["TECHCORP"].historique_cours) + 1):
            print(f"=== Jour {jour} ===")
            for nom, details in self.portefeuille.items():
                quantite = details["Quantite"]
                cours = details["Cours"]
                cout_total = quantite * cours
                print(f"{nom}: {quantite} actions (Cours actuel: {cours}), Valeur totale: {cout_total} crédits")
            print(f"Solde: {self.solde} crédits\n")


# Interaction utilisateur pour entrer le capital initial
capital_initial = input(
    "Entrez votre capital initial (entier positif, appuyez sur Entrée pour utiliser le capital par défaut de 1000) : ")
try:
    capital_initial = int(capital_initial)
    if capital_initial <= 0:
        raise ValueError("Le capital initial doit être un entier positif.")
except ValueError as e:
    print(f"Erreur : {e}. Utilisation du capital par défaut de 1000.")
    capital_initial = None

# Exemple d'utilisation pour un seul joueur avec capital initial personnalisé
bourse = Bourse(duree_jeu=15, capital_initial=capital_initial)

# Simuler la partie avec interaction utilisateur
for jour in range(1, bourse.duree_jeu + 1):
    bourse.simuler_journee()
    print(f"=== Jour {jour} ===")
    bourse.afficher_cours()

    # Afficher le portefeuille du joueur
    bourse.afficher_portefeuille()

    # Interaction utilisateur
    bourse.interaction_utilisateur()

    # Sauvegarder la partie à la fin de chaque jour
    bourse.sauvegarder_partie(f"sauvegarde_jour_{jour}.pkl")

# Afficher les statistiques et le graphique de l'évolution des cours à la fin
bourse.afficher_statistiques()
bourse.afficher_graphique()
