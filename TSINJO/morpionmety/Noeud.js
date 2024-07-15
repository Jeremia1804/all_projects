class Noeud{
    constructor(val1, val2,val3) {
        this.noeudPred = val1;
        this.state = val2;
        this.mouv = val3;
    }

    getNoeudPred(){
        return this.noeudPred;
    }

    getState(){
        return this.state;
    }

    setNoeudPred(value){
        this.noeudPred = value;
    }

    setState(value){
        this.state = value;
    }
    getMouv(){
        return this.mouv;
    }
}