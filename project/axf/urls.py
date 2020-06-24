
from django.conf.urls import url,include

from . import views

urlpatterns = [
    url(r'^home/$', views.home,name='home'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market,name='market'),
    url(r'^cart/$', views.cart,name='cart'),
    url(r'^mine/$', views.mine,name='mine'),
    url(r'^login/$', views.login,name='login'),
    url(r'^register/$', views.register,name='register'),
    url(r'^checkuserid/(\d+)/$', views.checkuserid,name='checkuserid'),
    url(r'^quit/$', views.quit,name='quit'),
    url(r'^changecart/(\d+)/$', views.changecart,name='changecart'),
    url(r'^saveorder/$', views.saveorder,name='saveorder'),
    url(r'^changePhone/$', views.changephone,name='changePhone'),
    url(r'^orderlist/$', views.orderlist,name='orderlist'),
    url(r'^order/(\d+)/$', views.order,name='order'),
    url(r'^order/none/$', views.ordernone,name='ordernone'),
    url(r'^favorite/$', views.favorite,name='favorite'),
    url(r'^favoritetype/$', views.favoritetype,name='favoritetype'),
]
