"""
1. Я не хочу сохранять в базу один и тот же сайт дважды
2. http и https
"""



from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView
from django.core.exceptions import ValidationError
from django.contrib import messages


from .models import SiteMap, Site
from .forms import NewSiteForm


def ads_maker(request):
    sites = Site.objects.all()
    form = NewSiteForm(request.POST or None)
    paginator = Paginator(sites, 21)
    page_number = request.GET.get('page', default=1)
    sites = paginator.get_page(page_number)
    context = {
        'form': form,
        'sites': sites,
        'paginator': paginator,
    }
    if not form.is_valid():
        return render(request, 'ads_maker/index.html', context)

    site = Site()
    site.url = form.cleaned_data['url']
    site.check_status()
    if site.status == 200:
        site.save()
        messages.success(request, 'Your website added successfully')
        sites = Site.objects.all()
        paginator = Paginator(sites, 10)
        context['sites'] = paginator.get_page(1)

    else:
        form.add_error(None, 'Connection error')
    return render(request, 'ads_maker/index.html', context)


# class AdsMakerIndex(ListView, UpdateView):
#     model = Site
#     paginate_by = 10
#     template_name = 'ads_maker/index.html'
#     form_class = NewSiteForm
#     queryset = Site.objects.all()
#     context_object_name = 'sites'
#
#     # def post(self, request, *args, **kwargs):
#     #     self.object = self.get_object()  # assign the object to the view
#     #     form = self.get_form()
#     #     if form.is_valid():
#     #         email = form.cleaned_data.get("email")
#     #         return self.form_valid(form)
#     #     else:
#     #         return self.form_invalid(form)