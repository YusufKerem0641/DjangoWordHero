function hakkimizda_div_boyut(){
    var divler=document.getElementsByClassName("w3-half w3-container ");
    var resim1=document.getElementById("resim1");
    resim1.style.height=(divler[0].clientHeight-20).toString()+"px";
    
}