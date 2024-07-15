var texte = document.querySelectorAll('[name="texte"]');
texte = texte[0];
console.log(texte);

var divsug = document.getElementById("suggestion");


function getText(){
    let tableau  = getTableau();
    let motfin = tableau[tableau.length-1];
    return motfin;
}

function getTableau(){
    let tableau  = texte.value.split(" ");
    return tableau;
}

function suggerer(){
    var xhr = new XMLHttpRequest();
    let mot = getText();
    let formdata = new FormData();
    formdata.append("mot",mot);
    xhr.open("POST", "/suggestion", true);
    xhr.onload = function(){
        if(xhr.status === 200){
            var valeur = JSON.parse(xhr.responseText);
            afficher(valeur);
            listener();
        }
    };
    xhr.send(formdata);
}

function afficher(tab){
    let str = "";
    for (let i=0; i<tab.length; i++){
        str += "<div class='btn btn-primary btn-sl-sm me-2 sug'>"+tab[i]+"</div>"
    }
    divsug.innerHTML = str;
}

function listener(){
    const sugs = document.querySelectorAll(".sug");
    sugs.forEach(sug => {
        sug.addEventListener("click",function(){
            mot = sug.textContent; 
            final(mot);
        });
    });
}

function final(mot){
    let tab = getTableau();
    let str = "";
    for(let i=0; i<tab.length-1; i++){
        str += tab[i] +" ";
    }
    str += mot+" ";
    texte.value = str;
}