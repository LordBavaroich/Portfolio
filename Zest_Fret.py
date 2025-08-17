import random
import time
import pygame
import sys


def print_welcome_banner():
    # Affiche une bannière de bienvenue stylisée.
    print("""
    ███████╗███████╗███████╗████████╗███████╗██╗  ██╗███████╗
    ╚══███╔╝██╔════╝██╔════╝╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝
      ███╔╝ █████╗  ███████╗   ██║   █████╗   ╚███╔╝ █████╗  
     ███╔╝  ██╔══╝  ╚════██║   ██║   ██╔══╝   ██╔██╗ ██╔══╝  
    ███████╗███████╗███████║   ██║██╗███████╗██╔╝ ██╗███████╗
    ╚══════╝╚══════╝╚══════╝   ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
    """)


def play_welcome_music():
    # Initialise Pygame et joue une musique d'accueil en boucle.
    pygame.mixer.init()
    pygame.mixer.music.load("music/Alien Soundtrack Track 1 ”Main Title Jerry Goldsmith.mp3")
    pygame.mixer.music.play(-1)


def get_user_input():
    try:
        # Demande à l'utilisateur des informations nécessaires à la livraison.
        print("\n[Communication en cours avec ZEST.EXE...]\n")
        time.sleep(2)
        print("ZEST.EXE : Bonjour, équipage de l'ACS Fortune. Prêt à recevoir vos coordonnées de livraison.")

        pop_origine = get_numeric_input("Veuillez indiquer la population PUM du monde d'origine: ")
        pop_destination = get_numeric_input("Veuillez indiquer la population PUM de la destination: ")
        spatioport_origine = get_spatioport_input(
            "Veuillez indiquer la classe du spatioport du monde d'origine (A, B, E, X): ")
        spatioport_destination = get_spatioport_input(
            "Veuillez indiquer la classe du spatioport de la destination (A, B, E, X): ")
        tech_origine = get_numeric_input("Veuillez indiquer le Niveau Technologique du monde d'origine: ")
        tech_destination = get_numeric_input("Veuillez indiquer le Niveau Technologique de la destination: ")
        secu_origine = get_security_input("Veuillez indiquer le niveau de sûreté du monde d'origine par G, R ou A: ")
        secu_destination = get_security_input("Veuillez indiquer le niveau de sûreté de la destination par G, R ou A: ")
        distance = get_numeric_input("Veuillez indiquer la distance en parsecs séparant les deux mondes: ")
        effect = get_numeric_input("Veuillez indiquer votre niveau de réussite dans vos recherches: ")

        return pop_origine, pop_destination, spatioport_origine, spatioport_destination, tech_origine, tech_destination, secu_origine, secu_destination, distance, effect

    except ValueError as e:
        # Gère l'erreur en cas de saisie incorrecte.
        print(f"Erreur de saisie : {e}")
        return get_user_input()


def get_numeric_input(prompt):
    # Demande à l'utilisateur une entrée numérique.
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


def get_spatioport_input(prompt):
    # Demande à l'utilisateur la classe du spatioport avec une validation.
    valid_spatioports = {"A", "B", "E", "X"}
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_spatioports:
            return user_input
        print("Entrée invalide. Veuillez choisir parmi les classes de spatioport suivantes : A, B, E, X.")


def get_security_input(prompt):
    # Demande à l'utilisateur le niveau de sûreté avec une validation.
    valid_security_levels = {"G", "R", "A"}
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_security_levels:
            return user_input
        print("Entrée invalide. Veuillez choisir parmi les niveaux de sûreté suivants : G, R, A.")


def calculate_modifier(value, ranges, modifiers):
    # Calcule le modificateur en fonction de plages de valeurs et de modificateurs.
    for r, m in zip(ranges, modifiers):
        if value <= r:
            return m
    return 0


def calculate_traffic(population_origine, population_destination, spatioport_origine, spatioport_destination,
                      tech_origine, tech_destination, secu_origine, secu_destination, distance, effect):
    # Calcule le trafic en fonction des paramètres donnés.
    type_freight_modifier = {"Major": -4, "Incidental": 2, "Minor": 0}
    spatioport_modifier = {"A": 2, "B": 1, "E": -1, "X": -3}

    dm_type_freight = random.choice(list(type_freight_modifier.values()))
    dm_population_origine = calculate_modifier(population_origine, [1, 5, 7], [-4, 0, 2])
    dm_population_destination = calculate_modifier(population_destination, [1, 5, 7], [-4, 0, 2])
    dm_spatioport_origine = spatioport_modifier.get(spatioport_origine, 0)
    dm_spatioport_destination = spatioport_modifier.get(spatioport_destination, 0)
    dm_tech_origine = calculate_modifier(tech_origine, [6, 8], [-1, 0, 2])
    dm_tech_destination = calculate_modifier(tech_destination, [6, 8], [-1, 0, 2])
    dm_secu_origine = calculate_modifier(ord(secu_origine), [ord('G'), ord('R'), ord('A')], [0, -4, -2])
    dm_secu_destination = calculate_modifier(ord(secu_destination), [ord('G'), ord('R'), ord('A')], [0, -4, -2])
    dm_distance = distance - 1

    traffic = random.randint(1, 6) + random.randint(1,
                                                    6) + dm_type_freight + dm_population_origine + dm_population_destination + dm_spatioport_origine + dm_spatioport_destination + dm_tech_origine + dm_tech_destination + dm_secu_origine + dm_secu_destination + dm_distance + effect
    return max(1, traffic)


def number_lots(traffic):
    # Détermine le nombre de lots en fonction du trafic.
    if traffic <= 1:
        lots = 0
    elif 2 <= traffic <= 3:
        lots = random.randint(1, 6) + random.randint(1, 6)
    elif 4 <= traffic <= 5:
        lots = (random.randint(1, 6) + random.randint(1, 6)) * 2
    elif 6 <= traffic <= 8:
        lots = (random.randint(1, 6) + random.randint(1, 6)) * 3
    elif 9 <= traffic <= 11:
        lots = (random.randint(1, 6) + random.randint(1, 6)) * 4
    elif 12 <= traffic <= 14:
        lots = (random.randint(1, 6) + random.randint(1, 6)) * 5
    elif 15 <= traffic <= 16:
        lots = (random.randint(1, 6) + random.randint(1, 6)) * 6
    elif traffic == 17:
        lots = (random.randint(1, 6) + random.randint(1, 6)) * 7
    elif traffic == 18:
        lots = (random.randint(1, 6) + random.randint(1, 6)) * 8
    elif traffic == 19:
        lots = (random.randint(1, 6) + random.randint(1, 6)) * 9
    else:
        lots = (random.randint(1, 6) + random.randint(1, 6)) * 10

    return lots


def generate_lots(lots, type_freight):
    # Génère une liste de lots en fonction du type de fret.
    if type_freight == "Major":
        return [random.randint(1, 6) * 10 for _ in range(lots)]
    elif type_freight == "Incidental":
        return [random.randint(1, 6) for _ in range(lots)]
    else:  # Minor
        return [random.randint(1, 6) * 5 for _ in range(lots)]


def calculate_total_lots(major_lots, minor_lots, incidental_lots):
    total_major_lots = sum(major_lots)
    total_minor_lots = sum(minor_lots)
    total_incidental_lots = sum(incidental_lots)

    return total_major_lots, total_minor_lots, total_incidental_lots


def check_events():
    # Vérifie les événements Pygame, comme la fermeture de la fenêtre.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def main():
    pygame.init()
    print_welcome_banner()
    play_welcome_music()
    print("Bienvenue, équipage de l'ACS Fortune. Initialisation du gestionnaire de livraison exclusif de Zemestang.")
    print(
        "Pour prendre commande, vous devrez rentrer manuellement quelques informations PUM sur le monde d'origine et "
        "la destination")

    user_input = get_user_input()

    print("\nZEST.EXE : Transmission des données à l'infosphère locale... Traitement en cours.")
    pygame.time.delay(random.randint(5000, 10000))

    traffic = calculate_traffic(*user_input)
    lots = number_lots(traffic)

    print("\nZEST.EXE : Contrats trouvés, équipage de l'ACS Fortune. Voici les détails des livraisons :")
    print("ZEST.EXE : Voici les lots Majeurs disponibles : " + str(generate_lots(lots, "Major")))
    print("ZEST.EXE : Voici les lots Incidentels disponibles : " + str(generate_lots(lots, "Incidental")))
    print("ZEST.EXE : Et les lots Mineurs disponibles : " + str(generate_lots(lots, "Minor")))

    user_choice = input("\nZEST.EXE : Souhaitez-vous voir le total des lots (T), ou quitter (Q) ? ").upper()
    if user_choice == "T":
        total_major, total_minor, total_incidental = calculate_total_lots(generate_lots(lots, "Major"),
                                                                          generate_lots(lots, "Minor"),
                                                                          generate_lots(lots, "Incidental"))
        print("\nZEST.EXE : Total des lots Majeurs : ", total_major)
        print("ZEST.EXE : Total des lots Mineurs : ", total_minor)
        print("ZEST.EXE : Total des lots Incidentels : ", total_incidental)
    elif user_choice == "Q":
        pygame.quit()
        sys.exit()
    else:
        print("ZEST.EXE : Choix invalide. Veuillez entrer T ou Q.")
    while True:
        check_events()


if __name__ == "__main__":
    main()
