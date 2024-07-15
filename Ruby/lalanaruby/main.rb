require './objet/Lalana.rb'
require './affichage/Affichage.rb'
require './base/MyConnection.rb'
con = MyConnection.connect()
# # result = con.exec("select * from lalana")
# # result.each do |row|
# #     puts [row['idlalana']]
# # end
# pre = Lalana.getListPrestataire(con,1)
# for value in pre
#     puts value.nom()
# end

# re = Lalana.getOneLalana(con,2)
# re.getAllSimba(con)

# # puts re.calCout(pre[0])
# tab = [1,2]
# puts Affichage.afficherCheck(con)
Lalana.changeFormule(con,1,"5*v + 3*a")
con.close()