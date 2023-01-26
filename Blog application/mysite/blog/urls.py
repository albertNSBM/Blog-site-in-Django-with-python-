from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('',views.Post_list,name='post_list'),
    path('<int:id>/',views.Post_detail,name='post_detail')
]
