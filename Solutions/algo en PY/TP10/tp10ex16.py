def filtrer_par_lettre(liste_de_chaines, lettre):
    resultats = []

    for chaine in liste_de_chaines:
        if lettre in chaine:
            resultats.append(chaine)
    return resultats

liste_originale = ["hamid", "mohamed", "rachid", "kotoubia", "casablanca"]
lettre_specifiee = "c"
resultats_filtres = filtrer_par_lettre(liste_originale, lettre_specifiee)

print(f"Liste originale : {liste_originale}")
print(f"Résultats filtrés pour la lettre '{lettre_specifiee}' : {resultats_filtres}")
