from django.urls import path
from . import views
urlpatterns = [
    path('', views.glav,name= 'glav'),
    path('za/', views.zaks,name= 'za'),
    path('so/',views.sot, name='so'),
    path('poisk/',views.poisk, name='poisk'),
    path('zak/',views.zak, name='zak'),
]
