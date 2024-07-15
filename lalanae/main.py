from objet.Lalana import *
from base.MyConnection import *
from affichage.Map import *

conn = MyConnection.connect()
rn2 = Lalana.getLalanaById(conn,1)
print(rn2.getCoutRN(conn))
conn.close()

