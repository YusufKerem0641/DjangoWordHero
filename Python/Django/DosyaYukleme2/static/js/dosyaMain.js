function imageSize() {/* resim boyutlarını mobile ve pc ye göre ayarlıyoruz */
    var images = document.getElementsByClassName("w3-block");
    if (window.innerWidth < 601) {
        for (var i = 0; i < images.length; i++) {
            images[i].style.width = (window.innerWidth - 102).toString() + "px";
        }
    }
    else{
        for (var i = 0; i < images.length; i++) {
            images[i].removeAttribute("style");
        }
        
    }
}