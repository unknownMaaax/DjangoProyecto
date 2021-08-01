from os import name
from django.conf.urls import url,re_path
from django.urls import path,include,reverse

from tours import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'tours/', views.HomeToursView.as_view(),name="tours"),
    url(r'tour/(?P<id>\d+)/',views.DetalleTourView.as_view(),name="detalle"),   
    url(r'^tour/create/$', views.TourCreate.as_view(success_url='/tours/'), name='tour_create'),
    url(r'^tour/(?P<pk>\d+)/update/$', views.TourUpdate.as_view(success_url='/tours/'), name='tour_update'),
    url(r'^tour/(?P<pk>\d+)/delete/$', views.TourDelete.as_view(success_url='/tours/'), name='tour_delete'),
    path('accounts/', include('accounts.urls')),
    path("accounts/",include("django.contrib.auth.urls"))
]