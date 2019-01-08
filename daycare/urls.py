from django.contrib import admin
from django.urls import path
from daycare import views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('daycare/activity', views.get_activity),
    path('daycare/sneakpeek', views.get_sneakpeek),
    path('daycare/profile', views.get_profile),
    path('daycare/events', views.get_attendance),
    path('daycare/notify', views.get_notification),
]
