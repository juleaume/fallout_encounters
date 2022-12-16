import time
import urandom
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_INKY_PACK

display = PicoGraphics(display=DISPLAY_INKY_PACK)
WIDTH, HEIGHT = display.get_bounds()
# you can change the update speed here!
# it goes from 0 (slowest) to 3 (fastest)
display.set_update_speed(1)

display.set_font("bitmap8")

button_a = Button(12)
button_b = Button(13)
button_c = Button(14)

LOGO_COLOR = 12


# a handy function we can call to clear the screen
# display.set_pen(15) is white and display.set_pen(0) is black
def clear():
    display.set_pen(15)
    display.clear()
    display.set_pen(LOGO_COLOR)
    display.circle(WIDTH // 2, HEIGHT // 2, 50)
    display.rectangle(30, HEIGHT // 2 - 5, WIDTH - 60, 10)
    display.triangle(
        30, HEIGHT // 2 - 5, 30, HEIGHT // 2 + 5, 15, HEIGHT // 2
    )
    display.triangle(
        WIDTH - 31, HEIGHT // 2 - 5,
        WIDTH - 31, HEIGHT // 2 + 5,
        WIDTH - 16, HEIGHT // 2
    )
    display.rectangle(50, HEIGHT // 3 - 10, WIDTH - 100, 10)
    display.triangle(
        50, HEIGHT // 3 - 10,
        50, HEIGHT // 3,
        35, HEIGHT // 3 - 5
    )
    display.triangle(
        WIDTH - 51, HEIGHT // 3 - 10,
        WIDTH - 51, HEIGHT // 3,
        WIDTH - 36, HEIGHT // 3 - 5
    )
    display.rectangle(50, 2 * HEIGHT // 3, WIDTH - 100, 10)
    display.triangle(
        50, 2 * HEIGHT // 3,
        50, 2 * HEIGHT // 3 + 10,
        35, 2 * HEIGHT // 3 + 5
    )
    display.triangle(
        WIDTH - 51, 2 * HEIGHT // 3,
        WIDTH - 51, 2 * HEIGHT // 3 + 10,
        WIDTH - 36, 2 * HEIGHT // 3 + 5
    )
    display.set_pen(15)
    display.circle(WIDTH // 2, HEIGHT // 2, 40)
    display.set_pen(LOGO_COLOR)
    display.circle(WIDTH // 2, HEIGHT // 2, 20)
    display.set_pen(0)


# set up
clear()
display.set_pen(0)
display.text("[A] Rencontres sociales", 10, 10, WIDTH, 2)
display.text("[B] Rencontres géographiques", 10, 50, WIDTH, 2)
display.text("[C] Temps et Météo", 10, 90, WIDTH, 2)
display.update()
time.sleep(0.5)


def d20():
    return urandom.randint(1, 20)


def get_social_encounter():
    return urandom.choice(
        [
            "Des pillards se sont emparés d'un hameau aux cabanes délabrées "
            "et exigent que les voyageurs se plient à leurs demandes.",
            "Un marchand itinérant tente d'échapper à une nuée de mouches "
            "bouffies. Si les personnages lui viennent en aide, ils auront "
            "droit à une réduction ou une récompense.",
            "Un eyebot errant passe dans le coin, il diffuse des publicités "
            "et éventuellement des informations sur une mission potentielle.",
            "Une meute de chiens affamés attaque les habitants des Terres "
            "Désolées pour calmer sa faim.",
            "Un yao guai enragé tend une ambuscade au groupe qui s'est "
            "aventuré sur son territoire.",
            "Une meute de goules sauvages repère les personnages et fonce "
            "droit sur leur position, un luminecent positionné au centre du "
            "groupe.",
            "Un vertiptère de l'Ordre survole le groupe et lui lance un "
            "appel. La teneur du message dépend de la réputation des "
            "aventuriers auprès de la faction concernée.",
            "Un béhémoth super mutant défend le lieu où se trouve "
            "actuellement le groupe.",
            "Une reine des fangeux, épaulée par sa progéniture, protège le "
            "point d'eau qui abrite ses oeufs.",
            "Un écorcheur se tient, triomphant, sur l'un de ses congénères "
            "qu'il vient juste de tuer.",
            "Un groupe de Mister Gutsy en plein exercice d'entrainement "
            "cherche à convaincre le groupe de jouer le role de soldats "
            "alliés ou ennemis.",
            "Des fidèles de la secte des Pilliers de la commaunuté désirent "
            "convertir le groupe.",
            "Des fans d'icones de la culture d'avant-guerre se sont réunis "
            "pour organiser une convention réunissant les groupes intéressés "
            "qui habitent les Terres Désolées.",
            "Des super mutants examinent un appareil technologique avancé "
            "pour le faire fonctionner (par ex. un avion, un robot ou un "
            "tank).",
            "Des colons tirant des pousse-pousse de fortune se rapprochent "
            "du groupe et proposent leurs service en échange de jetons de "
            "métro.",
            "L'habitant d'un abri dont vous n'avez jamais entendu parler "
            "vous aborde et demande des pièces qui aideront à maintenir en "
            "état l'infrastructure de son refuge.",
            "Des coups de feux se font entendre au loin.",
            "Un vertiptère passe au loin et finit sa course au sol. Une "
            "explosion se fait entendre et un nuage de fumée s'élève.",
            "Deux personnages sont surpris, un tient une arme, l'autre est "
            "dans un trou en train de creuser.",
            "Une colonie se fait piller régulièrement et prépare un plan "
            "pour se venger.",
            "Un personnage semble chercher son ou sa compagne qui a disparu.",
            "Des super mutants et des humains travaillent ensemble pour "
            "résoudre un problème commun, il leur manque un point de vue.",
            "L'Ordre est en mission de reconnaissance, l'Evèque et ses "
            "clercs demandent aux personnages de s'écarter",
            "UNE MINE !?",
            "Des animaux ont disparus dans une ferme, les colons accusent "
            "une goule qui habite non loin.",
            "Les personnages captent une radio qu'ils ne connaissent pas.",
            "Des habitants des Terres Désolées fuient un groupe de colons "
            "qui les poursuit, arme en main.",
            "Un cerobron est à la recherche de pièces de rechange et est "
            "pret à payer cher pour en récupérer",

        ]
    )


def get_urban():
    return urandom.choice(
        [
            "Boulevard", "Catacombes", "Fontaines", "Immeuble de bureaux",
            "Métro", "Librairie", "Parc", "Piscine", "Place", "Quai",
            "Théatre",
        ]
    )


def get_rural():
    return urandom.choice(
        [
            "Bunker", "Centrale éléctrique", "Décharge", "Ferme", "Grotte",
            "Lotissement", "Station satellite", "Usine",
        ]
    )


def get_location():
    return urandom.choice(
        [
            f"Abri FR-{urandom.randint(2, 999):03}", "Avant poste de l'Ordre",
            "Base de l'armée", "Boulangerie", "Café", "Camp de pillards",
            "Colonie", "Eglise", "Egouts", "Epave d'aéronefs", "Gare",
            "Hopital", "Magasin spécialisé", "Musée", "Poste de police",
            "Quai", "Red rocket", "Restaurant", "Ruines", "Tour de radio"
        ]
    )


def get_weather():
    hour = urandom.randint(0, 23)
    minutes = urandom.randint(0, 59)
    current_time = f"{hour:02}h{minutes:02}"
    d = d20()
    if 1 <= d <= 6:
        weather = "Beau temps"
        hot = 9 <= hour <= 18
    elif 7 <= d <= 12:
        weather = "Couvert"
        hot = False
    elif 13 <= d <= 16:
        weather = "Pluie"
        hot = False
    elif 17 <= d <= 18:
        weather = "Brumeux"
        hot = False
    elif 19 <= d <= 20:
        weather = "Orage"
        hot = 9 <= hour <= 18
    else:
        weather = "Apocalypse Nucléaire"
        hot = True
    d = d20()
    if 1 <= d <= 6:
        temp = urandom.randint(20, 25) if hot else urandom.randint(15, 20)
    elif 7 <= d <= 12:
        temp = urandom.choice(
            [urandom.randint(15, 20), urandom.randint(25, 30)]
        ) if hot else urandom.randint(10, 20)
    elif 13 <= d <= 16:
        temp = urandom.choice(
            [urandom.randint(10, 15), urandom.randint(30, 35)]
        ) if hot else urandom.randint(5, 15)
    elif 17 <= d <= 18:
        temp = urandom.choice(
            [urandom.randint(5, 10), urandom.randint(35, 40)]
        ) if hot else urandom.randint(0, 10)
    elif 19 <= d <= 20:
        temp = urandom.choice(
            [urandom.randint(-5, 5), urandom.randint(40, 45)]
        ) if hot else urandom.randint(-10, 5)
    else:
        temp = 100
    return f"{current_time} {weather} > {temp:2} °C"


def on_button_a():
    """
    get social encounters
    :return:
    """
    clear()
    display.text(
        f"0x{urandom.randint(0, 0xffff):04X} {get_social_encounter()}",
        0, 5, WIDTH - 10, 2
    )
    display.update()
    time.sleep(0.5)


def on_button_b():
    """
    get geographical encounter
    :return:
    """
    clear()
    locations = [get_urban(), get_rural()]
    for _ in range(4):
        _l = get_location()
        while _l in locations:
            _l = get_location()
        locations.append(_l)
    _b = urandom.randint(0, 0xffff)
    for i, _l in enumerate(locations):
        display.text(
            f"0x{_b + i:04X} {_l}",
            0, 5 + i * 20, WIDTH - 10, 2
        )
    display.update()
    time.sleep(0.5)


def on_button_c():
    """
    get the weather
    :return:
    """
    clear()
    display.text(
        f"Connexion Satellite... OK! ",
        0, 0, WIDTH - 10, 2
    )
    display.text("Bulletin météo Vault-Tec :", 0, 20, WIDTH - 10, 2)
    display.text(get_weather(), 0, 50, WIDTH - 10, 4)
    display.update()
    time.sleep(0.5)


while True:
    if button_a.read():  # if a button press is detected then...
        on_button_a()
    elif button_b.read():
        on_button_b()
    elif button_c.read():
        on_button_c()
    time.sleep(0.1)
