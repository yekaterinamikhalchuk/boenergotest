import math
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import QuadraticForm, ColorsForm
import random

class QuadraticView(TemplateView):
    template_name = 'quadratic.html'
    form_class = QuadraticForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            a = float(request.POST['a'])
            b = float(request.POST['b'])
            c = float(request.POST['c'])
            discr = b ** 2 - 4 * a * c
            if discr > 0:
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                result = f'Корни уравнения: {round(x1, 1)}, {round(x2, 1)}'
            elif discr == 0:
                x = -b / (2 * a)
                result = f'Корень уравнения: {x}'
            else:
                result = 'Корней нет'
            args = {'form': form , 'result': result}
            return render(request, self.template_name, args)
        else:
            return redirect(request.META.get('HTTP_REFERER', '/'))




class ColorsView(TemplateView):
    template_name = 'colors.html'
    form_class = ColorsForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            var = int(request.POST['var'])
            color_dict = {}
            for i in range(99):
                color = random.choices(['Синий', 'Зеленый', 'Красный'], weights=[50, 30, 20])[0]
                color_dict[i] = color
            args = {'form': form, 'result': color_dict[var]}
            return render(request, self.template_name, args)
        else:
            return redirect(request.META.get('HTTP_REFERER', '/'))
