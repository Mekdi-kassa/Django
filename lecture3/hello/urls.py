from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name ="index"),
    path("mekdi",views.mekdi ,name ="mekdi"),
    path("happy",views.happy,name="happy")
]