from django.urls import include, path

from core.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
