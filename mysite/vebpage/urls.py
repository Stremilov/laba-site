from django.urls import path

from .views import (
    BasePageView,
    TermPageView,
    StagesPageView,
    PresentationPageView,
    PresentationPage3View,
    PresentationPage4View,
)


app_name = 'vebpage'

urlpatterns = [
    path('main/', BasePageView.as_view(), name='base'),
    path('terms/', TermPageView.as_view(), name='terms'),
    path('stages/', StagesPageView.as_view(), name='stages'),
    path('pres/', PresentationPageView.as_view(), name='presentation'),
    path('pres/3/', PresentationPage3View.as_view(), name='3-sl'),
    path('pres/4/', PresentationPage4View.as_view(), name='4-sl'),
]