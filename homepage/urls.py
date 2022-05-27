from django.urls import path

from homepage.views import HomePageView

app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name = 'firstpage')
]