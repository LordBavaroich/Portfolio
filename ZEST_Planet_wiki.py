# Le but de ce programme est de donner des informations sur la planète à partir du PUM (UPP) et des classifications
# commerciales
# L'utilisateur en entrant le nom de la planète doit voir s'afficher une description de ses caractéristiques PUM (UPP)
# et de ses classifications commerciales.

# Voici les informations sous forme de liste, le premier élément est le nom, le second le PUM (UPP), les suivants les
# classifications commerciales :
# Sharristan - E8A4599-2 - Fl Ni
# Merchollon - E302457-8 - Ic Ni Va
# Sidika - B566689-9 - S Ag Ni Ri
# Libitini - B5415A6-9 - Ni Po
# Lyallia - X9B8757-3 - Fl
# Arthan - D240336-4 - De Lo Po
# Erissen - B654854-6 -
# GHANISUS - B250956-A - De Hi Po
# JIMANN - D0009AD-9 - As Hi In Na
# Marilior - B677320-B - S Lo
# Gunnandup - C347884-7 - S
# Intheradas - C100685-8 - Na Ni Va
# MANNECA - B5129B9-B - Hi Ic In Na
# Senelot - A551400-B - Ni Po
# Sagueneus - D7A4222-3 - Fl Lo
# Karino - C242430-6 - S Ni Po
# JIHLAVENKO - A8D19CD-A - S Fl Hi
# GUERNIUM - B445967-D - Hi In Co
# Leoncipidas - E7A2441-6 - Fl Ni
# Galy Fiver - C100534-C - S Ni Va
# McCuskenia - C410459-7 - Ni
# Wurzburnin - C440550-7 - De Ni Po
# RENALEEN - E5009A8-6 - Hi In Na Va
# Jurburgilis - X879684-0 - Ni
# CEPLECHT - C52799D-6 - S Hi In Co
# CHERALDIVIA - A2369DE-9 - Hi
# Kulinderso - D75A662-3 - Ni Wa
# Parvillon - B895200-8 - N Lo
# Gulincelope - D65A300-5 - Lo Wa
# Vilipedi - C141323-A - Lo Po
# Romederblom - A554205-C - Lo
# Vilk - B538A77-C - 2 Hi Cp
# Tyumenebe - D426674-4 - Ni A
# Gazulistana - B41368A-B - Ic Ni
# Lan-Chonard - E324213-9 - Lo Co
# Piran - A9B7645-7 - N Fl Ni
# Peiranklin - B3405AB-7 - De Ni Po
# Geronsas - E7A3222-2 - Fl Lo
# Laguenay - C5268BB-9 -
# Cetactori - A543587-C - Ni Po
# Caniiwan - C748878-6 - S A

import pygame
import time


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


# Liste 3D contenant les infos sur les planètes du secteur Vilkian
planets_info = [
    ['Sharristan', ['E', '8', 'A', '4', '5', '9', '9', '2'], ['Fl', 'Ni']],
    ['Merchollon', ['E', '3', '0', '2', '4', '5', '7', '8'], ['Ic', 'Ni', 'Va']],
    ['Sidika', ['B', '5', '6', '6', '6', '8', '9', '9'], ['S', 'Ag', 'Ni', 'Ri']],
    ['Libitini', ['B', '5', '4', '1', '5', 'A', '6', '9'], ['Ni', 'Po']],
    ['Lyallia', ['X', '9', 'B', '8', '7', '5', '7', '3'], ['Fl']],
    ['Arthan', ['D', '2', '4', '0', '3', '3', '6', '4'], ['De', 'Lo', 'Po']],
    ['Erissen', ['B', '6', '5', '4', '8', '5', '4', '6'], []],
    ['GHANISUS', ['B', '2', '5', '0', '9', '5', '6', 'A'], ['De', 'Hi', 'Po']],
    ['JIMANN', ['D', '0', '0', '0', '9', 'A', 'D', '9'], ['As', 'Hi', 'In', 'Na']],
    ['Marilior', ['B', '6', '7', '7', '3', '2', '0', 'B'], ['S', 'Lo']],
    ['Gunnandup', ['C', '3', '4', '7', '8', '8', '4', '7'], ['S']],
    ['Intheradas', ['C', '1', '0', '0', '6', '8', '5', '8'], ['Na', 'Ni', 'Va']],
    ['MANNECA', ['B', '5', '1', '2', '9', 'B', '9', 'B'], ['Hi', 'Ic', 'In', 'Na']],
    ['Senelot', ['A', '5', '5', '1', '4', '0', '0', 'B'], ['Ni', 'Po']],
    ['Sagueneus', ['D', '7', 'A', '4', '2', '2', '2', '3'], ['Fl', 'Lo']],
    ['Karino', ['C', '2', '4', '2', '4', '3', '0', '6'], ['S', 'Ni', 'Po']],
    ['JIHLAVENKO', ['A', '8', 'D', '1', '9', 'C', 'D', 'A'], ['S', 'Fl', 'Hi']],
    ['GUERNIUM', ['B', '4', '4', '5', '9', '6', '7', 'D'], ['Hi', 'In', 'Co']],
    ['Leoncipidas', ['E', '7', 'A', '2', '4', '4', '1', '6'], ['Fl', 'Ni']],
    ['Galy Fiver', ['C', '1', '0', '0', '5', '3', '4', 'C'], ['S', 'Ni', 'Va']],
    ['McCuskenia', ['C', '4', '1', '0', '4', '5', '9', '7'], ['Ni']],
    ['Wurzburnin', ['C', '4', '4', '0', '5', '5', '0', '7'], ['De', 'Ni', 'Po']],
    ['RENALEEN', ['E', '5', '0', '0', '9', 'A', '8', '6'], ['Hi', 'In', 'Na', 'Va']],
    ['Jurburgilis', ['X', '8', '7', '9', '6', '8', '4', '0'], ['Ni']],
    ['CEPLECHT', ['C', '5', '2', '7', '9', '9', 'D', '6'], ['S', 'Hi', 'In', 'Co']],
    ['CHERALDIVIA', ['A', '2', '3', '6', '9', 'D', 'E', '9'], ['Hi']],
    ['Kulinderso', ['D', '7', '5', 'A', '6', '6', '2', '3'], ['Ni', 'Wa']],
    ['Parvillon', ['B', '8', '9', '5', '2', '0', '0', '8'], ['N', 'Lo']],
    ['Gulincelope', ['D', '6', '5', 'A', '3', '0', '0', '5'], ['Lo', 'Wa']],
    ['Vilipedi', ['C', '1', '4', '1', '3', '2', '3', 'A'], ['Lo', 'Po']],
    ['Romederblom', ['A', '5', '5', '4', '2', '0', '5', 'C'], ['Lo']],
    ['Vilk', ['B', '5', '3', '8', 'A', '7', '7', 'C'], ['2', 'Hi', 'Cp']],
    ['Tyumenebe', ['D', '4', '2', '6', '6', '7', '4', '4'], ['Ni', 'A']],
    ['Gazulistana', ['B', '4', '1', '3', '6', '8', 'A', 'B'], ['Ic', 'Ni']],
    ['Lan-Chonard', ['E', '3', '2', '4', '2', '1', '3', '9'], ['Lo', 'Co']],
    ['Piran', ['A', '9', 'B', '7', '6', '4', '5', '7'], ['N', 'Fl', 'Ni']],
    ['Peiranklin', ['B', '3', '4', '0', '5', 'A', 'B', '7'], ['De', 'Ni', 'Po']],
    ['Geronsas', ['E', '7', 'A', '3', '2', '2', '2', '2'], ['Fl', 'Lo']],
    ['Laguenay', ['C', '5', '2', '6', '8', 'B', 'B', '9'], []],
    ['Cetactori', ['A', '5', '4', '3', '5', '8', '7', 'C'], ['Ni', 'Po']],
    ['Caniiwan', ['C', '7', '4', '8', '8', '7', '8', '6'], ['S', 'A']],
]


# Fonction parcourant la liste 2D planet_info et récupérant le nom, l'UPP et les classfications.
def get_planet_info(planet_name):
    planet_name = planet_name.lower()  # Convertir en minuscules pour être insensible à la casse
    for planet in planets_info:
        if planet[0].lower() == planet_name:
            return {
                'Nom': planet[0],
                'UPP': planet[1],
                'Classifications': planet[2] if planet[2] else 'Informations non disponibles'
            }
    return None


def get_upp(planet_name):
    planet_name = planet_name.lower()  # Convertir en minuscules pour être insensible à la casse
    for planet in planets_info:
        if planet[0].lower() == planet_name:
            return planet[1]
    return None


def precision_upp(planet_upp):
    answer = input("Voulez-vous des informations supplémentaires ? Y/N").upper()
    if answer == "N":
        print("Vous semblez expérimenté !")
    elif answer == "Y":
        upp_precise = input("""Quel élément voulez-vous isoler ? (spatioport, taille, atmosphère, hydrographie, 
        population, gouvernement, légalité, niveau technologique)""")
        upp_index = {
            'spatioport': 0,
            'taille': 1,
            'atmosphère': 2,
            'hydrographie': 3,
            'population': 4,
            'gouvernement': 5,
            'légalité': 6,
            'niveau technologique': 7
        }.get(upp_precise.lower())

        if upp_index is not None and upp_index < len(planet_upp):
            print(f"La valeur de {upp_precise.capitalize()} est : {planet_upp[upp_index]}")
        else:
            print(f"Information non disponible pour {upp_precise.capitalize()}.")


def main():
    print_welcome_banner()
    pygame.init()
    play_welcome_music()

    while True:
        print("Bienvenue dans le wiki de ZEST ! ")
        print("Chargement en cours...")
        time.sleep(5)
        nom_planete = input("\nEntrez le nom de la planète (ou 'quit' pour quitter) : ")

        if nom_planete.lower() == 'quit':
            break

        try:
            info_planete = get_planet_info(nom_planete)
            if info_planete:
                print(f"\nInformations sur {info_planete['Nom']} :")
                print(f"Nom : {info_planete['Nom']}")
                print(f"UPP : {info_planete['UPP']}")
                print(f"Classifications : {info_planete['Classifications']}")
                precision_upp(info_planete['UPP'])
            else:
                raise ValueError(f"La planète {nom_planete} n'a pas été trouvée dans la base de données.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    main()
