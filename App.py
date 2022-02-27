# print("premier affichage \n choisir une action :")
# action = input()
#
# while(action != "0"):
#     print(f"affichage dépendant de l'action {action}")
#     action = input()

#import RestoManager
import Scraping

resto='bichette'

res = Scraping.get_resto_avis(resto)

print(res)