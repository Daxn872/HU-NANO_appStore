import os

SCORE_FILE = os.path.join(os.path.dirname(__file__), '../data/scores.txt')

def voeg_score_toe(naam, spel, resultaat):
    # Sla de score op in een bestand
    with open(SCORE_FILE, 'a') as file:
        file.write(f"{naam}, {spel}, {resultaat}\n")

def toon_scores():
    # Toon alle scores
    if not os.path.exists(SCORE_FILE):
        print("Nog geen scores beschikbaar.")
        return

    print("\nScores:")
    with open(SCORE_FILE, 'r') as file:
        for regel in file:
            print(regel.strip())
