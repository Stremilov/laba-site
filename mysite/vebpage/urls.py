from django.urls import path

from .views import (
    BasePageView,
    TermPageView,
    StagesPageView,
    PresentationPageView,
    PresentationPage4View,
    PresentationPage5View,
    PresentationPage6View,
    PresentationPage7View,
    PresentationPage8View,
    PresentationPage9View,
    PresentationPage10View,
    PresentationPage11View,
    PresentationPage12View,
    PresentationPage13View,
    PresentationPage14View,
    PresentationPage15View,
    PresentationPage16View,
    PresentationPage17View,
    PresentationPage18View,
    PresentationPage19View,
    PresentationPage20View,
    PresentationPage21View,
    PresentationPage22View,
    PresentationPage23View,
    PresentationPage24View
)


app_name = 'vebpage'

urlpatterns = [
    path('main/', BasePageView.as_view(), name='base'),
    path('terms/', TermPageView.as_view(), name='terms'),
    path('stages/', StagesPageView.as_view(), name='stages'),
    path('pres/', PresentationPageView.as_view(), name='presentation'),
    path('pres/4/', PresentationPage4View.as_view(), name='4-sl'),
    path('pres/5/', PresentationPage5View.as_view(), name='5-sl'),
    path('pres/6/', PresentationPage6View.as_view(), name='6-sl'),
    path('pres/7/', PresentationPage7View.as_view(), name='7-sl'),
    path('pres/8/', PresentationPage8View.as_view(), name='8-sl'),
    path('pres/9/', PresentationPage9View.as_view(), name='9-sl'),
    path('pres/10/', PresentationPage10View.as_view(), name='10-sl'),
    path('pres/11/', PresentationPage11View.as_view(), name='11-sl'),
    path('pres/12/', PresentationPage12View.as_view(), name='12-sl'),
    path('pres/13/', PresentationPage13View.as_view(), name='13-sl'),
    path('pres/14/', PresentationPage14View.as_view(), name='14-sl'),
    path('pres/15/', PresentationPage15View.as_view(), name='15-sl'),
    path('pres/16/', PresentationPage16View.as_view(), name='16-sl'),
    path('pres/17/', PresentationPage17View.as_view(), name='17-sl'),
    path('pres/18/', PresentationPage18View.as_view(), name='18-sl'),
    path('pres/19/', PresentationPage19View.as_view(), name='19-sl'),
    path('pres/20/', PresentationPage20View.as_view(), name='20-sl'),
    path('pres/21/', PresentationPage21View.as_view(), name='21-sl'),
    path('pres/22/', PresentationPage22View.as_view(), name='22-sl'),
    path('pres/23/', PresentationPage23View.as_view(), name='23-sl'),
    path('pres/24/', PresentationPage24View.as_view(), name='24-sl'),
]