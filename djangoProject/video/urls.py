from django.urls import path
# from . views import VideoView
from . import views
# from .views import VideoView


urlpatterns=[
    path('',views.index),
    path('abc/',views.VideoView.as_view())
    # path('',views.index)
    # path('',views.index)
    # path('video/',VideoView.as_view(),name='video_view')

]
