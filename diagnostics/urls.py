from django.urls import path

from diagnostics.apps import DiagnosticsConfig
from diagnostics.views import DirectionsListView, DoctorListView, DiagnosticListView, DoctorDeleteView, \
    DiagnosticDeleteView, DirectionsDeleteView, DirectionsDetailView, ReviewListView, ReviewCreateView, \
    ReviewUpdateView, ReviewDeleteView

app_name = DiagnosticsConfig.name


urlpatterns = [
    # Главная страница
    path('', DirectionsListView.as_view(), name='home_page'),
    path('delete_directions/<int:pk>/', DirectionsDeleteView.as_view(), name='delete_directions'),
    path('directions_detail/<int:pk>/', (DirectionsDetailView.as_view()), name='directions_detail'),

    # Доктора
    path('doctors/', DoctorListView.as_view(), name='doctors'),
    path('delete_doctor/<int:pk>/', DoctorDeleteView.as_view(), name='delete_doctor'),

    # Услуги
    path('diagnostic_list/', DiagnosticListView.as_view(), name='diagnostic_list'),
    path('delete_diagnostic/<int:pk>/', DiagnosticDeleteView.as_view(), name='delete_diagnostic'),

    # Отзыв
    path('review_list/', ReviewListView.as_view(), name='review_list'),
    path('review_create/', ReviewCreateView.as_view(), name='review_create'),
    path('review_update/<int:pk>/', ReviewUpdateView.as_view(), name='review_update'),
    path('review_delete/<int:pk>/', ReviewDeleteView.as_view(), name='review_delete'),
]
