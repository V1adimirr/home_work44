from django.urls import path
from webapp.views import check_view

urlpatterns = [
    path('', check_view),
]