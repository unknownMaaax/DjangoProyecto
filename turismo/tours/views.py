from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin
from .models import Tour,TourFacade
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,"index.html",context=None)

class HomeToursView(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        tourFacade=TourFacade()
        return render(request,"tours.html",{"tours": tourFacade.buscarTours()})

class DetalleTourView(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        id=int(kwargs["id"])
        tourFacade=TourFacade()
        return render(request, 'tour.html',{"tour": tourFacade.buscarTour(id)})

class TourCreate(CreateView):
    model = Tour
    template_name = './tour_form.html'
    fields = '__all__'
class TourUpdate(UpdateView):
    model = Tour
    template_name = './tour_form.html'
    fields = ['nombre','dias']

class TourDelete(DeleteView):
    model = Tour
    template_name = './tour_confirm_delete.html'
    fields = reverse_lazy('tours')


# Create your views here.
