from django.db import models

# Create your models here.
class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class Mustbuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class Mainshow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=10)
    childcid_1 =models.CharField(max_length=10)
    productid_1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=10,null=True)
    childcid_2 = models.CharField(max_length=10,null=True)
    productid_2 = models.CharField(max_length=10,null=True)
    longname2 = models.CharField(max_length=50,null=True)
    price2 = models.CharField(max_length=10,null=True)
    marketprice2 = models.CharField(max_length=10,null=True)

    img3 = models.CharField(max_length=10,null=True)
    childcid_3 = models.CharField(max_length=10,null=True)
    productid_3 = models.CharField(max_length=10,null=True)
    longname3 = models.CharField(max_length=50,null=True)
    price3 = models.CharField(max_length=10,null=True)
    marketprice3 = models.CharField(max_length=10,null=True)


# 分类模型
class FoodType(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    #排序方式
    typesort = models.IntegerField()
    childtypenames = models.CharField(max_length=150)


class User(models.Model):
    userAccount = models.CharField(max_length=20,unique=True)
    userPasswd = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    userPhone = models.CharField(max_length=20)
    userAdderss = models.CharField(max_length=100)
    userImg = models.CharField(max_length=150)
    userRank = models.IntegerField()
    userToken = models.CharField(max_length=50)
    @classmethod
    def createuser(cls,account,passwd,name,phone,adderss,img,rank,token):
        u = cls(userAccount= account,userPasswd=passwd,userName=name,userPhone=phone,userAdderss=adderss,userImg=img,userRank=rank,userToken=token)
        return u
class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1, self).get_queryset().filter(isDelete=False)
class CartManager2(models.Manager):
    def get_queryset(self):
        return super(CartManager2, self).get_queryset().filter(isDelete=True)
class Cart(models.Model):
    userAccount = models.CharField(max_length=20)
    productid = models.CharField(max_length=10)
    productnum = models.IntegerField()
    productprice = models.CharField(max_length=10)
    isChose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=150)
    productname = models.CharField(max_length=100)
    orderid = models.CharField(max_length=20,default="0")
    isDelete = models.BooleanField(default=False)
    obj1 = CartManager1()
    obj2 = CartManager2()
    @classmethod
    def createuser(cls,userAccount,productid,productnum,productprice,isChose,productimg,productname,isDelete):
        c = cls(userAccount= userAccount,productid=productid,productnum=productnum,productprice=productprice,isChose=isChose,productimg=productimg,productname=productname,isDelete=isDelete)
        return c


class ProductGoods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=50)
    productlongname = models.CharField(max_length=100)
    # 是否是精选
    isxf = models.NullBooleanField(default=False)
    # 是否买一赠一
    pmdesc = models.CharField(max_length=10)
    specifics = models.CharField(max_length=20)
    price = models.FloatField(max_length=10)
    marketprice = models.FloatField(max_length=10,null=True)
    # 组id
    categoryid = models.CharField(max_length=10)
    # 子类组id
    childcid = models.CharField(max_length=10,null=True)
    childcidname = models.CharField(max_length=10,null=True)
    # 详情页id
    dealerid = models.CharField(max_length=10)
    # 库存
    storenums = models.IntegerField()
    # 销量
    productnum = models.IntegerField()
    # 定义一个变量后续用以与客户购买产品件数做比较，并赋值
    num = models.IntegerField(default=0)

class Order(models.Model):
    orderid = models.CharField(max_length=10)
    userid = models.CharField(max_length=20)
    # 订单进度
    progress = models.IntegerField()
    browsedorder = models.NullBooleanField(default=False)

    @classmethod
    def createorder(cls,orderid,userid,progress):
        o = cls(orderid=orderid,userid=userid,progress=progress)
        return o

class Favorite(models.Model):
    userAccount = models.CharField(max_length=20)
    productid = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)
    noRepeat = models.CharField(max_length=30,default=1)
    @classmethod
    def createfavorite(cls,userAccount,productid,noRepeat,isDelete):
        f = cls(userAccount=userAccount,productid=productid,noRepeat=noRepeat,isDelete=isDelete)
        return f



