require './objet/Rapport.rb'
require './objet/LalanaSimba.rb'
class Lalana
    
    def initialize(idlalana,nomlalana,longueur,largeur,types,formule)
        @idlalana = idlalana
        @nomlalana = nomlalana
        @longueur = longueur
        @largeur = largeur
        @types = types
        @formule = formule
    end

    @lalana = []
    def self.getAllLalana(con)
        result = con.exec("select * from lalana")
        rep = []
        result.each do |row|
            rep.push(Lalana.new(row['idlalana'],row['nomlalana'],row['longueur'],row['largeur'],row['types'],row['formule']))
        end
        return rep
    end

    def self.getOneLalana(con,id)
        req = "select * from lalana where idlalana = #{id}"
        result = con.exec(req)
        rep = []
        result.each do |row|
            rep.push(Lalana.new(row['idlalana'],row['nomlalana'],row['longueur'],row['largeur'].to_i,row['types'],row['formule']))
        end
        return rep[0]
    end

    def getListPrestataire(con)
        req = "select * from rapport where idl="+@idlalana.to_s+" order by rapport desc"
        result = con.exec(req)
        pre = []
        result.each do |row|
            pre.push(Rapport.new(row['idp'].to_f,row['nom'],row['idl'].to_f,row['nomlalana'],row['prix'].to_f,row['v'].to_f,row['qualite'].to_f,row['rapport'].to_f))
        end
        return pre
    end

    def getAllSimba(con)
        req = "select * from simba where idlalana = "+@idlalana.to_s
        result = con.exec(req)
        rep = []
        result.each do |row|
            rep.push(LalanaSimba.new(row['idsimba'],row['idlalana'],row['pk1'].to_i,row['pk2'].to_i,row['niveau'].to_f))
        end
        @lalana = rep
        return rep
    end

    def calCout(pres)
        total = 0
        for value in @lalana
            v = value.calCout(@largeur,pres)
            total = total + v
        end
        return total
    end

    def self.changeFormule(con,id,fo)
        req = "insert into formule values (default,'"+id.to_s+"','"+fo+"',now())"
        con.exec(req)
    end

    def calDure(pres)
        total = 0
        for value in @lalana
            v = value.calDure(@largeur,pres)
            total = total + v
        end
        return total
    end

    def idlalana
        @idlalana
    end
    def lalana
        @lalana
    end
    def nomlalana
        @nomlalana
    end
    def longueur
        @longueur
    end
    def largeur
        @largeur
    end
    def types
        @types
    end
    def formule
        @formule
    end

    def idlalana=(new_idlalana)
        @idlalana = new_idlalana
    end
    def lalana=(new_lalana)
        @lalana = new_lalana
    end
    def nomlalana=(new_nomlalana)
        @nomlalana = new_nomlalana
    end
    def longueur=(new_l)
        @longueur = new_l
    end
    def largeur=(new_l)
        @largeur = new_l
    end
    def types=(new_t)
        @types = new_t
    end
    def formule=(new_f)
        @formule = new_f
    end

end