from . import views
from django.urls import path

app_name = 'shop'
urlpatterns = [
  path('', views.index,name='index'),
  path('<int:id>/',views.detail,name='detail'),
]
