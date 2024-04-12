from django.contrib import admin
from django.urls import path
from GuvenWebScam.views import *
from django.urls import include
from GuvenWebUser import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('activate/<uid>/<token>/', include('djoser.urls.jwt')),
    path('activate/<uid>/<token>/', views.activate_account, name='activate'),
    path('scamreport/',get_all_scams),
    path('scamreport/<int:scam_id>/',get_scamreport_by_id),
    path('scamreport/createscamreport/',create_scam_report),
    path('scamreport/<int:scam_id>/update/',update_scam_report),
    path('scamreport/<int:id>/delete',delete_scam_report),
]
