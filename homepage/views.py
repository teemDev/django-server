from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from homepage.models import HomePageModel, AboutPageModel, CardPageModel, SkillPageModel, PortfolioPageModel, \
    BlogPageModel, ContactPageModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homepage'] = HomePageModel.objects.order_by('-pk').all()[:1]
        context['aboutpage'] = AboutPageModel.objects.order_by('-pk').all()[:1]
        context['cardpage'] = CardPageModel.objects.order_by('-pk').all()[:4]
        context['skillpage'] = SkillPageModel.objects.order_by('-pk').all()[:4]
        context['portfoliopage'] = PortfolioPageModel.objects.order_by('-pk').all()[:3]
        context['blogpage'] = BlogPageModel.objects.order_by('-pk').all()[:3]
        context['contactpage'] = ContactPageModel.objects.order_by('-pk').all()[:1]

        return 