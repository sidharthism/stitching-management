// dropdown footer

let designCard = document.querySelectorAll("footer .container .design");


for(let i=0; i<designCard.length; i++){

  let current = designCard[i].querySelector(".expand-btn");
  let toggle = false;
  let designItems = designCard[i].querySelectorAll(".items");
  current.addEventListener('click',()=>{
    if(!toggle){
      designItems.forEach(item => item.style.display="block");
      current.style.transform = "translate(-50%,10%) rotate(180deg)";
    }
    else{
      designItems.forEach(item => item.style.display="none");
      current.style.transform = "translate(-50%,10%) rotate(0deg)";
    }
    toggle=!toggle;
  });
}