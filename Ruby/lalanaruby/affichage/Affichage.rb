require './objet/Lalana.rb'
require './objet/Prestataire.rb'
require './base/MyConnection.rb'

class Affichage
    def self.afficherRNPrest(con,tab)
        rn = []
        for ou in 0..tab.length-1
            rn.push(Lalana.getOneLalana(con,tab[ou]))
        end
        # rn = Lalana.getAllLalana(con)
        stre = ""
        for route in rn
            stre += "<h1>"+route.nomlalana+" <form action='/change' method='get'><input type='hidden' name='id' value='"+route.idlalana+"'><input type='text' name='fo' placeholder='entrer une nouvelle formule'><input type='submit' value='valider'></form></h1>
            <table>
            <thead>
                <tr>
                    <th>Nom Prestataire</th>
                    <th>Prix</th>
                    <th>Qualite</th>
                    <th>Rapport</th>
                    <th>Cout</th>
                    <th>Dure</th>
                </tr>
            </thead>
            <tbody>"
            prest = route.getListPrestataire(con)
            route.getAllSimba(con)
            for pre in prest
                stre += "<tr>
				<td>"+pre.nom+"</td>
				<td>"+pre.prix.to_s+"</td>
				<td>"+pre.qualite.to_s+"</td>
				<td>"+pre.rapport.to_s+"</td>
				<td>"+route.calCout(pre).to_s+"</td>
				<td>"+route.calDure(pre).to_s+"</td>
			</tr>"
            end
            stre += "</tbody>
            </table>
            <br>"
        end
        return stre
    end

    def self.afficherCheck(con)
        rn = Lalana.getAllLalana(con)
        stre = ""
        i = 0;
        for route in rn
            stre += "<label for='checkbox' class='custom-checkbox'>
			<input type='checkbox' name='"+i.to_s+"' id='"+route.idlalana.to_s+"' class='checkbox-input' value='"+route.idlalana.to_s+"'>
			<span class='checkbox-label'>"+route.nomlalana+"</span>
		  </label>
		  <br>"
          i = i+1
        end 
        return stre
    end

    def self.nbLalana(con)
        rep = Lalana.getAllLalana(con)
        return rep.length
    end

    def self.changeFormule(con,id,fo)
        Lalana.changeFormule(con,id,fo)
    end 
end