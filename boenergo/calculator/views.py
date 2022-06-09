from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import QuadraticForm, ColorsForm


class QuadraticView(TemplateView):
    template_name = 'quadratic.html'

    def get(self, request, *args, **kwargs):
        form = QuadraticForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = QuadraticForm()
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['s']
            c = form.cleaned_data['d']
            result = a+b+c
        args = {'form': form}
        return render(request, self.template_name, args)


class ColorsView(TemplateView):
    template_name = 'colors.html'

    def get(self, request, *args, **kwargs):
        form = ColorsForm()
        return render(request, self.template_name, {'form': form})

    # def post(self, request):
    #     form = QuadraticForm()
    #     if form.is_valid():
    #         a = form.cleaned_data['a']
    #         b = form.cleaned_data['s']
    #         c = form.cleaned_data['d']
    #         result = a+b+c
    #     args = {'form': form}
    #     return render(request, self.template_name, args)
