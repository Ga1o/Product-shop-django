from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'main_app/index.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'main_app/about.html')