from django.shortcuts import render
from django.views.generic import TemplateView
import datetime

# Create your views here.
class HomeView(TemplateView):
    # template_name required by TemplateView
    template_name = 'home/index.html'

    def get(self, request):
        today = datetime.datetime.today()
        return render(request, self.template_name, {'today': today, 'message': 'Hello world from Django'})

class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get(self, request):
        message = "This is the about page"
        return render(request, self.template_name, {'message': message})

# to-do: create a page for gallert, the url is e.g. mywebsite.com/gallery/
# to-do: display the current Time (not the date) in the page gallery
