// (document.onload = () => {
let Card = document.querySelectorAll(".card");
let amount = 0;
let items = 0;

for (let i = 0; i < Card.length; i++) {

    let AddBtn = Card[i].querySelector(".right .add-btn");

    let IncreBtn = Card[i].querySelector(".right .inc-btn");

    let num = IncreBtn.querySelector(".num");
    let minus = IncreBtn.querySelector(".minus");
    let plus = IncreBtn.querySelector(".plus");

    let sub = Card[i].querySelector(".left .sub").innerHTML.split(" ")[2].slice(1);
    let tempPrice = parseInt(sub);

    AddBtn.addEventListener("click", function () {
        AddBtn.style.display = "none";
        num.innerHTML = 1;
        amount += tempPrice;
        items += 1;
        console.log(amount);
    });

    plus.addEventListener("click", function () {
        let temp = parseInt(num.innerHTML);
        temp += 1;
        num.innerHTML = temp;
        amount += tempPrice;
        items += 1;
        console.log(amount);
    });

    minus.addEventListener("click", function () {
        let temp = parseInt(num.innerHTML);
        temp -= 1;
        amount -= tempPrice;
        items -= 1;
        console.log(amount);
        if (temp === 0) {
            AddBtn.style.display = "flex";
        }
        else
            num.innerHTML = temp;
    });

}
// })();