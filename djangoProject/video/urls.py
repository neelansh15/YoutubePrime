from django.urls import path
from . import views

urlpatterns=[
    # path('',views.index)
    path('video/',VideoView.as_view(),name='video_view')

]