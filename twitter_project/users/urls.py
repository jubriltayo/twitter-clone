from django.urls import path, include
from . import views
from users import views as user_views

urlpatterns = [
    path('', user_views.register, name='register'),
    path('update/', user_views.profile_update, name='update'),
]