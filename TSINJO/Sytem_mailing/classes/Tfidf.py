import math
from collections import Counter

def preprocess_text(text):
    # Mettre en minuscule et enlever la ponctuation
    text = text.lower()
    text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace("\r",'')
    return text

def compute_tf(text):
    # Calcul de la fréquence du terme (Term Frequency, TF)
    word_counts = Counter(text.split())
    total_words = len(text.split())
    tf_scores = {word: count/total_words for word, count in word_counts.items()}
    return tf_scores

def compute_idf(documents):
    # Calcul de la fréquence inverse du document (Inverse Document Frequency, IDF)
    N = len(documents)
    idf_scores = {}
    all_words = set([word for doc in documents for word in doc.split()])
    
    for word in all_words:
        doc_count = sum([1 for doc in documents if word in doc])
        idf_scores[word] = math.log(N / (doc_count + 1))
    return idf_scores

def compute_tfidf(tf_scores, idf_scores, all_words):
    # Calcul du score TF-IDF pour tous les mots existants dans tous les documents
    tfidf_scores = [tf_scores[word] * idf_scores[word] if word in tf_scores else 0 for word in all_words]
    return tfidf_scores

def getMatrix(documents):
    preprocessed_documents = [preprocess_text(doc) for doc in documents]
    tf_scores = [compute_tf(doc) for doc in preprocessed_documents]
    idf_scores = compute_idf(preprocessed_documents)
    # print(idf_scores)
    # Création d'un tableau contenant tous les mots existants dans tous les documents
    all_words = set([word for doc in preprocessed_documents for word in doc.split()])

    data = {"all_words":all_words,"idf_scores":idf_scores}
    # Création d'une matrice sous forme de tableau à une seule dimension pour chaque document
    matrix = []
    for i, doc in enumerate(preprocessed_documents):
        tfidf_scores = compute_tfidf(tf_scores[i], idf_scores, all_words)
        matrix.append(tfidf_scores)
    return data,matrix

def getMatrixPrediction(texte,all_words,idf_scores):
    preprocessed_documents = [preprocess_text(doc) for doc in [texte]]
    tf_scores = compute_tf(preprocessed_documents[0])
    print(tf_scores)
    tfidf_scores = compute_tfidf(tf_scores,idf_scores,all_words)
    return tfidf_scores


# documents = [
#     "Ce document parle de la classification des textes.",
#     "La classification est  une tâche importante en traitement du langage naturel.",
#     "Le TF-IDF est une mesure couramment utilisée pour la classification de textes."
# ]

# matrix = getMatrix(documents)
# print("Score TF-IDF sous forme de matrice:")
# for i, doc_scores in enumerate(matrix):
#     print(f"Document {i+1}: {doc_scores}")
