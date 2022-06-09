# from .vies import TestView
from django.urls import path
from django.views.generic import TemplateView
from .views import QuadraticView, ColorsView

urlpatterns = [
    path('', TemplateView.as_view(template_name="task.html",
        extra_context={"header": "О сайте"})),
    path('quadratic/', QuadraticView.as_view()),
    path('colors/', ColorsView.as_view()),

]