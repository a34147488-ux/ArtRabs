// ArtRabs Game Logic


let multiStars = Number(localStorage.getItem("multiStars")) || 0;

let stars = Number(localStorage.getItem("stars")) || 0;



const multiText = document.getElementById("multi");

const starsText = document.getElementById("stars");



function updateBalance(){

    multiText.innerHTML = multiStars;

    starsText.innerHTML = stars;


    localStorage.setItem(
        "multiStars",
        multiStars
    );


    localStorage.setItem(
        "stars",
        stars
    );

}



updateBalance();




// КЛИКЕР


document
.getElementById("clickBtn")
.onclick = function(){


    multiStars += 1;


    updateBalance();


    showReward("+1 Multi ⭐");

};




// РУЛЕТКА


document
.getElementById("wheelBtn")
.onclick = function(){


    let reward = Math.floor(
        Math.random() * 6
    );


    stars += reward;


    updateBalance();


    alert(
        "🎁 Рулетка\n\nТы получил: "
        + reward
        + " ⭐"
    );


};





// Анимация награды


function showReward(text){


    let item = document.createElement("div");


    item.innerHTML = text;


    item.style.position = "fixed";

    item.style.left = "50%";

    item.style.top = "45%";

    item.style.transform =
    "translate(-50%,-50%)";


    item.style.color =
    "#FFD700";


    item.style.fontSize =
    "25px";


    item.style.fontWeight =
    "bold";


    item.style.zIndex =
    "999";


    document.body.appendChild(item);



    setTimeout(()=>{

        let workerLevel =
Number(localStorage.getItem("workerLevel")) || 1;


let refs =
Number(localStorage.getItem("refs")) || 0;



function openPage(page){

document.querySelectorAll(".page")
.forEach(p=>p.style.display="none");


document.getElementById(page)
.style.display="block";

}



function upgradeWorker(){


if(workerLevel < 50){


workerLevel++;


localStorage.setItem(
"workerLevel",
workerLevel
);


document.getElementById(
"workerLevel"
).innerHTML = workerLevel;


document.getElementById(
"workerIncome"
).innerHTML =
workerLevel * 40;


}

}





function invite(){


let link =
window.location.href
+
"?ref="
+
Date.now();



alert(
"Твоя ссылка:\n\n"
+
link
);


}





function exchange(){


if(multiStars >= 1000){


let getStars =
Math.floor(
multiStars / 4000
);


stars += getStars;


multiStars = 0;


updateBalance();


alert(
"Обмен выполнен!\nПолучено ⭐ "
+
getStars
);


}

else{


alert(
"Нужно минимум 1000 Multi Stars"
);


}

}





openPage("home");
    },800);


}
