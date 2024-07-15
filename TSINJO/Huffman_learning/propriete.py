def longueur_moyenne(language):
    taille = len(language)
    somme = 0
    for el in language:
        somme += len(el)
    return somme/taille

def about_1_0(language):
    taille = len(language)
    taille_total = 0
    nb_0 = 0
    nb_1 = 0
    for el in language:
        taille_total += len(el)
        nb_0 += el.count('0')
        nb_1 += el.count('1')
    moyenne_nb_0 = nb_0/taille
    moyenne_nb_1 = nb_1/taille
    p_nb_0 = nb_0/taille_total
    p_nb_1 = nb_1/taille_total

    return moyenne_nb_0,moyenne_nb_1,p_nb_0,p_nb_1


def language_to_matrix(language):
    lgm = longueur_moyenne(language)
    moyenne_nb_0,moyenne_nb_1,p_nb_0,p_nb_1 = about_1_0(language)
    nb_mot = len(language)
    return [nb_mot,lgm,moyenne_nb_0,moyenne_nb_1,p_nb_0,p_nb_1]

def language_to_matrix2(language,all_binary_words):
    matr = language_to_matrix(language)
    for words in all_binary_words:
        if words in language:
            matr.append(1)
        else:
            matr.append(0)
    return matr