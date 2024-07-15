package main;
import arbre.*;
import java.util.*;
public class Main{
	public static void main(String[] args)throws Exception{
		int[] tab = new int[5];
		tab[0] = 5;
		tab[1] = 7;

		tab[2] = 4;
		tab[3] = 3;
		tab[4] = 1;
		// int u = +1-+5*(-5+1)*-+-+-+-+-5;
		// System.out.println("andrana :  "+u);
		Noeud arbre = new Noeud();
		for(int i = 0; i<tab.length; i++){
			arbre.inserer(tab[i],null);
		}
		// arbre.inserer(7,null);
		// arbre.inserer(16,null);
		// arbre.inserer(9,null);
		// arbre.inserer(11,null);
		// arbre.delete(3);
		// arbre.inserer(5,null);
		// arbre.inserer(4,null);
		// arbre.inserer(15,null);
		// System.out.println(arbre.getMin().getDroit().getMin().getDroit().getValue());
		
		Vector v = new Vector();
		Noeud min = arbre.getMin();
		System.out.println(min.getValue());
		//System.out.println(arbre.getMin().getValue());
		// System.out.println(arbre.getGauche().getValue());
		// arbre.trier(v);	
		// for(int i=0; i<v.size(); i++){
		// 	System.out.println(v.get(i));
		// }

		// Noeud re = arbre.recherche(8);
		// System.out.println("valeur: 	 "+re.getValue());
		
	}
}