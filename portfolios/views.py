from django.shortcuts import render
from .models import Portfolio
from main.models import Header, Footer

# Create your views here.

def portfolio_detail(request, pk):
    header = Header.objects.first()
    footer = Footer.objects.first()
    pi = Portfolio.objects.filter(pk=pk).first()
    context = {'pi':pi, 'rate':[1,3,5,7,9], 'header':header, 'footer':footer}
    return render(request, 'item_preview.html', context)


def modal_portfolio_detail(request, pk):
    pi = Portfolio.objects.filter(pk=pk).first()
    context = {'pi':pi, 'rate':[1,3,5,7,9]}
    return render(request, 'modal_item_preview.html', context)
