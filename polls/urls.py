from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailsView.as_view(), name='details'),
    path('<int:question_id>/vote/',views.vote, name='vote'),
    path('<int:pk>/results',views.ResultsView.as_view(), name='results')
]
