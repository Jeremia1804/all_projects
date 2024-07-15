class Prestataire

    def initialize(idprestataire,nom,prix,annee,vitesse,penalite)
        @idprestataire = idprestataire
        @nom = nom
        @prix = prix
        @annee = annee
        @vitesse = vitesse
        @penalite = penalite
    end

    # all prestataire
    def self.getAllPrestataire(con)
        result = con.exec("select * from prestataire")
        rep = []
        result.each do |row|
            rep.push(Prestataire.new(row['idprestataire'],row['nom'],row['prix'].to_f,row['annee'],row['vitesse'],row['penalite']))
        end
        return rep
    end

    def self.getOnePrestataire(con, idpre)
        result = con.exec("select * from prestataire where idprestataire = "+idpre)
        rep = []
        result.each do |row|
            rep.push(Prestataire.new(row['idprestataire'],row['nom'],row['prix'].to_f,row['annee'],row['vitesse'],row['penalite']))
        end
        return rep[0]
    end

    def idprestataire
        @idprestataire
    end
    def nom
        @nom
    end
    def prix
        @prix
    end
    def annee
        @annee
    end
    def vitesse
        @vitesse
    end
    def penalite
        @penalite
    end

    def idprestataire=(new_idprestataire)
        @idprestataire = new_idprestataire
    end
    def nom=(new_nom)
        @nom = new_nom
    end
    def prix=(new_prix)
        @prix = new_prix
    end
    def annee=(new_annee)
        @annee = new_annee
    end
    def vitesse=(new_vitesse)
        @vitesse = new_vitesse
    end
    def penalite=(new_penalite)
        @penalite = new_penalite
    end
end