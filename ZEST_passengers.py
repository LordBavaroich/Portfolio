import random

import pygame

from Zest_Fret import check_events


def print_welcome_banner():
    # Fonction pour afficher une bannière de bienvenue.
    print("""
    ███████╗███████╗███████╗████████╗███████╗██╗  ██╗███████╗
    ╚══███╔╝██╔════╝██╔════╝╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝
      ███╔╝ █████╗  ███████╗   ██║   █████╗   ╚███╔╝ █████╗  
     ███╔╝  ██╔══╝  ╚════██║   ██║   ██╔══╝   ██╔██╗ ██╔══╝  
    ███████╗███████╗███████║   ██║██╗███████╗██╔╝ ██╗███████╗
    ╚══════╝╚══════╝╚══════╝   ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
                                                             """)
    print("Bienvenue dans ZEST_Passengers ! ")
    print(
        "Pour poster une annonce dans la cybersphère locale, veuillez rentrer la distance du trajet, la population du "
        "monde d'origine et de destination selon la notation PUM, la classe de spatioport du monde d'origine et de "
        "destination, ainsi que le niveau de certification de votre steward/hôtesse de l'espace.")
    print()


def play_welcome_music():
    pygame.mixer.init()
    pygame.mixer.music.load(
        "music/Alien Soundtrack Track 1 ”Main Title Jerry Goldsmith.mp3")  # Remplacez par le chemin de votre fichier
    # audio
    pygame.mixer.music.play(-1)  # -1 pour jouer en boucle


def get_user_input():
    # Fonction pour obtenir les entrées utilisateur nécessaires pour générer le trafic de passagers.
    try:
        distance_pc = get_integer_input("Distance en parsec: ")
        pop_origine = get_integer_input("Population du monde d'origine: ")
        pop_destination = get_integer_input("Population de la destination: ")
        spatioport_origine = get_spatioport_input("Classe du spatioport d'origine: ")
        spatioport_destination = get_spatioport_input("Classe du spatioport de destination: ")
        steward_skill = get_integer_input("Niveau de certification du steward/hôtesse: ")
        effect_skill_check = get_integer_input("Niveau de réussite du test de compétence: ")
        zone_origine = get_zone_input("Notez A pour zone Ambre, R pour zone Rouge, G pour zone Verte: ")
        zone_destination = get_zone_input("Notez A pour Ambre, R pour Rouge, G pour verte: ")

        return distance_pc, pop_origine, pop_destination, spatioport_origine, spatioport_destination, steward_skill, effect_skill_check, zone_origine, zone_destination

    except ValueError as e:
        print(f"Erreur: {e}")
        raise


def get_integer_input(prompt):
    # Fonction pour obtenir une entrée numérique de l'utilisateur.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Erreur: Veuillez entrer une valeur numérique.")


def get_spatioport_input(prompt):
    # Fonction pour obtenir une entrée valide pour la classe de spatioport de l'utilisateur.
    valid_classes = ["A", "B", "E", "X"]
    while True:
        spatioport_class = input(prompt).upper()
        if spatioport_class in valid_classes:
            return spatioport_class
        else:
            print("Erreur: Classe de spatioport invalide. Veuillez entrer A, B, E, ou X.")


def get_zone_input(prompt):
    # Fonction pour obtenir une entrée valide pour la note de zone de l'utilisateur.
    valid_zones = ["A", "R", "G"]
    while True:
        zone = input(prompt).upper()
        if zone in valid_zones:
            return zone
        else:
            print("Erreur: Note de zone invalide. Veuillez entrer A, R, ou G.")


def calculate_passenger_traffic(distance_pc, pop_origine, pop_destination, spatioport_origine, spatioport_destination,
                                steward_skill, effect_skill_check, zone_origine, zone_destination):
    # Fonction pour calculer le trafic de passagers en fonction des paramètres fournis.
    DM_destination = distance_pc - 1

    if pop_origine <= 1:
        DM_pop_origine = -4
    elif pop_origine in range(6, 7):
        DM_pop_origine = 1
    elif pop_origine >= 8:
        DM_pop_origine = 3
    else:
        DM_pop_origine = 0

    if pop_destination <= 1:
        DM_pop_destination = -4
    elif pop_destination in range(6, 7):
        DM_pop_destination = 1
    elif pop_destination >= 8:
        DM_pop_destination = 4
    else:
        DM_pop_destination = 0

    if spatioport_origine == "A":
        DM_spatioport_origine = 2
    elif spatioport_origine == "B":
        DM_spatioport_origine = 1
    elif spatioport_origine == "E":
        DM_spatioport_origine = -1
    elif spatioport_origine == "X":
        DM_spatioport_origine = -3
    else:
        DM_spatioport_origine = 0

    if spatioport_destination == "A":
        DM_spatioport_destination = 2
    elif spatioport_destination == "B":
        DM_spatioport_destination = 1
    elif spatioport_destination == "E":
        DM_spatioport_destination = -1
    elif spatioport_destination == "X":
        DM_spatioport_destination = -3
    else:
        DM_spatioport_destination = 0

    if zone_origine == "A":
        DM_zone_origine = 1
    elif zone_origine == "R":
        DM_zone_origine = -4
    else:
        DM_zone_origine = 0

    if zone_destination == "A":
        DM_zone_destination = 1
    elif zone_destination == "R":
        DM_zone_destination = -4
    else:
        DM_zone_destination = 0

    # Retourne un dictionnaire contenant le trafic de passagers pour chaque classe.
    return {
        "Low": random.randint(2,
                              12) + steward_skill + effect_skill_check + DM_destination + DM_pop_origine + DM_pop_destination + DM_spatioport_origine + DM_spatioport_destination + DM_zone_origine + DM_zone_destination + 1,
        "Basic": random.randint(2,
                                12) + steward_skill + effect_skill_check + DM_destination + DM_pop_origine + DM_pop_destination + DM_spatioport_origine + DM_spatioport_destination + DM_zone_origine + DM_zone_destination,
        "Middle": random.randint(2,
                                 12) + steward_skill + effect_skill_check + DM_destination + DM_pop_origine + DM_pop_destination + DM_spatioport_origine + DM_spatioport_destination + DM_zone_origine + DM_zone_destination,
        "High": random.randint(2,
                               12) + steward_skill + effect_skill_check + DM_destination + DM_pop_origine + DM_pop_destination + DM_spatioport_origine + DM_spatioport_destination + DM_zone_origine + DM_zone_destination - 4
    }


def print_result(passenger_traffic):
    # Fonction pour imprimer le nombre de passagers générés pour chaque classe.
    for passenger_class, traffic in passenger_traffic.items():
        print(f"Le nombre de passagers de classe {passenger_class} générés est: {calculate_number_passengers(traffic)}")


def calculate_number_passengers(traffic):
    # Fonction pour calculer le nombre de passagers en fonction du trafic de passagers.
    if traffic <= 1:
        return 0
    elif traffic in range(2, 3):
        return random.randint(1, 6)
    elif traffic in range(4, 6):
        return random.randint(1, 6) + random.randint(1, 6)
    elif traffic in range(7, 10):
        return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    elif traffic in range(11, 13):
        return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    elif traffic in range(14, 15):
        return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1,
                                                                                                   6) + random.randint(
            1, 6)
    elif traffic == 16:
        return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1,
                                                                                                   6) + random.randint(
            1, 6) + random.randint(1, 6)
    elif traffic == 17:
        return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1,
                                                                                                   6) + random.randint(
            1, 6) + random.randint(1, 6) + random.randint(1, 6)
    elif traffic == 18:
        return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1,
                                                                                                   6) + random.randint(
            1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    elif traffic == 19:
        return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1,
                                                                                                   6) + random.randint(
            1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
    else:
        return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1,
                                                                                                   6) + random.randint(
            1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1,
                                                                                                        6) + random.randint(
            1, 6)


if __name__ == "__main__":
    print_welcome_banner()
    pygame.init()
    play_welcome_music()

    try:
        while True:
            user_input = get_user_input()
            passenger_traffic = calculate_passenger_traffic(*user_input)
            print_result(passenger_traffic)

            continue_prompt = input("Voulez-vous générer des passagers pour une autre configuration? (Oui/Non): ")
            if continue_prompt.lower() != "oui":
                break
        while True:
            check_events()

    except ValueError as e:
        print(f"Erreur: {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite: {e}")
