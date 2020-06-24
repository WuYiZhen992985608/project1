$(function () {
    document.documentElement.style.fontSize = innerWidth / 10 + "px";

    function change_img(imgname) {
        var imgnum = imgname.slice(-5)[0]
        console.log(imgnum)
        if (imgnum !== '1') {
            imgnum = '1'
        } else {
            imgnum = ''
        }
        var imgstr = imgname.split('.')
        var img = imgstr[0] + imgnum + '.' + imgstr[1]
        console.log(img)
        return img
    }

    var jsa = document.getElementsByClassName("footer_span")
    for (var i = 0; i < jsa.length; i++) {
        jsa[i].addEventListener('click', function () {
            var reg = /(\w+).png/g
            var imgname = reg.exec(this.attributes['style'].nodeValue)[0]
            // console.log(imgname)
            img = change_img(imgname)
            this.style.backgroundImage = 'url(/static/main/img/' + img + ')'
        }, false)
    }
    // console.log("8888")
    var Jsbg1 = document.getElementById('bg1')
    var Jsbg2 = document.getElementById('bg2')
    var bgtimer = setInterval(function () {
        Jsbg1.style.left = Jsbg1.offsetLeft - 1 + "px"
        Jsbg2.style.left = Jsbg2.offsetLeft - 1 + "px"
        if (Jsbg1.offsetLeft <= -360) {
            Jsbg1.style.left = "360px"
        }
        if (Jsbg2.offsetLeft <= -360) {
            Jsbg2.style.left = "360px"
        }
    }, 20)

    function checkmenu(){
        var currenturl = window.location.href
        // console.log(currenturl)
        var keywords =currenturl.split("/")
        // console.log(keywords)
        var Jsdivs = document.getElementsByClassName("markdiamond")
        for (var i=0;i<Jsdivs.length;i++){
            var Jsdiv = Jsdivs[i]
            var keyword = Jsdiv.getAttribute("id").split("d")[1]
            // console.log(keyword)
            if (keywords.indexOf(keyword) != -1){
                Jsdiv.style.display = "block"
            }else{
                Jsdiv.style.display = "none"
            }

        }
    }
    checkmenu()
})








