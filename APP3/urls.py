from os import name
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from .views import login,register,forgotpassword,changepassword,home,logout,servcie,addcart,show_mycart,removecart,cartorder,serviceorder
from .views import payment,otp,edit_cart_qunatity
urlpatterns=[
    path('',login,name='loginpage'),
    path('logout/',logout,name='logout'),
    path('home/',home,name='home'),
    path('register/',register,name='registerpage'),
    path('forgotpassword/',forgotpassword,name='forgotpassword'),
    path('otp/',otp,name='otp'),
    path('changepassword/',changepassword,name='changepassword'),
    path('service/<int:p>',servcie,name='service'),
    path('addtocart/<int:d>/<str:s1>',addcart,name='cart'),
    path('changequnatity/<int:d>/<str:s1>',edit_cart_qunatity,name='cqa'),
    path('mycart/',show_mycart,name='mycart'),
    path('removecart/<int:d>',removecart,name='removecart'),
    path('myorder/',cartorder,name='myorder'),
    path('serviceorder/<int:d>/<str:s>',serviceorder,name='sorder'),
    path('pay/',payment,name='payment')
    ] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
