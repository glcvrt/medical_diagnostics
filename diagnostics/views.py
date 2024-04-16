from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

from diagnostics.forms import ReviewForm
from diagnostics.models import Directions, Doctor, Diagnostic, Review


# Направления
class DirectionsListView(ListView):
    model = Directions
    template_name = 'diagnostics/home_page.html'


class DirectionsDeleteView(DeleteView):
    model = Directions
    # success_url = reverse_lazy('diagnostics:blog_list')


class DirectionsDetailView(DetailView):
    model = Directions
    permission_required = 'diagnostics.directions_detail'


# Доктора
class DoctorListView(ListView):
    model = Doctor
    template_name = 'diagnostics/doctors.html'

    # def get_context(self):
    #     context_data = get_category_cache()
    #     return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class DoctorDeleteView(DeleteView):
    model = Doctor


# Услуги
class DiagnosticListView(ListView):
    model = Diagnostic
    template_name = 'diagnostics/diagnostic_list.html'


class DiagnosticDeleteView(DeleteView):
    model = Diagnostic


# Отзывы
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('diagnostics:review_list')

    def form_valid(self, form):
        if form.is_valid():
            product = form.save()
            product.user = self.request.user
            product.save()

        return super().form_valid(form)


class ReviewListView(ListView):
    model = Review
    template_name = 'diagnostics/review_list.html'


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = reverse_lazy('diagnostics:review_list')


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('diagnostics:review_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object

    def test_func(self):
        _user = self.request.user
        _instance: Review = self.get_object()

        if _user == _instance.user:
            return True

        return self.handle_no_permission()
