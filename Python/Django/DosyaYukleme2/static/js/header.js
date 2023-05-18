 function headerPencereBoyut(){/* Header listesini küçültüp 3 çizgiye buton olarak atar */
    var headerListe=document.getElementsByClassName("w3-right w3-container w3-padding")[0];
     if (window.innerWidth < 601){
      headerListe.style.display ="none";
        document.getElementsByClassName("w3-container w3-padding")[0].style.display ="block";
        document.getElementsByClassName("w3-display-container w3-red w3-bar")[0].style.height="66px";
        if(headerListe.className.indexOf("w3-dropdown-content")== -1){
         headerListe.className+=" w3-dropdown-content";
        }
     }
     else{
        document.getElementsByClassName("w3-container w3-padding")[0].style.display ="none";
        document.getElementsByClassName("w3-display-container w3-red w3-bar")[0].style.height="54.5px";
        headerListe.style.display ="block";
        if(headerListe.className.indexOf("w3-dropdown-content")> -1){
         console.log(headerListe.className.indexOf("w3-dropdown-content"));
         headerListe.className = headerListe.className.replace(" w3-dropdown-content","");
        }
     }
 }
function headerTus(){/*3 noktaya basınca aşağı doğru açılan pencere*/
   var headerListe=document.getElementsByClassName("w3-right w3-container w3-padding")[0];
   if (headerListe.className.indexOf("w3-show") == -1) {
      headerListe.className += " w3-show";
      document.getElementsByClassName("w3-display-container w3-red w3-bar")[0].style.height=(headerListe.clientHeight+document.getElementsByClassName("w3-container w3-padding")[0].clientHeight).toString()+"px";
      console.log(headerListe.offsetHeight)
      
    } else { 
      headerListe.className = headerListe.className.replace(" w3-show", "");
      document.getElementsByClassName("w3-display-container w3-red w3-bar")[0].style.height="66px";
    }
}
