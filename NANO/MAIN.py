import os
import sys
from spellen import guessTheNumber, hangMan
from spellen.score import toon_scores

def main_menu():
    while True:
        print("\nWelkom bij HockeyHub!")
        print("Het digitale platform voor hockeyliefhebbers en gamers.")
        print("1. Raad het nummer - Hockey editie")
        print("2. Hockey Galgje")
        print("3. Bekijk scores")
        print("4. Afsluiten")

        keuze = input("Kies een optie (1-4): ")

        if keuze == '1':
            guessTheNumber.raad_het_nummer()  # Aanroepen van de juiste functie
        elif keuze == '2':
            hangMan.main()  # Aanroepen van de juiste functie
        elif keuze == '3':
            toon_scores()
        elif keuze == '4':
            print("Bedankt voor het spelen bij HockeyHub! Tot ziens.")
            sys.exit()
        else:
            print("Ongeldige keuze. Kies een optie tussen 1 en 4.")

if __name__ == "__main__":
    main_menu()
