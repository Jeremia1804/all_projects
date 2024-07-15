class Fonction:

    @staticmethod
    def diviserImage(image,larg,haut):
        image = image.resize((420,420))
        largeur, hauteur = image.size
        
        larg_sous_image = largeur // larg
        haut_sous_image = hauteur // haut
        sous = []
        for i in range(haut):
            sous_sous = []
            for j in range(larg):
                y1 = i*haut_sous_image
                x1 = j*larg_sous_image
                y2 = y1 + haut_sous_image
                x2 = x1 + larg_sous_image

                sous_image = image.crop((x1,y1,x2,y2))
                sous_sous.append(sous_image)
            sous.append(sous_sous)
        return sous
