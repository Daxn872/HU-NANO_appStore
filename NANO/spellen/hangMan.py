import random
from spellen.score import voeg_score_toe

def kies_woord(moeilijkheid):
    woorden = {
        'makkelijk': ['stick', 'bal', 'veld', 'goal', 'keeper'],
        'gemiddeld': ['corner', 'scoopen', 'schuifslag', 'doelpunt'],
        'moeilijk': ['scooptechniek', 'schijnbeweging', 'uitverdedigen'],
    }
    return random.choice(woorden[moeilijkheid])

def main():
    naam = input("Voer je naam in: ")
    moeilijkheid = input("Kies een moeilijkheidsgraad: makkelijk, gemiddeld of moeilijk: ").lower()

    if moeilijkheid not in ['makkelijk', 'gemiddeld', 'moeilijk']:
        print("Ongeldige moeilijkheidsgraad. Kies uit makkelijk, gemiddeld of moeilijk.")
        return

    woord = kies_woord(moeilijkheid)
    geraden_woord = ['_' for _ in woord]
    aantal_pogingen = len(woord) + 3

    gebruikte_letters = set()

    while aantal_pogingen > 0:
        print("\nHuidige status van het woord:", " ".join(geraden_woord))
        print("Gebruikte letters:", " ".join(gebruikte_letters))
        print(f"Aantal resterende pogingen: {aantal_pogingen}")

        gok = input("Raad een letter: ").lower()

        if len(gok) != 1 or not gok.isalpha():
            print("Voer een enkele letter in.")
            continue

        if gok in gebruikte_letters:
            print("Je hebt deze letter al geprobeerd.")
            continue

        gebruikte_letters.add(gok)

        if gok in woord:
            for i, letter in enumerate(woord):
                if letter == gok:
                    geraden_woord[i] = gok
            if "_" not in geraden_woord:
                print("Gefeliciteerd! Je hebt het woord geraden en een doelpunt gescoord!")
                voeg_score_toe(naam, "Hockey Galgje", "Gewonnen")
                break
        else:
            aantal_pogingen -= 1
            print(f"Fout! De letter '{gok}' zit niet in het woord. Balverlies!")

        if aantal_pogingen <= 0:
            print(f"Helaas, je hebt geen pogingen meer. Het juiste woord was: {woord}.")
            voeg_score_toe(naam, "Hockey Galgje", "Verloren")
            break

if __name__ == "__main__":
    main()
