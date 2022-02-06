
from django.urls import path
from data import views

from .forms import login,mypasswordchange
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home.as_view(),name='home'),
    path('product-detail/<int:pk>/', views.product_detail, name='product-detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('<int:pk>/', views.deleteordersview.as_view(), name='deleteordersview'),
    path('orders/', views.orders, name='orders'),

    path('paymentdone/',views.paymentdone,name='paymentdone'),

    path('password_change/', views.change_password.as_view(), name='password_change'),
    path('password_change/done/', views.password_changedone_view.as_view(), name='password_change_done'),
    path('password_reset/', views.password_reset.as_view(), name='password_reset'),
    path('password_reset/done/', views.password_reset_done.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name='app/login.html'), name='password_reset_complete'),


    path('mobile/', views.mobile, name='mobile'),
    path('electronics/', views.electronics, name='electronics'),



    path('accounts/login/',views.login.as_view(authentication_form=login), name='login'),
    path('accounts/logout/',views.logout, name='logout'),
    path('registration/', views.customerregistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('feedback/',views.feedback,name='feedback'),
    path('deletecart/<int:pk>/',views.Deletecart.as_view(),name='deletecart'),




]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
