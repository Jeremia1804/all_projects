import pickle
import itertools

def generate_all_binary_words(min_length, max_length):
    all_words = []
    for length in range(min_length, max_length + 1):
        all_words.extend([''.join(bits) for bits in itertools.product('01', repeat=length)])
    return all_words

def lireFichier():
        with open("data/modele.pkl", "rb") as fichier:
            contenu_fichier = fichier.read()
        return pickle.loads(contenu_fichier)

def ecrireFichier(clf):
        variable_serializee = pickle.dumps(clf)
        with open("data/modele.pkl", "wb") as fichier:
            fichier.write(variable_serializee)

clf = lireFichier()
all_binary_words = generate_all_binary_words(1, 7)