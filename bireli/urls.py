from django.urls import path

from bireli.views import page

urlpatterns = (
    path('<str:slug>/', page, name='page'),
    path('', page, name='homepage')
)
