from django.urls import path
from.import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('<int:id>', views.CandidateView.as_view(), name='candidate'),
]
