from django.urls import path,re_path
from . import views

urlpatterns =[
path('',views.index,name='index'),
path('search/<int:id>',views.search,name='search'),
path('user/',views.user,name='users'),
]
