class Taquin{

    constructor() {
        this.grille = new Grille();
        this.solved = false;
        this.solvedByPlayer = false;
    }

    getGrid(){
        return this.grille;
    }

    changeBackground(){
        //On cherche le thème choisi
        let selectID = document.getElementById("themes");
        let bg = selectID.options[selectID.selectedIndex].value;

        for (let i = 0; i < 3; i++){
            for (let j = 0 ; j < 3; j++){
                //On récupère l'id de la photo devant être la "normalement"
                let elementID = "photo" + ((i*3 + j+1)%9);
                //et on le remplace par celui qui y est actuellement
                document.getElementById(elementID).src = "/static/img/" + bg + "/" + bg +"_" + (this.grille.getGrid()[i][j].toString()).toString() + ".jpg" ;
            }
        }
        //On mets à jour l'écran de texte en dessous
        this.updateInfo();

        if (this.solved){
            this.solve();
        }
        else {
            this.unsolve();
        }

        if (this.getGrid().getCorrectMoves() === 9){
            this.solvedByPlayer = true;
            this.victory(bg);
        }
    }

    //Changement du plateau de fin (en cas de victoire en somme)
    victory(bg){
        this.solvedByPlayer = true;
        document.getElementById("message").innerText = "Bravo, puzzle résolu en " + this.getGrid().getMoves() + " coups."
        document.getElementById("photo0").src = "/static/img/" + bg + "/" + bg +"_.jpg" ;
    }

    //Permet de changer l'écran en front-end
    solve(){
        let selectID = document.getElementById("themes");
        let bg = selectID.options[selectID.selectedIndex].value;

        document.getElementById("jeu").style.display = "none";
        document.getElementById("modele").style.display = "flex";
        document.getElementById("photo16").src =  "/static/img/" + bg + "/" + bg +"_16.jpg" ;
        document.getElementById("solution").value = "puzzle";
        document.getElementById("melanger").disabled = true;
    }

    //L'opposé de la méthode du dessus
    unsolve(){
        document.getElementById("jeu").style.display = "flex";
        document.getElementById("modele").style.display = "none";
        // document.getElementById("solution").value = "solution";
        document.getElementById("melanger").disabled = false;
    }

    updateInfo(){
        document.getElementById("message").innerText = this.getGrid().getMoves() + " coup(s), " + this.getGrid().getCorrectMoves() +" bien placé(s)";
    }

    markLegalMoves(){
        let legalMove = this.getGrid().getLegalMove();

        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                //On met la case en mémoire pour économiser des performances
                let pickedCase = this.grille.getGrid()[i][j];
                document.getElementById("photo" + ((3*i+j+1)%9).toString()).style.cursor = "not-allowed";
                for (let z = 0; z < legalMove.length; z++){
                    //Si le move est autorisé
                    if (pickedCase.toString() === legalMove[z].toString()){
                        //Si le taquin n'est pas résoulu encore
                        if (!this.solvedByPlayer){
                            document.getElementById("photo" + ((3*i+j+1)%9).toString()).style.cursor = "pointer";
                        }

                    }
                }
            }
        }
    }

    afficherPatience(){
        let patience = document.getElementById("titre");
        patience.style.display = "block";
    }

    cacherPatience(){
        let patience = document.getElementById("titre");
        patience.style.display = "none";
    }

    addListeners(){
        let square = document.getElementsByClassName("img_puzzle");
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++){
                //On ajoute a chacun des carrés images, un evenement de clic qui permet de jouer d'échanger les cases de place et qui change l'affichage instantanément après le mouvement
                //Et on vérifie quels sont les tuiles qui peuvent bouger (pour le curseur)
                square[3*i + j].addEventListener("click", function(){
                    //On ne peut pas jouer si le taquin est résoulu
                    if (!taquin.solvedByPlayer) {
                        taquin.grille.swapCases(taquin.grille.getGrid()[i][j]);
                    }
                     taquin.changeBackground();
                     taquin.markLegalMoves();
                });
            }
        }

        

        //Tout pareil pour le menu déroulant
        let scrollingMenu = document.getElementById("themes");
        scrollingMenu.addEventListener("click", function(){taquin.changeBackground();});

        //Le bouton mélanger se voit ajouter un listener pour mélanger et un autre pour rafraîchir les tuiles
        let shuffle = document.getElementById("melanger");
        shuffle.addEventListener("click", function () {
            taquin.solvedByPlayer = false;
            taquin.getGrid().randomiseGrid(100);
            taquin.changeBackground();
            //Pour éviter que les cursors ne soient pas mises à jours lors du mélange, on va vérifier après chaque mélange l'emplacement des tuiles
            taquin.markLegalMoves();
            });

        //Le bouton résoudre résoud et rafraîchi le plateau
        // let solve = document.getElementById("solution");
        // solve.addEventListener("click", function(){
        //     taquin.solved = !taquin.solved;
        //     taquin.changeBackground();});
        this.cacherPatience();

        //Le boutton resoudre va resoudre tous le puzzle avec animation
        let resoudre = document.getElementById("resoudre");
        resoudre.addEventListener("click",function(){
            let matrice = taquin.getGrid().getState();

            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/resolution", true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function(){
                if(xhr.status === 200){
                    taquin.cacherPatience();
                    var valeur = JSON.parse(xhr.responseText);
                    taquin.getGrid().boucleavecpause(0,valeur,taquin);
                }
            };
            taquin.afficherPatience();
            xhr.send(JSON.stringify(matrice));
        });
        }

}