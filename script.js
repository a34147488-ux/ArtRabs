// ArtRabs Game // ======================
// ArtRabs Game System
// ======================


// Балансы

let multiStars =
Number(localStorage.getItem("multiStars")) || 0;


let stars =
Number(localStorage.getItem("stars")) || 0;



// Работник

let workerLevel =
Number(localStorage.getItem("workerLevel")) || 1;



let refs =
Number(localStorage.getItem("refs")) || 0;



let refMoney =
Number(localStorage.getItem("refMoney")) || 0;




// Обновление экрана

function updateBalance(){


document.getElementById("multi").innerHTML =
multiStars;


document.getElementById("stars").innerHTML =
stars;



document.getElementById("profileMulti").innerHTML =
multiStars;


document.getElementById("profileStars").innerHTML =
stars;



document.getElementById("workerLevel").innerHTML =
workerLevel;



document.getElementById("workerIncome").innerHTML =
workerLevel * 40;



document.getElementById("refsCount").innerHTML =
refs;



document.getElementById("refMoney").innerHTML =
refMoney;


save();

}





function save(){


localStorage.setItem(
"multiStars",
multiStars
);


localStorage.setItem(
"stars",
stars
);


localStorage.setItem(
"workerLevel",
workerLevel
);


localStorage.setItem(
"refs",
refs
);


localStorage.setItem(
"refMoney",
refMoney
);


}





// ======================
// КЛИКЕР
// ======================


document
.getElementById("clickBtn")
.onclick = function(){


multiStars += 1;


updateBalance();


showPopup(
"+1 Multi ⭐"
);


};






// ======================
// РУЛЕТКА
// ======================


document
.getElementById("wheelBtn")
.onclick = function(){


let reward =
Math.floor(Math.random()*6);



stars += reward;



updateBalance();



alert(
"🎁 Рулетка\n\nТы получил:\n⭐ "
+
reward
);



};







// ======================
// СТРАНИЦЫ
// ======================


function openPage(page){


let pages =
document.querySelectorAll(".page");



pages.forEach(function(item){


item.style.display="none";


});



document.getElementById(page)
.style.display="block";



}








// ======================
// ПРОКАЧКА РАБОТНИКА
// ======================


function upgradeWorker(){



if(workerLevel >= 50){


alert(
"Максимальный уровень!"
);


return;


}



let price =
workerLevel * 500;



if(multiStars < price){


alert(
"Нужно "
+
price
+
" Multi Stars"
);



return;


}




multiStars -= price;



workerLevel++;



updateBalance();



alert(
"Работник улучшен!\nУровень: "
+
workerLevel
);



}








// ======================
// РЕФЕРАЛЫ
// ======================


function invite(){



let link =
window.location.href
+
"?ref="
+
Date.now();



alert(
"Твоя ссылка ArtRabs:\n\n"
+
link
+
"\n\nЗа приглашение:\n+500 Multi Stars"
);



}








// ======================
// ОБМЕН
// ======================


function exchange(){



if(multiStars < 1000){


alert(
"Минимальный обмен: 1000 Multi Stars"
);



return;


}



let result =
Math.floor(multiStars / 4000);



stars += result;



multiStars = 0;



updateBalance();



alert(
"Обмен выполнен!\nПолучено ⭐ "
+
result
);



}









// ======================
// КЕЙСЫ
// ======================


function openCase(){



let price = 500;



if(multiStars < price){


alert(
"Нужно 500 Multi Stars"
);



return;


}



multiStars -= price;



let result =
[
-1000,
0,
500,
1000,
2000,
3500
]
[
Math.floor(
Math.random()*6
)
];



multiStars += result;



updateBalance();



alert(
"📦 Кейс открыт!\n\nРезультат:\n"
+
result
+
" Multi Stars"
);



}








// ======================
// АНИМАЦИЯ
// ======================


function showPopup(text){



let popup =
document.createElement("div");



popup.innerHTML=text;



popup.style.position="fixed";

popup.style.left="50%";

popup.style.top="40%";

popup.style.transform=
"translate(-50%,-50%)";

popup.style.color="#FFD700";

popup.style.fontSize="30px";

popup.style.fontWeight="bold";

popup.style.zIndex="999";



document.body.appendChild(popup);



setTimeout(()=>{


popup.remove();


},800);



}







// Запуск


updateBalance();


openPage("home");Logic


