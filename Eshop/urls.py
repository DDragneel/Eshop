from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings


from MainApp import views as my
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',my.Home,name='home'),
    path('shop/<str:cn>/',my.Shop,name='shop'),
    path('shop2/<str:bn>/',my.Shop2,name='shop2'),
    path('product/<int:num>/',my.ProductDetails,name='product'),
    path('cart/',my.CartDetails,name='cart'),
    path('checkout/',my.CheckoutForm,name='checkout'),
    path('login/',my.Login,name='login'),
    path('signup/',my.SignUp,name="signup"),
    path('addproduct/',my.AddProduct,name='addproduct'),
    path('adminpage/',my.AdminPage,name="adminpage"),
    path('logout/',my.logout,name='logout'),
    path('delete/<int:num>',my.DeleteProduct,name='deleteproduct'),
    path('edit/<int:num>',my.editProduct,name='edit'),
    path('payment/', include(('payment.urls','payment'),namespace='payment')),
    path('paypal/',include('paypal.standard.ipn.urls')),
    #pip install django-paypal
]
urlpatterns=urlpatterns+staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,
                               document_root=settings.MEDIA_ROOT)