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


class PresentationPage3View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/3-sl.html')


class PresentationPage4View(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'vebpage/4-sl.html')