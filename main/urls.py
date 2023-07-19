
from django.urls import path
from . import views


# from .views import home
urlpatterns = [
    path('',views.home,name="home" ),
    path('logged/',views.logged,name="logged" ),
    path('about/',views.about,name="about" ),
    path('profile/',views.profile,name="profile" ),
    path('logout/',views.logout,name="logout" ),
    path('register/',views.register,name="register" ),
    path('logged/',views.logged,name="logged" ),
    path('post/<int:pk>', views.PostDetail ,name="post_detail"),
    path('add_blog/', views.add_blog, name="add_blog"),
    path("update_addblog/<int:id>",views.update_addblog,name="update_addblog"),
    path("delete_addblog/<int:id>",views.delete_addblog,name="delete_addblog"),
    

]
