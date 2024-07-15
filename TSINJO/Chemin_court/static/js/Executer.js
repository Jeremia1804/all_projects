class Executer{
    constructor() {
        
    }

    couper(){
        let select1 = document.getElementById("select1");
        let select2 = document.getElementById("select2");

        let ip1 = +select1.value
        let ip2 = +select2.value

        var xhr = new XMLHttpRequest();
            xhr.open("POST", "/couper", true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function(){
                if(xhr.status === 200){
                    
                }
            };
            
            xhr.send(JSON.stringify([ip1,ip2]));

    }

    search(){
        let select3 = document.getElementById("select3");
        let select4 = document.getElementById("select4");

        let ip3 = +select3.value
        let ip4 = +select4.value

        var xhr = new XMLHttpRequest();
            xhr.open("POST", "/search", true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function(){
                if(xhr.status === 200){
                    
                }
            };
            
            xhr.send(JSON.stringify([ip3,ip4]));

    }

    actualiserImage(){
        let image = document.getElementById("myImage");
        var timestamp = new Date().getTime();
        image.src = "/static/img/toi.png?t="+timestamp;
    }

    addListener(){
        //couper
        let couper = document.getElementById("couper")
        couper.addEventListener("click",function(){
            execution.couper();
        });

        //trouver
        let trouver = document.getElementById("trouver")
        trouver.addEventListener("click",function(){
            execution.search();
        });
    }
}