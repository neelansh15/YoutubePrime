from django.urls import path
# from . views import VideoView
from . import views


urlpatterns=[
    path('',views.index),
    path('abc/',views.VideoView.as_view())

]
