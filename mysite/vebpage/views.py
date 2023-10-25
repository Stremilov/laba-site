from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class BasePageView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/main.html')


class TermPageView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/terms.html')


class StagesPageView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/stages.html')


class PresentationPageView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/presentation.html')


class PresentationPage4View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/4-sl.html')


class PresentationPage5View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/5-sl.html')


class PresentationPage6View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/6-sl.html')

class PresentationPage7View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/7-sl.html')

class PresentationPage8View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/8-sl.html')

class PresentationPage9View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/9-sl.html')

class PresentationPage10View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/10-sl.html')

class PresentationPage11View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/11-sl.html')

class PresentationPage12View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/12-sl.html')

class PresentationPage13View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/13-sl.html')

class PresentationPage14View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/14-sl.html')

class PresentationPage15View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/15-sl.html')

class PresentationPage16View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/16-sl.html')

class PresentationPage17View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/17-sl.html')

class PresentationPage18View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/18-sl.html')

class PresentationPage19View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/19-sl.html')

class PresentationPage20View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/20-sl.html')

class PresentationPage21View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/21-sl.html')

class PresentationPage22View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/22-sl.html')

class PresentationPage23View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/23-sl.html')

class PresentationPage24View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/24-sl.html')