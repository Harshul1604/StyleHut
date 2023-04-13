
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.home),
    path('contact/',mainapp.contact),
    path('checkout/',mainapp.checkout),
    path('shop/<str:mc>/<str:br>/<str:sc>/',mainapp.shop),
    path('shop-detail/<int:num>/',mainapp.shopdetail),
    path('blog/',mainapp.blog),
    path('about/',mainapp.about),
    path('sort-filter/<str:mc>/<str:br>/<str:sc>/',mainapp.sortFilter),
    path('search/',mainapp.searchpage),
    path('login/',mainapp.loginpage),
    path('logout/',mainapp.logoutpage),
    path('signup/',mainapp.signuppage),
    path('profile/',mainapp.profilepage),
    path('update-profile/',mainapp.updateProfilePage),
    path('add-to-cart/<int:num>/',mainapp.addToCartPage),
    path('cart/',mainapp.cartPage),
    path('delete-cart/<str:id>/',mainapp.deleteCartPage),
    path('update-cart/<str:id>/<str:op>/',mainapp.updateCartPage),
    path('order/<int:num>/',mainapp.orderPage),
    path('confirmation/',mainapp.confirmationPage),
    path('forget-username/',mainapp.forgetUsername),
    path('forget-otp/',mainapp.forgetOTP),
    path('forget-password/',mainapp.forgetPassword),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
