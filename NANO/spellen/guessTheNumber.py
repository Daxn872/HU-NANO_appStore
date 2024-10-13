import random
from spellen.score import voeg_score_toe

def raad_het_nummer():
    # Introductie
    print("Welkom bij 'Raad het nummer - Hockey editie'!")
    print("De computer kiest een willekeurig getal. Kan jij een doelpunt scoren door het juiste nummer te raden?")

    naam = input("Voer je naam in: ")
    try:
        max_getal = int(input("Wat is het hoogste getal waaruit de computer mag kiezen? "))
        aantal_pogingen = int(input("Hoe vaak mag je schieten? "))
    except ValueError:
        print("Voer een geldig getal in.")
        return

    # Willekeurig getal genereren
    geheim_getal = random.randint(1, max_getal)

    # For-loop om de gebruiker te laten raden
    for poging in range(1, aantal_pogingen + 1):
        try:
            gok = int(input(f"Poging {poging}: Raad het getal: "))
        except ValueError:
            print("Voer een geldig getal in.")
            continue

        if gok == geheim_getal:
            print(f"Gefeliciteerd! Je hebt het juiste getal {geheim_getal} geraden en een doelpunt gescoord!")
            voeg_score_toe(naam, "Raad het nummer - Hockey editie", "Gewonnen")
            break
        elif gok < geheim_getal:
            print("Het getal is hoger. Probeer opnieuw te scoren!")
        else:
            print("Het getal is lager. Blijf aanvallen!")
        
        # Als dit de laatste poging is en het getal niet geraden is
        if poging == aantal_pogingen:
            print(f"Helaas, je hebt geen pogingen meer. Het juiste getal was {geheim_getal}.")
            voeg_score_toe(naam, "Raad het nummer - Hockey editie", "Verloren")

def main():
    raad_het_nummer()

if __name__ == "__main__":
    main()
