from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, 'contact.html')


    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('home')


        return render(request, 'contact.html', {'form': form})






