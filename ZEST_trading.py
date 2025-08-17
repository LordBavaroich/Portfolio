import random
import pygame
import time


def print_welcome_banner():
    print("""
    ███████╗███████╗███████╗████████╗███████╗██╗  ██╗███████╗
    ╚══███╔╝██╔════╝██╔════╝╚══██╔══╝██╔════╝╚██╗██╔╝██╔════╝
      ███╔╝ █████╗  ███████╗   ██║   █████╗   ╚███╔╝ █████╗  
     ███╔╝  ██╔══╝  ╚════██║   ██║   ██╔══╝   ██╔██╗ ██╔══╝  
    ███████╗███████╗███████║   ██║██╗███████╗██╔╝ ██╗███████╗
    ╚══════╝╚══════╝╚══════╝   ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
    """)


def play_welcome_music():
    pygame.mixer.init()
    pygame.mixer.music.load(
        "music/Alien Soundtrack Track 1 ”Main Title Jerry Goldsmith.mp3")  # Remplacez par le chemin de votre fichier
    # audio
    pygame.mixer.music.play(-1)  # -1 pour jouer en boucle


def get_trade_codes():
    trade_codes = []
    while True:
        code = input("Quels sont les codes commerciaux de la planète? (Entrez 'n' pour arrêter)")
        if code.lower() == "n":
            break
        trade_codes.append(code)
    return trade_codes


def dm_pop(pop):
    if pop <= 3:
        return -3
    elif pop >= 9:
        return 3
    else:
        return 0


def check_trade_classification(item, planet_trade_codes):
    item_classification = item["Availability"]
    for code in item_classification:
        if code == "All" or code in planet_trade_codes:
            return True
    return False


def roll_d66():
    return random.randint(1, 6) * 10 + random.randint(1, 6)


def generate_random_trade_good(trade_goods_list):
    while True:
        result = roll_d66()
        index = result - 11
        if 0 <= index < len(trade_goods_list):
            return trade_goods_list[index]


def generate_trade_goods(population, planet_trade_codes):
    trade_goods_list = [
        {"D66": 11, "Type": "Common Electronics", "Availability": "All", "Tons": "2D x 10", "Base Price": "Cr10000",
         "Purchase DM": "Agricultural +3, Garden +2",
         "Sale DM": "Agricultural +3, Water World +2, Garden +1, Asteroid -4"},
        {"D66": 12, "Type": "Common Industrial Goods", "Availability": "All", "Tons": "2D x 10",
         "Base Price": "Cr20000",
         "Purchase DM": "Asteroid +4", "Sale DM": "Industrial +2, Poor +2"},
        {"D66": 13, "Type": "Common Manufactured Goods", "Availability": "All", "Tons": "2D x 20",
         "Base Price": "Cr5000",
         "Purchase DM": "Non-Industrial +2, Low Tech +1, Poor +1", "Sale DM": "Non-Industrial +3, Agricultural +2"},
        {"D66": 14, "Type": "Common Raw Materials", "Availability": "All", "Tons": "2D x 20", "Base Price": "Cr500",
         "Purchase DM": "Non-Industrial +3, High Population +2",
         "Sale DM": "Asteroid +1, Fluid Oceans +1, Ice-Capped +1"},
        {"D66": 15, "Type": "Common Consumables", "Availability": "All", "Tons": "2D x 10", "Base Price": "Cr20000",
         "Purchase DM": "Industrial +3, Non-Ore bearing common metals +1", "Sale DM": "Industrial +1"},
        {"D66": 16, "Type": "Common Ore", "Availability": "All", "Tons": "2D x 20", "Base Price": "Cr10000",
         "Purchase DM": "Asteroid +2, Non-Industrial +1", "Sale DM": "High Population +1, Rich +2"},
        {"D66": 21, "Type": "Advanced Electronics", "Availability": "Industrial, High Tech", "Tons": "1D x 5",
         "Base Price": "Cr100000", "Purchase DM": "Industrial +2, High Tech +3",
         "Sale DM": "Industrial +2, High Tech +1"},
        {"D66": 22, "Type": "Advanced Machine Parts", "Availability": "Industrial, High Tech", "Tons": "1D x 5",
         "Base Price": "Cr75000", "Purchase DM": "Industrial +2, High Tech +1", "Sale DM": "Industrial +1"},
        {"D66": 23, "Type": "Advanced Manufactured Goods", "Availability": "Industrial, High Tech", "Tons": "1D x 5",
         "Base Price": "Cr100000", "Purchase DM": "Industrial +1", "Sale DM": "High Tech +2"},
        {"D66": 24, "Type": "Advanced Weapons", "Availability": "Industrial, High Tech", "Tons": "1D x 5",
         "Base Price": "Cr150000", "Purchase DM": "High Tech +2", "Sale DM": "Poor +1, Amber Zone +2, Red Zone +4"},
        {"D66": 25, "Type": "Advanced Vehicles", "Availability": "Industrial, High Tech", "Tons": "1D x 5",
         "Base Price": "Cr180000", "Purchase DM": "High Tech +2", "Sale DM": "Asteroid +2, Rich +2"},
        {"D66": 26, "Type": "Biofuels", "Availability": "High-Tech", "Tons": "1D x 5", "Base Price": "Cr50000",
         "Purchase DM": "Industrial +2", "Sale DM": "Agricultural +1, Water World +2"},
        {"D66": 31, "Type": "Crystals & Gems", "Availability": "High-Tech", "Tons": "1DCr250000", "Base Price": "Cr1",
         "Purchase DM": "Asteroid +2, Low Population +2", "Sale DM": "Industrial +1"},
        {"D66": 32, "Type": "Cybernetics", "Availability": "High-Tech", "Tons": "1D x 10", "Base Price": "Cr10000",
         "Purchase DM": "Rich +6, High Population +1", "Sale DM": "Rich +4"},
        {"D66": 33, "Type": "Live Animals", "Availability": "Agricultural +2", "Tons": "1D x 10",
         "Base Price": "Cr10000",
         "Purchase DM": "High Population +3", "Sale DM": "Low Population +3"},
        {"D66": 34, "Type": "Luxury Consumables", "Availability": "Agricultural +2, Water World +1", "Tons": "1D x 10",
         "Base Price": "Cr20000", "Purchase DM": "Rich +2", "Sale DM": "High Population +2"},
        {"D66": 35, "Type": "Luxury Goods", "Availability": "Agricultural, Garden", "Tons": "1DCr200000",
         "Base Price": "Cr1", "Purchase DM": "High Population +1", "Sale DM": "Rich +4"},
        {"D66": 36, "Type": "Medical Supplies", "Availability": "High-Tech", "Tons": "1D x 5", "Base Price": "Cr50000",
         "Purchase DM": "Industrial +2, Poor +1, Rich +1", "Sale DM": "High Tech +2, Industrial +3"},
        {"D66": 41, "Type": "Petrochemicals", "Availability": "Industrial", "Tons": "1D x 5", "Base Price": "Cr150000",
         "Purchase DM": "High Tech +2", "Sale DM": "Poor +6, Amber Zone +2, Red Zone +6"},
        {"D66": 42, "Type": "Pharmaceuticals", "Availability": "High-Tech", "Tons": "1D x 5", "Base Price": "Cr180000",
         "Purchase DM": "High Tech +2", "Sale DM": "Asteroid +2, Rich +2"},
        {"D66": 43, "Type": "Polymers", "Availability": "Industrial", "Tons": "1D x 5", "Base Price": "Cr50000",
         "Purchase DM": "Industrial +2", "Sale DM": "Agricultural +1, Water World +2"},
        {"D66": 44, "Type": "Precious Metals", "Availability": "Asteroid +1", "Tons": "1D x 20", "Base Price": "Cr1000",
         "Purchase DM": "Agricultural +6", "Sale DM": "Rich +2, Industrial +1"},
        {"D66": 45, "Type": "Radioactives", "Availability": "Industrial", "Tons": "1D x 10", "Base Price": "Cr15000",
         "Purchase DM": "High Tech +1", "Sale DM": "Desert +2"},
        {"D66": 46, "Type": "Robots", "Availability": "Industrial, High Tech", "Tons": "1D x 5",
         "Base Price": "Cr250000",
         "Purchase DM": "High Tech +1", "Sale DM": "Desert, Fluid Oceans, Ice-Capped, Water World +1"},
        {"D66": 51, "Type": "Spices", "Availability": "Asteroid +1", "Tons": "1D x 20", "Base Price": "Cr3000",
         "Purchase DM": "Agricultural +7", "Sale DM": "Asteroid +4"},
        {"D66": 52, "Type": "Textiles", "Availability": "Agricultural", "Tons": "1D x 20", "Base Price": "Cr5000",
         "Purchase DM": "Asteroid +4", "Sale DM": "Agricultural +1"},
        {"D66": 53, "Type": "Uncommon Ore", "Availability": "Asteroid +4", "Tons": "1D x 10", "Base Price": "Cr20000",
         "Purchase DM": "Agricultural +2, Water World +1", "Sale DM": "Industrial +3, High Tech +1"},
        {"D66": 54, "Type": "Uncommon Raw Materials", "Availability": "Agricultural -3", "Tons": "1D x 20",
         "Base Price": "Cr5000", "Purchase DM": "Agricultural +2, High Tech +1",
         "Sale DM": "Agricultural -2, Industrial +1"},
        {"D66": 55, "Type": "Wood", "Availability": "Agricultural +2, High Population +1", "Tons": "1D x 20",
         "Base Price": "Cr3000", "Purchase DM": "Desert +2", "Sale DM": "High Population +1"},
        {"D66": 56, "Type": "Vehicles", "Availability": "Industrial", "Tons": "1D x 10", "Base Price": "Cr6000",
         "Purchase DM": "Desert +2", "Sale DM": "Agricultural +2"},
        {"D66": 61, "Type": "Illegal Biochemicals", "Availability": "High Tech", "Tons": "1D x 20",
         "Base Price": "Cr3000",
         "Purchase DM": "Desert +2", "Sale DM": "Rich +6, High Population +1"},
        {"D66": 62, "Type": "Illegal Cybernetics", "Availability": "High Tech", "Tons": "1D", "Base Price": "Cr400000",
         "Purchase DM": "Asteroid +1, Low Population +2", "Sale DM": "Industrial +1"},
        {"D66": 63, "Type": "Illegal Drugs", "Availability": "Industrial", "Tons": "1D x 5", "Base Price": "Cr100000",
         "Purchase DM": "Garden, Desert, Water World +1", "Sale DM": "Asteroid +2, Desert +1, Ice-Capped +1"},
        {"D66": 64, "Type": "Illegal Luxuries", "Availability": "Asteroid +1", "Tons": "1D x 10",
         "Base Price": "Cr50000",
         "Purchase DM": "Agricultural +2, Water World +1", "Sale DM": "Rich +6, High Population +1"},
        {"D66": 65, "Type": "Illegal Weapons", "Availability": "Asteroid, Desert, High Pop, Water World",
         "Tons": "1D x 5",
         "Base Price": "Cr20000", "Purchase DM": "Desert +2, High Pop +1", "Sale DM": "Rich +4"},
        {"D66": 66, "Type": "Exotics", "Availability": "Industrial", "Tons": "1D x 10", "Base Price": "Cr150000",
         "Purchase DM": "High Tech +2", "Sale DM": "Poor +6, Amber Zone +2, Red Zone +6"}
    ]

    available_goods = []

    # Ajout des biens correspondant aux codes commerciaux de la planète
    for item in trade_goods_list:
        if item["Type"] == "Exotics" or check_trade_classification(item, planet_trade_codes):
            # Récupérer le prix correct en fonction de la position
            price = item["Base Price"]  # Utilisez le prix de base pour les biens autres qu'"Exotics"
            available_goods.append(
                {"Type": item["Type"], "Quantity": (random.randint(1, 6) + dm_pop(population)) * 10, "Price": price})

        # Ajout du nombre de trade goods générés aléatoirement égal au code de population
    for _ in range(population):
        random_trade_good = generate_random_trade_good(available_goods)  # Utilisez available_goods ici
        # Vérification pour les biens "Exotics"
        if random_trade_good["Type"] == "Exotics":
            price = "Special Price"  # Définir un prix spécial pour les biens "Exotics"
        else:
            # Récupérer le prix correct en fonction de la position
            price = random_trade_good["Base Price"]  # Utilisez le prix de base pour les autres biens
        available_goods.append(
            {"Type": random_trade_good["Type"], "Quantity": (random.randint(1, 6) + dm_pop(population)) * 10,
             "Price": price})

    return available_goods


# Programme principal

print_welcome_banner()
pygame.init()
play_welcome_music()
print("Bienvenue dans ZEST_TRADING, votre gestionnaire et assistant commercial préféré !")
print("Chargement de ZEST_TRADING...")
time.sleep(5)
print("Vous devrez rentrer quelques informations manuellement pour aider ZEST.")

population = int(input("Quelle est la population PUM du monde? "))
trade_codes_lst = get_trade_codes()

available_trade_goods = generate_trade_goods(population, trade_codes_lst)

print("Biens disponibles pour cette planète:")
for item in available_trade_goods:
    print(f"{item['Type']} - Quantité: {item['Quantity']}, Prix: {item['Price']}")
