class LalanaSimba

    def initialize(idsimba,idlalana,pk1,pk2,niveau)
        @idsimba = idsimba
        @idlalana = idlalana
        @pk1 = pk1
        @pk2 = pk2
        @niveau = niveau
    end

    def self.getAllSimba(con, idsimba)
        result = con.exec("select * from simba where idlalana")
        rep = []
        result.each do |row|
            rep.push(LalanaSimba.new(row['idsimba'],row['idlalana'],row['pk1'].to_i,row['pk2'].to_i,row['niveau'].to_f))
        end
        return rep
    end

    def self.getOneSimba(con, idsimba)
        result = con.exec("select * from simba where idsimba ="+idsimba.to_s)
        rep = nil
        result.each do |row|
            rep=LalanaSimba.new(row['idsimba'].to_i,row['idlalana'],row['pk1'].to_i,row['pk2'].to_i,row['niveau'].to_f)
        end
        return rep
    end

    def calCout(larg,pres)
        longe = @pk2 - @pk1
        prof = @niveau
        vol = longe.to_i * larg.to_i * prof
        prix = vol * pres.prix
        return prix
    end

    def calDure(larg,pres)
        longe = @pk2 - @pk1
        prof = @niveau
        vol = longe.to_i * larg.to_i * prof
        prix = vol / pres.vitesse
        return prix
    end

    def idsimba
        @idsimba
    end
    def idlalana
        @idlalana
    end
    def pk1
        @pk1
    end
    def pk2
        @pk2
    end
    def niveau
        @niveau
    end

    def idsimba=(new_idsimba)
        @idsimba=new_idsimba
    end
    def idlalana=(new_idlalana)
        @idlalana = new_idlalana
    end
    def pk1=(new_pk1)
        @pk1 = new_pk1
    end
    def pk2=(new_pk2)
        @pk2 = new_pk2
    end
    def niveau=(new_niveau)
        @niveau = new_niveau
    end
end