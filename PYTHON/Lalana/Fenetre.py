import tkinter as tk
from tkinter import ttk
from Route import Route
from Reparation import Reparation
from PostgresDB import PostgresDB
class Fenetre:
    route =  Route()
    reparation = Reparation()
    db = PostgresDB()
    connection = db.connect()
        
    # Créer une instance de la classe Tk
    root = tk.Tk()
    # root.geometry("500x500")
    tableau = ttk.Treeview(root)

    # Ajouter des en-têtes de colonne
    tableau["columns"] =("Route", "Etat", "Distance","Devis","Reparation/Jour")
    tableau.column("#0", width=0, stretch=tk.NO)
    tableau.column("Route",anchor=tk.CENTER, width=100)
    tableau.column("Etat",anchor=tk.CENTER, width=100)
    tableau.column("Distance",anchor=tk.CENTER, width=100)
    tableau.column("Devis",anchor=tk.CENTER, width=100)
    tableau.column("Reparation/Jour",anchor=tk.CENTER, width=100)
    select = route.selectAll(connection)
    connection.close()
    # Ajouter des données au tableau
    for a in range(0,len(select)):
        tableau.insert(parent="", index="end", iid=a, text="", values=(select[a].getRoute_national(), select[a].getLavaka(),(select[a].getPkFin()-select[a].getPkDebut()), int(reparation.PrixGoudronById(a)),int(reparation.tempsDeFabrication(a))))
        # Afficher le tableau
        tableau.pack()
    root.mainloop()

        # Lancer la boucle principale de la fenêtre
