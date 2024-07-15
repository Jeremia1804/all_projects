nombre = 10000.20
nombre_formate = "{:,}".format(nombre)
print(nombre_formate)

nombre = 1000.050
# Utilisation de l'espace comme séparateur
nombre_formate_avec_espace = "{:,.0f}".format(nombre).replace(',', ' ')
# Utilisation du point comme séparateur
nombre_formate_avec_point = "{:,.0f}".format(nombre).replace(',', '.')
print(nombre_formate_avec_espace)  # Affiche : 1 000 000
print(nombre_formate_avec_point)   # Affiche : 1.000.000
 # Affiche : 1,000,000

nombre_decimal = 1234567.89
# Utilisation de la virgule comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_virgule = "{:,.2f}".format(nombre_decimal).replace(',', ' ')
# Utilisation du point comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_point = "{:,.2f}".format(nombre_decimal).replace(',', '.')
print(nombre_formate_virgule)  # Affiche : 1 234 567,89
print(nombre_formate_point)    # Affiche : 1.234.567,89


nombre_decimal = 1234567.89
# Utilisation de la virgule comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_virgule = f"{nombre_decimal:,.2f}".replace(',', ' ')
nombre_arrondi = round(nombre_decimal, 2)
# Utilisation du point comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_point = f"{nombre_decimal:,.2f}".replace(',', '.')
print(nombre_formate_virgule)  # Affiche : 1 234 567,89
print(nombre_formate_point)    # Affiche : 1.234.567,89

nombre_decimal = 1234567.895
# Arrondir le nombre à deux décimales avant le formatage
nombre_arrondi = round(nombre_decimal, 2)
# Utilisation de la virgule comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_virgule = "{:,.2f}".format(nombre_arrondi).replace(',', ' ')
# Utilisation du point comme séparateur et affichage de deux chiffres après la virgule
nombre_formate_point = "{:,.2f}".format(nombre_arrondi).replace(',', '.')
print(nombre_formate_virgule)  # Affiche : 1 234 567,90
print(nombre_formate_point)    # Affiche : 1.234.567,90

from datetime import datetime
import locale

# Définir la localisation en français
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

# Date à formater
date = datetime(2024, 5, 13)

# Formater la date en "Jeudi 13 Mai 2024"
date_formatee = date.strftime("%A %d %B %Y")
print(date_formatee)  # Affiche : Jeudi 13 Mai 2024

import re

def valider_numero_telephone(numero):
    # Expression régulière pour vérifier le format du numéro de téléphone
    pattern = r'^(\+\d{1,3})?(\d{9,15})$'

    # Vérifier si le numéro correspond au pattern
    if re.match(pattern, numero):
        return True
    else:
        return False

# Exemples de numéros de téléphone
numeros = ['+261341204035', '+123456789', '+123456789012345']

# Tester les numéros de téléphone
for numero in numeros:
    if valider_numero_telephone(numero):
        print(f"Le numéro {numero} est valide.")
    else:
        print(f"Le numéro {numero} n'est pas valide.")