from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from apps.fansubs.models import Contrib
from apps.novels.models import Chapter


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Capítulos ordenados por fecha más recientes y por número visualizaciones
        context['hot_novels'] = Chapter.objects.all().order_by('-last_content', '-views')[:20]

        # Paginator 
        # Pienso quitarlo para dedicarle una vista exlusiva, en el home tendrá un btn de "ver más"
        uploads   = Contrib.objects.all().order_by('-creation_date')[:999]
        paginator = Paginator(uploads, 30)
        context['uploads'] = paginator.get_page(1)

        return context