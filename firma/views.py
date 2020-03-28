from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.shortcuts import render
from django.db.models import Q
from .models import Firm


def index(request):      # zrobić, żeby na tym widoku była też informacja o ostatnio wyszukiwanych firmach

    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(firm_name__icontains=query) | Q(add_date__icontains=query)

            results = Firm.objects.filter(lookups).distinct()

            context = {'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'firma/results.html', context)

        else:
            return render(request, 'firma/index.html')

    else:
        return render(request, 'firma/index.html')


def results(request, firm_name):
    firm = get_object_or_404(Firm, pk=firm_name)
    return render(request, 'firma/results.html', {'firm': firm})


# def last_searching_firm(request):
#     if request.method == 'POST':
#         query = request.POST.get('p')
#
#     if query is not None:
#         lookups = Q(firm_name__icontains=query) | Q(searching_date__icontains=query)
#
#         results = Firm.objects.filter(lookups).distinct()
#
#         context = {'results': results,
#                    }
#
#         return render(request, 'firma/results.html', context)



# class IndexView(generic.ListView):
#     template_name = 'firma/index.html'   #używamy template_name, aby powiedzieć ListView, by używała naszego istniejącego szablonu "firma/index.html".
#     context_object_name = 'latest_searching_list'  # dla ListView automatycznie generowaną zmienną kontekstową jest question_list. Aby to nadpisać nadajemy wartość atrybutowi context_object_name, wskazując, że chcemy użyć zamiast niej latest_question_list
#
#     def get_queryset(self):
#         """Return the last five searching firms. """
#         return Search.objects.filter(
#             searching_date__lte=timezone.now()
#         ).order_by('searching_date')[:5]


