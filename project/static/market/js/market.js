$(document).ready(function(){
    var alltypebtn = document.getElementById("alltypebtn")
    var showsortbtn = document.getElementById("showsortbtn")
    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")
    var ayellows = document.getElementsByClassName("ayellow")
    // typediv.style.display = "none"
    // sortdiv.style.display = "none"
    alltypebtn.addEventListener("click",function(){
        typediv.style.display = "block"
    },false)
    showsortbtn.addEventListener("click",function(){
        sortdiv.style.display = "block"
    },false)
    typediv.addEventListener("click",function(){
        typediv.style.display = "none"
    },false)
    sortdiv.addEventListener("click",function(){
        sortdiv.style.display = "none"
    },false)
    var currenturl = window.location.href
    compare_categoryid(ayellows,currenturl)
})
// 将url中categoryid与a标签中categoryid作比较，相同的将span标签display改为block
function compare_categoryid(ayellows,currenturl){
    // console.log(currenturl)
    var categoryid_1 = currenturl.split('/')[4]
    // console.log(categoryid_1[4])
    // console.log(ayellows.length)
    for (var i=0;i < ayellows.length;i++) {
        categoryid_2 = ayellows[i].getAttribute("href").split("/")[2]
        if (categoryid_2 == categoryid_1){
            ayellows[i].previousSibling.previousSibling.style.display = "block"
        }
    }
// 修改购物车
    var addShoppings = document.getElementsByClassName('addShopping')
    var subShoppings = document.getElementsByClassName('subShopping')
    // console.log(addShoppings.length)
    for (var i=0;i<addShoppings.length;i++){
        var addShopping = addShoppings[i]
        addShopping.addEventListener('click',function(){
            var pid = this.getAttribute('ga')
            $.post('/changecart/0/',{'productid':pid},function(data){
                if (data.status == 'success'){
                    console.log(data.data)
                    document.getElementById(pid).innerHTML = data.data
                }else{
                    if (data.data == -1){
                        window.location.href = 'http://127.0.0.1:8000/login/'
                    }
                }
            })
        },false)
    }
    for (var i=0;i<subShoppings.length;i++){
        var subShopping = subShoppings[i]
        subShopping.addEventListener('click',function(){
            var pid = this.getAttribute('ga')
            $.post('/changecart/1/',{'productid':pid},function(data){
                if (data.status == 'success'){
                    console.log(data.data)
                    document.getElementById(pid).innerHTML = data.data
                }else{
                    if (data.data == -1){
                        window.location.href = 'http://127.0.0.1:8000/login/'
                    }
                }
            })
        },false)
    }
    // var Jsselectedspan = document.getElementById("selected")
    // console.log(Jsselectedspan.innerHTML)
    // if (!Jsselectedspan.innerHTML){
    //     Jsselectedspan.display = "none"
    // }else{
    //     Jsselectedspan.display = "block"
    // }
    var favorites = document.getElementsByClassName("glyphicon glyphicon-heart")
    for (var k=0;k<favorites.length;k++){
        var favorite = favorites[k]
        favorite.addEventListener("click",function(){
            this.style.color = "red"
            var pid = this.getAttribute("id").split("g")[0]
            $.post('/favorite/',{'productid':pid},function(data){
                if (data.status == 'success'){
                }else {
                    if (data.data == -1) {
                        window.location.href = "/login/"
                    }
                }
            })
        },false)
    }


}