from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('allmember/',views.allmember),
    path('searchmember/', views.searchmember),
    path('displaymember/<str:member_id>/', views.displaymember, name='displaymember'),
    path('newMember/',views.newMember),
    path('addMember/',views.addMember),
    path('filter_members/', views.filter_members, name='filter_members'), 
    path('delmember/',views.delmember),
    path('delete/',views.delete),
     # path('print_view/',views.print_view),
    ]
