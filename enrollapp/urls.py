from django.urls import path
from enrollapp import views
from django.views.generic.base import TemplateView 

#appname='enrollapp'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/',views.sign_up, name='signup'),
    path('profile/', views.user_profile, name='profile'),
    #path('',TemplateView.as_view(template_name="profile.html"), name="profile"),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.user_change_pass, name='changepass'),
    path('setpass/', views.user_set_pass, name='setpass'),
    path('userdetails/<int:id>', views.user_detail, name='userdetail'),
    path('',views.home, name='home'),
]
