var btn_decouper = document.getElementById("decouper")
var btn_melanger = document.getElementById("melanger")
var input_larg = document.getElementById("larg")
var input_long = document.getElementById("long")


btn_decouper.addEventListener("click", function(){
    val_larg = input_larg.value;
    val_long = input_long.value;
    console.log("bonjour")
    diviser(val_larg,val_long);

});

btn_melanger.addEventListener("click", function(){
    melanger();
});


function diviser(larg,hauteur){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/diviser", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function(){
        if(xhr.status === 200){
            var valeur = JSON.parse(xhr.responseText);
            setAffichage(valeur);
            coups = 0;
            updateInfo();
            putListener();
        }
    };

    var data = {
        larg: larg,
        hauteur: hauteur
    };

    xhr.send(JSON.stringify(data));
}

function melanger(){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/melanger", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function(){
        if(xhr.status === 200){
            var valeur = JSON.parse(xhr.responseText);
            setAffichage(valeur);
            putListener();
        }
    };

    xhr.send(null);
}

function manakisaka(data1,data2){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/bouger", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function(){
        if(xhr.status === 200){
            var valeur = JSON.parse(xhr.responseText);
            setAffichage(valeur.noeuds);
            if(valeur.etat == true){
                updateInfo();
                alert("Vous avez fini le Jeu a "+coups+" coups")
                coups = 0;
                updateInfo();
            }
            putListener();
        }
    };

    var data = {
        data1: data1,
        data2: data2
    };

    xhr.send(JSON.stringify(data));
}


function setAffichage(donnee){
    let div_jeu = document.getElementById("jeu");
    div_jeu.innerHTML = "";
    let str = "";
    for(let i=0; i<donnee.length; i++){
        str=str+`<div id="ligne" class="ligne">`;
        for(let j=0; j<donnee[i].length; j++){
            str = str+`<div class="img_puzzle" id="`+j+";"+i+`"><img id="`+j+";"+i+`" src="data:image/jpg;base64,`+donnee[i][j].image+`"/></div>`;
        }
        str = str + `</div>`
    }
    div_jeu.innerHTML = str;
}

function updateInfo(){
    document.getElementById("message").innerText = coups + " coups";
}

var select1 = null;
var coups = 0
function putListener() {
    let r = document.querySelectorAll(".img_puzzle");
    console.log(r)
    r.forEach(element => {
        element.addEventListener("click", function(){
            if (select1==null) {
                console.log("B1")
                select1 = element.getAttribute("id");
            }else{
                console.log("B2")
                let select2 = element.getAttribute("id");
                if(select1 == select2){
                }else{
                    manakisaka(select1,select2)
                    coups  = coups + 1
                    updateInfo();
                }
                select1 = null;
            }
        });
    });
}

putListener();

function rotation(deg) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/rotate", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function(){
        if(xhr.status === 200){
            var valeur = JSON.parse(xhr.responseText);
            setAffichage(valeur);
            putListener();
        }
    };

    var data = {
        degre: deg
    };

    xhr.send(JSON.stringify(data));
}

var rotateplus = document.getElementById("rotateplus");
var rotatemoins = document.getElementById("rotatemoins");

rotateplus.addEventListener("click", function() {
    rotation(90);
})

rotatemoins.addEventListener("click", function() {
    rotation(-90);
})
