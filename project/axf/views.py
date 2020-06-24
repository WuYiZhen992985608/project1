from pprint import pprint

from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import time,random,os
from django.conf import settings
from django.urls import reverse
from axf.forms.login import LoginForm
from axf.models import Wheel, Nav, Mustbuy, Shop, Mainshow, FoodType, User, Cart, ProductGoods, Order, Favorite


def home(request):
    wheelslist = Wheel.objects.all()
    navlist = Nav.objects.all()
    mustbuylist = Mustbuy.objects.all()
    shoplist = Shop.objects.all()
    shop1 = shoplist[0]
    shop2 = shoplist[1:3]
    shop3 = shoplist[3:7]
    shop4 = shoplist[7:11]
    mainlist = Mainshow.objects.all()
    return render(request,'axf/home.html',{'title':'主页','wheelslist':wheelslist,'navlist':navlist,'mustbuylist':mustbuylist,'shop1':shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,'mainlist':mainlist})

def market(request,categoryid,cid,sortid):
    leftSliter = FoodType.objects.all()
    if cid == '0':
        productlist = ProductGoods.objects.filter(categoryid=categoryid)
    else:
        productlist = ProductGoods.objects.filter(categoryid=categoryid,childcid=cid)
    if sortid == "1":
        productlist = productlist.order_by("productnum")
    elif sortid == "2":
        productlist = productlist.order_by("price")
    elif sortid == "3":
        productlist = productlist.order_by("-price")
    group = leftSliter.get(typeid=categoryid)
    childlist = []
    arr1 = group.childtypenames.split("#")
    for i in arr1:
        arr2 = i.split(":")
        obj = {"childcidname":arr2[0],"childcid":arr2[1]}
        childlist.append(obj)
    token = request.session.get('token')
    cartlist = []
    favoritelist = []
    fidlist = []
    if token:
        user = User.objects.get(userToken=token)
        cartlist = Cart.obj1.filter(userAccount=user.userAccount)
        favoritelist = Favorite.objects.filter(userAccount=user.userAccount)
    for f in favoritelist:
        fidlist.append(f.productid)
    # print("fidlist",fidlist)
    for p in productlist:
        # print(p.productid)
        for c in cartlist:
            if c.productid == p.productid:
                p.num = c.productnum
                # print('num',p.num)
                continue
    return render(request,'axf/market.html',{'title':'闪送超市','leftSliter':leftSliter,'productlist':productlist,'childlist':childlist,'categoryid':categoryid,'cid':cid,'fidlist':fidlist})




def cart(request):
    cartlist = []
    token = request.session.get('token')
    username = ""
    userphone = ""
    useradderss = ""
    totalprice = 0
    if token != None:
        user = User.objects.get(userToken=token)
        username = user.userName
        userphone = user.userPhone
        useradderss = user.userAdderss
        cartlist = Cart.obj1.filter(userAccount=user.userAccount)
        for c in cartlist:
            unitprice = float(c.productprice)*c.productnum
            totalprice += unitprice
            # print(totalprice)
    return render(request,'axf/cart.html',{'title':'购物车','cartlist':cartlist,'username':username,'userphone':userphone,
                                           'useradderss':useradderss,'totalprice':totalprice})

def changecart(request,flag):
    # 首先判断用户是否登录
    token = request.session.get('token')
    if token==None:
        return JsonResponse({'data':-1,'status':'error'})
    productid = request.POST.get('productid')
    user = User.objects.get(userToken=token)
    product = ProductGoods.objects.get(productid=productid)
    if flag == '0':
        if product.storenums == 0:
            return JsonResponse({'data':-2,'status':'error'})
        carts = Cart.obj1.filter(userAccount=user.userAccount)
        c = None
        if carts.count() == 0:
            c = Cart.createuser(user.userAccount,productid,1,product.price,True,product.productimg,product.productlongname,False)
            c.save()
        else:
            try:
                c = carts.get(productid=productid)
                # print(c.productid)
                c.productnum += 1
                c.productprice = '%.2f'%(float(product.price)*c.productnum)
                c.save()
            except Cart.DoesNotExist as e:
                c = Cart.createuser(user.userAccount, productid, 1, product.price, True, product.productimg,product.productlongname, False)
                # print(c.productid)
                c.save()
        product.storenums -= 1
        product.save()
        return JsonResponse({'data':c.productnum,'price':c.productprice,'status':'success'})
    elif flag == '1':
        carts = Cart.obj1.filter(userAccount=user.userAccount)
        # print(len(carts))
        # print(carts.count())
        # print(productid)
        c = None
        if carts.count() == 0:
            return JsonResponse({'data':-2, 'status': 'error'})
        else:
            try:
                # print('productid',productid)
                c = carts.get(productid=productid)
                c.productnum -= 1
                # print(c.productnum)
                c.productprice = '%.2f'%(float(product.price)*c.productnum)
                if c.productnum == 0:
                    c.delete()
                else:
                    # print(c.productnum)
                    c.save()
            except Cart.DoesNotExist as e:
                return JsonResponse({'data': -2, 'status': 'error'})
        product.storenums += 1
        product.save()
        return JsonResponse({'data':c.productnum,'price':c.productprice,'status':'success'})
    elif flag == '2':
        carts = Cart.obj1.filter(userAccount=user.userAccount)
        c = carts.get(productid=productid)
        c.isChose = not c.isChose
        c.save()
        str = ""
        color = "white"
        if c.isChose:
            str='&#8730;'
            color = 'yellow'
        return JsonResponse({'data':str,'status':'success','color':color})
    elif flag == '3':
        text = request.POST.get('text')
        if text:
            carts = Cart .obj1.filter(userAccount=user.userAccount)
            for c in carts:
                c.isChose = True
                c.save()
            str = "&#8730;"
            color = "yellow"
            return JsonResponse({'data': str, 'status': 'success', 'color': color})
        else:
            carts = Cart.obj1.filter(userAccount=user.userAccount)
            for c in carts:
                c.isChose = False
                c.save()
            str = ""
            color = "white"
            return JsonResponse({'data': str, 'status': 'success', 'color': color})
    elif flag == '4':
        try:
            carts = Cart.obj1.filter(userAccount=user.userAccount)
            c = carts.get(productid=productid)
            str = ""
            color = "white"
            # print(c.productname)
            # print(c.isChose)
            if c.isChose:
                str = '&#8730;'
                color = 'yellow'
            return JsonResponse({'data':str,'status':'success','color':color,'productid':productid})
        except Cart.DoesNotExist as e:
            return JsonResponse({'data': -2, 'status': 'error'})

def mine(request):
    username = request.session.get('username','未登录')
    userimg = ""
    userrank = "等级"
    try:
        user = User.objects.get(userName=username)
        userimg = user.userImg
        userrank = user.userRank
        return render(request,'axf/mine.html',{'title':'我的','username':username,'userimg':userimg,'userrank':userrank})
    except Exception as e:
        return render(request,'axf/mine.html',{'title':'我的','username':username,'userimg':userimg,'userrank':userrank})


def login(request):
    if request.method == 'POST':
        f = LoginForm(request.POST)
        if f.is_valid():
            nameid = f.cleaned_data['username']
            pswd = f.cleaned_data['passwd']
            try:
                user = User.objects.get(userAccount=nameid)
                if user.userPasswd != pswd:
                    return redirect('/login/')

            except User.DoesNotExist as e:
                return redirect('/login/')
            token = random.randrange(1, 100000)
            user.userToken = str(token)
            user.save()
            request.session['username'] = user.userName
            request.session['token'] = user.userToken
            return redirect('/mine/')
        else:
            return render(request, 'axf/login.html', {'title': '登录','form': f,'error':f.errors})
    else:
        f = LoginForm()
        return render(request,'axf/login.html',{'title':'登录','form':f})


def register(request):
    if request.method == 'POST':
        userAccount = request.POST.get('userAccount')
        userPasswd = request.POST.get('userPasswd')
        userName = request.POST.get('userName')
        userPhone = request.POST.get('userPhone')
        userAdderss = request.POST.get('userAddress')
        userRank = 0
        token = random.randrange(1,100000)
        userToken = str(token)
        f = request.FILES['userImg']
        userImg = os.path.join(settings.MEDIA_ROOT,userAccount+'.png')
        with open(userImg,'wb') as fp:
            for data in f.chunks():
                fp.write(data)
        user = User.createuser(userAccount,userPasswd,userName,userPhone,userAdderss,userRank,userToken,userImg)
        user.save()
        request.session['username'] = userName
        request.session['token'] = userToken
        return redirect('/mine/')
    else:
        return render(request,'axf/register.html',{'title':'注册'})


def checkuserid(request,flag):
    userid = request.POST.get('userid')
    if flag == "0":
        try:
            user = User.objects.get(userAccount=userid)
            return JsonResponse({'data':'该用户已经被注册','status':'error'})
        except User.DoesNotExist as e:
            return JsonResponse({'data':'ok','status':'success'})
    elif flag == "1":
        try:
            user = User.objects.get(userAccount=userid)
            return JsonResponse({'data': 'ok', 'status': 'success'})
        except User.DoesNotExist as e:
            return JsonResponse({'data': '该用户不存在。', 'status': 'error'})


def quit(request):
    logout(request)
    return redirect(reverse("axf:mine"))


def saveorder(request):
    token = request.session.get('token')
    if token == None:
        return JsonResponse({'data': -2, 'status': 'error'})
    user = User.objects.get(userToken=token)
    carts = Cart.obj1.filter(isChose=True)
    if carts.count == 0:
        return JsonResponse({'data': -2, 'status': 'error'})
    oid = random.randrange(1,10000)
    oid = "%d"%oid
    o = Order.createorder(oid,user.userAccount,0)
    o.save()
    for item in carts:
        item.isDelete = True
        item.orderid = oid
        item.save()
    return JsonResponse({"status":"success"})


def changephone(request):
    if request.method == 'POST':
        token = request.session.get('token')
        if token == None:
            return JsonResponse({'data': -2, 'status': 'error'})
        userAccount = request.POST.get('userAccount')
        userPhone = request.POST.get('userPhone')
        # print(userAccount)
        # print(userPhone)
        user = User.objects.get(userToken=token)
        user.userPhone = userPhone
        user.save()
        return redirect('/mine/')
    else:
        return render(request,'axf/changePhone.html',{'title':'修改信息'})


def orderlist(request):
    token = request.session.get('token')
    if token == None:
        return redirect(reverse('axf:login'))
    user = User.objects.get(userToken=token)
    orders = Order.objects.filter(userid=user.userAccount)
    for order in orders:
        order.browsedorder = False
        order.save()
    return render(request,'axf/orderlist.html',{'title':'订单','orders':orders})


def order(request,orderid):
    # print(orderid)
    token = request.session.get('token')
    if token == None:
        return JsonResponse({'data': -2, 'status': 'error'})
    # pprint(request.META)
    carts = Cart.obj2.filter(orderid=orderid)
    user = User.objects.get(userToken=token)
    orders = Order.objects.filter(userid=user.userAccount)
    currentorder = Order.objects.get(orderid=orderid)
    currentorderid = orderid
    currentorder.browsedorder = True
    currentorder.save()
    lastorderid = request.META['HTTP_REFERER'].split("/")
    # print("lastorderid",lastorderid)
    nextorderid = "none"
    orderids = []
    for order in orders:
        if order.browsedorder == False:
            orderids.append(order.orderid)
    # print("orderids", orderids)
    if len(orderids) !=0:
        nextorderid = orderids[0]
        # print("next", nextorderid)
    return render(request,'axf/order.html',{'title':'订单详情','cartlist':carts,'orderid':orderid,'nextorderid':nextorderid})


def ordernone(request):
    return render(request,'axf/ordernone.html')


def favorite(request):
    token = request.session.get('token')
    if token == None:
        return JsonResponse({'data': -1, 'status': 'error'})
    productid = request.POST.get("productid")
    user = User.objects.get(userToken=token)
    try:
        f = Favorite.objects.get(noRepeat=user.userAccount+productid)
        # print("不需新建")
    except :
        f = Favorite.createfavorite(user.userAccount,productid,user.userAccount+productid,False)
        # print("创建like成功")
    f.save()
    return JsonResponse({'status':'success'})


def favoritetype(request):
    token = request.session.get('token')
    if token == None:
        return redirect(reverse('axf:login'))
    user = User.objects.get(userToken=token)
    userid = user.userAccount
    favorites = Favorite.objects.filter(userAccount=userid)
    productlist = []
    for f in favorites:
        productlist.append(ProductGoods.objects.get(productid=f.productid))
    print(productlist)
    return render(request,'axf/favoritetype.html',{'userid':userid,'favorites':favorites,'productlist':productlist})


