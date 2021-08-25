from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns=[
    path('',HomePage,name="HomePage"),
    path('addPost',AddPost,name="AddPost"),
    path('registerUser',RegisterUser,name="RegisterUser"),
    path('loginUser',LoginUser,name="LoginUser"),
    path('logout/', Logout, name='Logout'),
    path('editText/<str:id>/',EditPost,name="EditPost"),
    path('deletePost/<str:id>/',DeletePost,name="DeletePost"),
]