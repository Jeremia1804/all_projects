class Rapport

    def initialize(idp,nom,idl,nomlalana,prix,vit,qualite,rapport)
        @idp = idp
        @nom = nom
        @idl = idl
        @nomlalana = nomlalana
        @prix = prix
        @qualite = qualite
        @rapport = rapport
        @vitesse = vit
    end

    def idp
        @idp
    end
    def idl
        @idl
    end
    def nom
        @nom
    end
    def nomlalana
        @nomlalana
    end
    def prix
        @prix
    end
    def qualite
        @qualite
    end
    def rapport
        @rapport
    end
    def vitesse
        @vitesse
    end
end