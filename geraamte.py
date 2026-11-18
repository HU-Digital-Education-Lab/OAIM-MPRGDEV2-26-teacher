# =============================================================
#  Dit is het geraamte: de functies bestaan al, met parameters
#  en een beschrijving van invoer en uitvoer. Jullie schrijven
#  zelf de inhoud: vervang overal pass door jullie eigen code.
#
#  Afspraken:
#  - De code hoeft niet snel te zijn, maar wel volgbaar:
#    zinvolle namen en een commentaarregel bij elke
#    belangrijke stap.
#  - Gebruik NIET de ingebouwde hulp van Python om je functie
#    te schrijven: geen lijst.sort(), geen sorted(), geen
#    lijst.index(). In een test mag sorted() wel, want dan
#    gebruik je het om te controleren, niet om te bouwen.
# =============================================================

import random

# ==========================================
#  ZOEKEN: geef de positie terug, of -1
# ==========================================

def lineair_zoeken(lijst, doel):
    """Zoek het doel door de lijst één voor één af te gaan.

    invoer:  lijst, bijv. [7, 2, 9, 3, 6]
             doel,  bijv. 3
    uitvoer: de index van het eerste voorkomen van doel,
            of -1 als doel er niet in staat
    """
    # TODO: begin vooraan, vergelijk elke kaart met het doel
    pass


def binair_zoeken(lijst, doel):
    """Zoek het doel door telkens de zoekruimte te halveren.

    invoer:  lijst, al gesorteerd van klein naar groot, bijv. [2, 4, 6, 8, 10]
             doel,  bijv. 8
    uitvoer: de index van doel, of -1 als doel er niet in staat
    """
    # TODO: houd links en rechts bij, bereken midden, halveer de zoekruimte
    pass

# ==========================================
#  SORTEREN: geef de gesorteerde lijst terug
# ==========================================

def bubble_sort(lijst):
    """Sorteer door aangrenzende kaarten te vergelijken en te verwisselen.

    invoer:  lijst, bijv. [7, 2, 9, 3, 6]
    uitvoer: dezelfde waarden, van klein naar groot
    """
    # TODO: herhaal rondes, vergelijk steeds de kaart op plek index met de volgende
    pass


def insertion_sort(lijst):
    """Sorteer door de waarde op de juiste plek in het gesorteerde begin te schuiven.

    invoer:  lijst, bijv. [7, 2, 9, 3, 6]
    uitvoer: dezelfde waarden, van klein naar groot
    """
    # TODO: neem telkens één kaart op en schuif de grotere kaarten één plaats op
    pass


def selection_sort(lijst):
    """Sorteer door telkens de kleinste overgebleven kaart vooraan te leggen.

    invoer:  lijst, bijv. [7, 2, 9, 3, 6]
    uitvoer: dezelfde waarden, van klein naar groot
    """
    # TODO: zoek per plek de kleinste kaart in de rest en verwissel
    pass


# =============================================================
#  Controleer je werk: 
#  Met print controleer je met je ogen. Met assert laat je
#  Python zelf controleren: stopt het programma met een
#  AssertionError, dan wijst Python de regel aan die nog
#  niet klopt. Een geslaagde assert zegt niets, dat is normaal.
# =============================================================

print(lineair_zoeken([7, 2, 9, 3, 6], 3))      # verwacht: 3
print(lineair_zoeken([7, 2, 9, 3, 6], 5))      # verwacht: -1
print(lineair_zoeken([], 5))                  # verwacht: -1
print(lineair_zoeken([5, 2, 5, 1], 5))        # verwacht: 0  (eerste voorkomen)

print(binair_zoeken([2, 4, 6, 8, 10], 8))     # verwacht: 3
print(binair_zoeken([2, 4, 6, 8, 10], 5))     # verwacht: -1
print(binair_zoeken([], 5))                  # verwacht: -1

assert lineair_zoeken([7, 2, 9, 3, 6], 3) == 3, "3 staat op plek 3"
assert lineair_zoeken([7, 2, 9, 3, 6], 5) == -1, "5 zit er niet, dus -1"
assert lineair_zoeken([], 5) == -1, "lege lijst: dus -1"
assert binair_zoeken([2, 4, 6, 8, 10], 8) == 3
assert binair_zoeken([2, 4, 6, 8, 10], 5) == -1


# =============================================================
#  Controleer je werk: 
#  Deze regels staan nog uit (met een hekje ervoor), zodat het
#  bestand ook startbaar blijft terwijl de sorteerfuncties
#  nog niet af zijn. Verwijder het hekje (#) vóór een regel
#  zodra de functie waar die regel over gaat af is.
#  De regels van insertion_sort of selection_sort die jullie
#  tweetal niet hoeven te doen, mag je gewoon laten staan.
# =============================================================

# print(bubble_sort([7, 2, 9, 3, 6]))           # verwacht: [2, 3, 6, 7, 9]
# print(insertion_sort([7, 2, 9, 3, 6]))        # verwacht: [2, 3, 6, 7, 9]
# print(selection_sort([7, 2, 9, 3, 6]))       # verwacht: [2, 3, 6, 7, 9]
# print(bubble_sort([5, 2, 5, 1]))             # verwacht: [1, 2, 5, 5]
# print(bubble_sort([]))                       # verwacht: []

# assert bubble_sort([5, 2, 5, 1]) == [1, 2, 5, 5]
# assert bubble_sort([]) == []
# assert insertion_sort([7, 2, 9, 3, 6]) == [2, 3, 6, 7, 9]
# assert selection_sort([7, 2, 9, 3, 6]) == [2, 3, 6, 7, 9]

# Extra controle met een geschudde proefrij:
# random.shuffle verandert de lijst ter plekke en geeft niets
# terug. Schrijf dus NIET: proefrij = random.shuffle(proefrij),
# want dan staat er None in proefrij.
# proefrij = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(proefrij)
# print(proefrij)                              # telkens een andere volgorde
# assert bubble_sort(proefrij) == sorted(proefrij), "gesorteerde proefrij klopt niet"

# Deze zin zie je alleen als alle asserts die op dat moment
# actief zijn geslaagd zijn:
print("Alle asserts geslaagd!")
