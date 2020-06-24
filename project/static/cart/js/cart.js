$(document).ready(function(){
    var addShoppings = document.getElementsByClassName('addShopping')
    var subShoppings = document.getElementsByClassName('subShopping')
    var choses = document.getElementsByClassName("productchose")
    var outertotalChose = document.getElementById("outertotalChose")
    var ischoses = document.getElementsByClassName("ischose")
    var spanprices = document.getElementsByClassName("productprice")
    var totalprice = document.getElementById("totalprice")
    initchose(choses)
    totalChose(choses,outertotalChose)
    Statisticprice()
    function Statisticprice(){
        var Statisticprice = 0
        for (var i=0;i<spanprices.length;i++){
            var spanprice = spanprices[i]
            var pid = spanprice.getAttribute("id").split("p")[0]
            var chose = document.getElementById(pid+'a')
            // console.log("++++"+chose.innerHTML)
            if (chose.innerHTML){
                Statisticprice += parseFloat(spanprice.innerText)
            }
            // console.log("Statisticprice"+Statisticprice)
        }
        // console.log(totalprice)
        // console.log(totalprice.innerText)
        totalprice.innerText = parseFloat(Statisticprice)
    }
    for (var i=0;i<addShoppings.length;i++){
        var addShopping = addShoppings[i]
        addShopping.addEventListener('click',function(){
            var pid = this.getAttribute('ga')
            $.post('/changecart/0/',{'productid':pid},function(data){
                if (data.status == 'success'){
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid+'price').innerHTML = data.price
                    Statisticprice()
                }
            },false)

        })

    }
    for (var i=0;i<subShoppings.length;i++){
        var subShopping = subShoppings[i]
        subShopping.addEventListener('click',function(){
            var pid = this.getAttribute('ga')
            // console.log('pid'+pid)
            $.post('/changecart/1/',{'productid':pid},function(data){
                if (data.status == 'success'){
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid+'price').innerHTML = data.price
                    if (data.data==0) {
                        // window.location.href = 'http://127.0.0.1:8000/cart/'
                        var li = document.getElementById(pid + "li")
                        li.parentNode.removeChild(li)
                    }
                    Statisticprice()
                }
            })
        },false)
    }
    // 以下实现
    for (var j=0;j<ischoses.length;j++) {
        ischose = ischoses[j]
        // console.log(ischose)
        ischose.addEventListener('click', function () {
            var pid = this.getAttribute('goodsid')
            $.post('/changecart/2/', {'productid': pid}, function (data) {
                if (data.status == 'success') {
                    // window.location.href = 'http://127.0.0.1:8000/cart/'
                    var s = document.getElementById(pid+'a')
                    s.innerHTML = data.data
                    s.style.backgroundColor = data.color
                    totalChose(choses,outertotalChose)
                    Statisticprice()
                }
            })
        }, false)
    }
    // 以下实现当商品全选或全不选时"全选"按钮变更状态
    function totalChose(choses,outertotalChose){
        var totalTrue = new Array()
        for (var i=0;i<choses.length;i++){
            var chose = choses[i].innerHTML
            if (chose) {
                totalTrue.push(chose)
            }
        }
        if (totalTrue.length == choses.length){
            outertotalChose.innerHTML = "&#8730;"
            outertotalChose.style.backgroundColor = 'yellow'
        }else{
            outertotalChose.innerText = ""
            outertotalChose.style.backgroundColor = 'white'
        }
    }
    function initchose(choses){
        var datadict = new Array()
        var productidlist = new Array()
        for (var i=0;i<choses.length;i++){
            // console.log(choses.length)
            chose = choses[i]
            var pid = chose.getAttribute("id").split("a")[0]
            // console.log(pid)
            productidlist.push(pid)
            $.post('/changecart/4/',{'productid':pid},function(data){
                // console.log(data)
                datadict.push(data)
            })
        }
        // console.log(datadict)
        // console.log(productidlist)
        for (var i=0;i<choses.length;i++){
            for (var j=0;j<datadict.length;j++){
                if (productidlist[i]==datadict[j].productid){
                    chose.innerHTML = datadict[j].data
                    chose.style.backgroundColor = datadict[j].color
                    break
                }
            }
        }

    }
    // 以下函数实现所有商品同时勾选或取消勾选
    function changeischoses(choses,text){
        for (var j=0;j<choses.length;j++) {
            chose = choses[j]
            if(text){
                chose.innerHTML = "&#8730;"
                chose.style.backgroundColor = "yellow"
            }else{
                chose.innerHTML = ""
                chose.style.backgroundColor = "white"
            }
        }
    }
    // 以下监听全选按钮点击事件
    outertotalChose.addEventListener("click",function () {
        // console.log(outertotalChose.innerHTML)
        if (outertotalChose.innerHTML){
            outertotalChose.innerHTML = ""
            outertotalChose.style.backgroundColor = "white"
            var hasnotext = outertotalChose.innerHTML
            console.log(hasnotext)
            changeischoses(choses,hasnotext)
        }else{
            outertotalChose.innerHTML = "&#8730;"
            outertotalChose.style.backgroundColor = "yellow"
            var hastext = outertotalChose.innerHTML
            console.log(hastext)
            changeischoses(choses,hastext)
        }
        Statisticprice()
    },false)

    var ok = document.getElementById("ok")

    ok.addEventListener("click",function () {
        var f = confirm("是否确认下单？")
        if (f){
            $.post("/saveorder/",function(data){
                if (data.status =="success"){
                    window.location.href = "http://127.0.0.1:8000/cart/"
                    totalChose(choses,outertotalChose)
                }
            })

        }
    },false)


})

