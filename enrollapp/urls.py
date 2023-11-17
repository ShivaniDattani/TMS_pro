from django.urls import path
from enrollapp import views

#appname='enrollapp'

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/',views.sign_up, name='signup'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.user_change_pass, name='changepass'),
    # path('setpass/', views.user_set_pass, name='setpass'),
    path('userdetails', views.user_detail, name='userdetail'),
    path('userdetails/<int:id>', views.showuser_detail, name='showuserdetail')
]
