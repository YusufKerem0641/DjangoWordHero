function mainPencereBoyut() {/*pencere boyutna göre yüksekliği ayarlar*/
    if (window.innerWidth > 599) {
        var etiketler = document.getElementsByClassName("w3-display-container");
        for (var i = 2; i < etiketler.length; i++) {
            etiketler[i].style.height = ((window.innerHeight - 55) / 3).toString() + "px";
        }

        document.getElementsByClassName("w3-display-container")[1].style.height = (document.getElementsByClassName("w3-third")[1].clientHeight).toString() + "px";
    }
}