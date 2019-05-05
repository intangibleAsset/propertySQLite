from django.shortcuts import render

from . forms import ItemForm
from . models import Item
# Create your views here.
from django.views import View

class Index(View):
    template_name = 'core/index.html'
    def get(self, request):
        form = ItemForm()
        context = {
        'form':form
        }
        return render(request, self.template_name,context)
    def post(self, request):
        pass
