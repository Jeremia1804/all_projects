from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class Cryptography:
    def __init__(self) -> None:
        self.key = self.numero_en_cle('etu0000000001804')
    # Générer une clé AES-128 aléatoire (128 bits = 16 octets)
    def generer_cle_AES():
        return os.urandom(16)

    def numero_en_cle(self,numero):
        # Assurez-vous que la longueur du numéro est de 4 chiffres (1804)
        # if len(numero) != 4:
        #     raise ValueError("Le numéro de téléphone doit avoir une longueur de 4 chiffres.")
        # Convertir le numéro en octets en utilisant l'encodage UTF-8
        return numero.encode('utf-8')

    # Fonction de chiffrement AES-128
    def encrypt_AES(self, data):
        data = data.encode('utf-8')
        backend = default_backend()

        # Assurez-vous que la clé a la bonne taille (128 bits pour AES-128)
        if len(self.key) != 16:
            raise ValueError("La clé doit avoir une taille de 128 bits (16 octets).")

        # Générer un vecteur d'initialisation (IV) aléatoire
        iv = os.urandom(16)

        # Créer l'objet Cipher avec l'algorithme AES-128 en mode CBC
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=backend)

        # Créer un objet encrypteur
        encryptor = cipher.encryptor()

        # Remplir le texte clair pour qu'il soit multiple de 16 octets (taille du bloc AES)
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()

        # Chiffrer les données
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        # Renvoyer l'IV concaténé avec le texte chiffré
        return iv + ciphertext

    # Fonction de déchiffrement AES-128
    def decrypt_AES(self, encrypted_data):
        backend = default_backend()

        # Assurez-vous que la clé a la bonne taille (128 bits pour AES-128)
        if len(self.key) != 16:
            raise ValueError("La clé doit avoir une taille de 128 bits (16 octets).")

        # Extraire l'IV du texte chiffré
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        # Créer l'objet Cipher avec l'algorithme AES-128 en mode CBC
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=backend)

        # Créer un objet decrypteur
        decryptor = cipher.decryptor()

        # Déchiffrer les données
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()

        # Supprimer le padding pour récupérer le texte clair d'origine
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()

        return data

crypt = Cryptography()

texte_a_chiffrer = 'Ceci est un texte à chiffrer en utilisant AES-128.'

# Chiffrer les données
texte_chiffre = crypt.encrypt_AES(texte_a_chiffrer)
print("Texte chiffré :", texte_chiffre)

# Déchiffrer les données
texte_dechiffre = crypt.decrypt_AES(texte_chiffre)
print("Texte déchiffré :", texte_dechiffre.decode('utf-8'))
