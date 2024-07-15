package arbre;
import java.util.*;
public class Noeud{
	int value = -1804;
	Noeud sup = null;
	Noeud droit = null;
	Noeud gauche = null;
	
	public Noeud (){}
	
	public void inserer(int i, Noeud supe){
		if(value==-1804){
			this.setValue(i);
			this.setSup(supe);
		}else{
			if(i<value){
				if(gauche==null){
					gauche = new Noeud();
				}
				gauche.inserer(i, this);
			}else{
				if(droit==null){
					droit = new Noeud();
				}
				droit.inserer(i,this);
			}
		}
	}
	
	public void delete(int i)throws Exception{
		Noeud d = this.recherche(i);
		if(d.gauche==null && d.droit==null){

			System.out.println("jereo fa tsy mety ");
			d = null;
		}
		else if(d.gauche==null){
			d.getDroit().setSup(d.getSup());
			d = d.getDroit();
			System.out.println("jereo fa tsy mety "+ d.value+" "+d.getSup().getSup());
		}
		else if(d.droit==null){
			System.out.println("jereo fa tsy mety 2");
			d.getGauche().setSup(d.getSup());
			d = d.getGauche();
		}
		else{
			System.out.println("jereo fa tsy mety 3");
			Noeud min = d.getDroit().getMin();
			d.setValue(min.getValue());
			if(min.gauche==null && min.droit==null){
				min = null;
			}else if(min.gauche==null){
				min = min.getDroit();
			}else{
				min = min.getGauche();
			}
		}
	}

	
	
	public Noeud recherche(int i)throws Exception{
		Noeud valiny = null;
		if(value==i){
			return this;
		}else if(i<value){
			if(gauche==null){
				throw new Exception("valeur inexistante");
			}else{
			valiny = gauche.recherche(i);
			}
		}else if(i>value){
			if(droit==null){
				throw new Exception("valeur inexistante");
			}else{
			valiny = droit.recherche(i);
			}
		}
		return valiny;
	}
	
	public void trier(Vector trie){	
		this.getMin().adder(trie);
	}
	
	public void adder(Vector trie){
		trie.add(this.getValue());
		if(this.getDroit()!=null){
			Noeud dr = this.getDroit();
			dr.trier(trie);
		}

		if(this.getSup()!=null && this.getSup().getGauche()==this){
		this.getSup().adder(trie);
		}
	}
	
	public Noeud getMin(){
		Noeud min = this;
		while(min.getGauche()!=null){
			min = min.getGauche();
		}
		return min;
	}

	
	public Noeud getMax(){
		Noeud max = this;
		while(max.getDroit()!=null){
			max = max.getDroit();
		}
		return max;
	}
	
	
	public int getValue(){
		return value;
	}
	
	public Noeud getSup(){
		return sup;
	}
	
	public Noeud getDroit(){
		return droit;
	}
	
	public Noeud getGauche(){
		return gauche;
	}
	
	public void setValue(int i){
			value = i;
	}
	
	public void setSup(Noeud i){
		sup = i; 	
	}
	
	public void setDroit(Noeud i){
		droit = i;
	}
	
	public void setGauche(Noeud i){
		gauche = i;
	}
	
}